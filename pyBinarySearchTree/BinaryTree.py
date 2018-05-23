class Node:
    def __init__(self, root):
        self.key = 1
        self.left = None
        self.right = None
        self.root = root

    def insert_node(self, val):
        if self.root:
            if val <= self.root:
                if self.left is not None:
                    self.left.insert_node(val)
                else:
                    self.left = Node(val)
                    self.key += 1
            if val > self.root:
                if self.right is not None:
                    self.right.insert_node(val)
                else:
                    self.right = Node(val)
                    self.key += 1

    def search_val(self, val):
        if val < self.root:
            if self.left is not None:
                return self.left.search_val(val)
            else:
                return "Th e" + str(val) + " value cannot be found on these Tree..."
        elif val > self.root:
            if self.right is not None:
                return self.right.search_val(val)
            else:
                return "The " + str(val) + " value cannot be found on these Tree..."
        else:
            return str(self.root) + " is found in the Tree"

    def get_left_child(self):
        if self.left is not None:
            return self.left
        else:
            return None

    def get_right_child(self):
        if self.right is not None:
            return self.right
        else:
            return None


BST = Node(10)
BST.insert_node(7)
BST.insert_node(8)
BST.insert_node(9)
BST.insert_node(13)
print(BST.search_val(13))
print("The right Child key is : ", BST.get_right_child().key)
print(BST.sort())
