class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:  # if lower than self.value go to left
            if self.left is None:
                self.left = BSTNode(value)  # if left is None, set new node with value as left,
            else:
                self.left.insert(value)  # else insert to the left

        elif value >= self.value:  # if greater or equal than self.value go to right of tree
            # if right is empty, set value is right, else insert when an empty
            if self.right is None:
                self.right = BSTNode(value)  # if right is None, set new node with value as right,
            else:
                self.right.insert(value)  # else insert to the right

        # Return True if the tree contains the value
        # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # return self.value if self.right is None else self.right.get_max()
        if self.right is not None:  # if there is a right node,
            return self.right.get_max()  # return max of sub-tree(ast the right sub-tree to give its max
        else:  # else return
            return self.value  # self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)  # using/calling the function of the value stored in self.value
        if self.left is not None:  # call rest of nodes
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    def print_for_each(self):
        print(self.value) # print the top of the tree
        if self.left is not None:
            self.left.print_for_each()
        if self.right is not None:
            self.right.print_for_each()

    # Part 2 -----------------------
    """
                8
            3       10
        1     6        14
           4  7      13
    """

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # when function does not use self it is considered static
    def in_order_print(self, node): # 1 3 4 6 7 8 10 13 14 (# LEFT, ROOT, RIGHT)
        # LEFT
        if node.left is not None:
            node.in_order_print(node.left)

        # ROOT
        print(node.value)

        # RIGHT
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node): # 8 3 10 1 6 14 4 7 13
        queue = Queue()
        queue.enqueue(node)

        while len(queue) > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)


    """ node_queue = [node]
    while node_queue: # while list is not empty[]
        node = node_queue.pop(0) # dequeue
        print(node.value)
        if node.left:
            node_queue.append(node.left)
        if node.right:
            node_queue.apend(node.right)  # enqueue
    Alfredo's alternative method 
    """

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while len(stack) > 0:
            node = stack.pop()

            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)
            print(node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):  # (ROOT, LEFT, RIGHT)

        # ROOT
        print(node.value)

        # LEFT
        if node.left is not None:
            node.pre_order_dft(node.left)

        # RIGHT
        if node.right is not None:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node): # (LEFT, RIGHT, ROOT)

        # LEFT
        if node.left is not None:
            node.post_order_dft(node.left)

        # RIGHT
        if node.right is not None:
            node.post_order_dft(node.right)

        # ROOT
        print(node.value)