class Node:

    def __init__(self, content, prev: "Node" = None, next: "Node" = None):
        self.content = content
        self.prev = prev
        self.next = next
    
    def get_connected(self, reverse: bool = False, get_content: bool = False) -> list["Node"]:
        get_prev = lambda node: node.prev
        get_next = lambda node: node.next
        if reverse:
            get_prev, get_next = get_next, get_prev

        root = self
        while get_prev(root) is not None:
            root = get_prev(root)
        
        element = lambda root: root.content if get_content else root
        lst = [element(root)]
        while get_next(root) is not None:
            root = get_next(root)
            lst.append(element(root))
        return lst

    def add_next_node(self, next: "Node") -> None:
        self.next = next
        next.prev = self

    def __lt__(self, other: "Node"):
        return self.content < other.content
    
    def __eq__(self, other: "Node"):
        return self.content == other.content
    
    def __hash__(self):
        return hash(self.content)
    
    def __str__(self):
        return f"Node({self.content})"