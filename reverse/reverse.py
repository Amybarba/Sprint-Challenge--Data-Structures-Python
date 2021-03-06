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
        if self.head is None:  # safeguard for head
            return             # implicit it will return None

        if node.next_node is None:  # safeguard if no additional nodes
            self.head = node        # defines node if only value
            node.next_node = prev   # instead of the next node following make it go reverse
        else:
            node_after = node.next_node  # else go to the next value
            node.next_node = prev        # point to the previous value
            self.reverse_list(node_after, node)  # reverse list
