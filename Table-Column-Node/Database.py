from Node import Node
from Column import Column

class Database:

    def __init__(self, col: Column = None):
        self.root_col = col.get_root()
        self.leaf_col = col.get_leaf()

    def get_row_index(self, index: int) -> list[Node]:
        node = self.root_col[index]
        return node.get_connected()
    
    def append_col(self, col_or_lst: Column|list) -> None:
        col = col_or_lst if isinstance(col_or_lst, Column) else Column(col_or_lst)
        self.leaf_col.add_next_Column(col)
        self.leaf_col = col

    def get_table(self, reverse: bool = False, get_content: bool = False) -> list[list[Node]]:
        table = []
        for node in self.root_col:
            table.append(node.get_connected(reverse, get_content))
        return table
    
    def print_table(self, reverse: bool = False, get_content: bool = False) -> str:
        table = self.get_table(reverse, get_content)
        return '\n'.join([str([node for node in col]) for col in table])
    
    def __getitem__(self, index: int):
        result = self.root_col
        for _i in range(index):
            result = result.next
        return result
    
    def __setitem__(self, index: int, col: Column):
        curr = self[index]
        prev = curr.prev
        next = curr.next
        if curr is not self.root_col:
            prev.add_next_Column(col)
        if curr is not self.leaf_col:
            col.add_next_Column(next)
        self.root_col = col if curr is self.root_col else self.root_col
        self.leaf_col = col if curr is self.leaf_col else self.leaf_col
        curr.initialize()
        del curr
    
    def __delitem__(self, index):
        curr = self[index]
        prev = curr.prev
        next = curr.next
        if curr is self.root_col:
            next.set_as_root()
            self.root_col = next
        elif curr is self.leaf_col:
            prev.set_as_leaf()
            self.leaf_col = prev
        else:
            prev.add_next_Column(next)
        curr.initialize()
        del curr