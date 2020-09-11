class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # new_node = Node(self.head)
        # while new_node.next_node is not None:
        #     # store next node
        #     next1 = new_node.next_node
        #     # reverse current node's pointer
        #     new_node.next_node = prev
        #     # move pointer one position ahead
        #     self.head = prev
        #     new_node = next1
        if node is None or node.get_next() is None:
            self.head = node
            return node
# recursively call reverse_list with next node until end of list is reached
        reversed_list = self.reverse_list(node.get_next(), node)

        node.next_node.next_node = node
        return reversed_list
