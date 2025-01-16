from Node import Node

class Column:

    @staticmethod
    def Column_to_list(col: "Column") -> list[Node]:
        return [str(node) for node in col.col]

    def __init__(self, col: list, prev: "Column" = None, next: "Column" = None):
        self.col: list[Node] = col if all(isinstance(element, Node) for element in col) else [Node(i) for i in col]
        self.prev = prev
        self.next = next
    
    def set_as_root(self) -> None:
        self.prev = None
    
    def set_as_leaf(self) -> None:
        self.next = None

    def get_root(self) -> "Column":
        root = self
        while self.prev is not None:
            root = self.prev
        return root

    def get_leaf(self) -> "Column":
        leaf = self
        while self.next is not None:
            leaf = self.next
        return leaf
    
    def add_next_Column(self, next: "Column") -> None:
        if len(self.col) != len(next.col):
            raise ValueError("The lengths of the two lists must be equal.")

        for i in range(len(self.col)):
            self.col[i].add_next_node(next.col[i])
        self.next = next
        next.prev = self
    
    def sort(self, reverse: bool = False) -> None:
        self.col.sort(reverse=reverse)

    def set_row(self, root: "Column", row_index: int, row: Node) -> None:
        new_row = row.get_connected()
        old_row = self.col[row_index].get_connected()
        if len(new_row) != len(old_row):
            raise ValueError("The new row and the old row must have the same length")
        
        for node in new_row:
            root.col[row_index] = node
            root = root.next

    def initialize(self) -> None:
        self.prev = None
        self.next = None
        del self.col
        self.col = None

    def __getitem__(self, index: int):
        return self.col[index]
    
    def __setitem__(self, index: int, value: Node):
        self.col[index].content = value.content
    
    def __delitem__(self, index):
        del self.col[index]

    def __iter__(self):
        for item in self.col:
            yield item

    def __str__(self):
        return str(Column.Column_to_list(self))