# This class is the node value of a tree
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

        # Augmenting the Tree so for all Node there is a height that can be used for
        # comparing the balance of a tree or subtree
        self.height = 0


# Creating the children and the parent using the class -> Node
# With is basically the BST itself
class Tree:
    def insert(self, root_, val):
        if not root_:
            return Node(val)
        elif val <= root_.value:
            root_.left = self.insert(root_.left, val)
        elif val > root_.value:
            root_.right = self.insert(root_.right, val)

        root_.height = 1 + max(get_height(root_.left), get_height(root_.right))
        balanceValue = get_balance(root_)

        # The four applicable rotation used
        if balanceValue > 1 and val < root_.left.value:
            return self.right_rotate(root_)
        if balanceValue < -1 and val > root_.right.value:
            print("The root", root_.value, "The val", val)
            return self.left_rotate(root_)
        if balanceValue > 1 and val > root_.left.value:
            root_.left = self.left_rotate(root_.left)
            return self.right_rotate(root_)
        if balanceValue < -1 and val < root_.right.value:
            root_.right = self.right_rotate(root_.right)
            return self.left_rotate(root_)
        else:
            return root_

    # rotate the tree or a subtree to the right
    # this is used when the left.height - right.height > 1
    def right_rotate(self, root_) -> Node:
        left_val = root_.left
        left_right = left_val.right

        # swapping
        left_val.right = root_
        root_.left = left_right

        left_val.height = 1 + max(get_height(left_val.left), get_height(left_val.right) - get_height(root_))
        root_.height = 1 + max(get_height(root_.left), get_height(root_.right))

        return left_val

    # rotate a tree or subtree to the left
    # this is used when the left.height - right.height < -1
    def left_rotate(self, root_) -> Node:
        right_val = root_.right
        right_left = right_val.left

        # swapping
        right_val.left = root_
        root_.right = right_left

        root_.height = 1 + max(get_height(root_.left), get_height(root_.right))
        right_val.height = 1 + max(get_height(right_val.left), get_height(right_val.right))

        return right_val

    # Printing the Pre-Order of the Tree
    def preOrder(self, root_):
        if not root_:
            return

        print(root_.value, end=" ")
        self.preOrder(root_.left)
        self.preOrder(root_.right)


# get the balance difference of a tree Node 
# return -1 if there is no left or right on the Node
# return the difference of the left.height and right.height of the the node
def get_balance(root_):
    if not root_:
        return -1
    return int(get_height(root_.left) - get_height(root_.right))


# returning the height of a Node
def get_height(root_):
    if not root_:
        return -1

    return root_.height


tree = Tree()
root = None
root = tree.insert(root, 10)
root = tree.insert(root, 8)
root = tree.insert(root, 9)
root = tree.insert(root, 13)
root = tree.insert(root, 12)
root = tree.insert(root, 11)
# root = tree.insert(root, 14)
print("Node value", root.value, "Node height", root.height)
print("Pre Order Traversal")
tree.preOrder(root)
