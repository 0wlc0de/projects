from math import fabs

class Node:
    def __init__(self, root):

        # Augmenting the Binary Search Tree based on MITOpenCourseWare
        self.key = 1
        self.left = None
        self.right = None
        self.root = root
        self.parent = None

    def insert_node(self, val):
        if self.root:
            if val <= self.root:
                if self.left is not None:
                    self.left.insert_node(val)
                else:
                    self.left = Node(val)
                    self.left.parent = self

            if val > self.root:
                if self.right is not None:
                    self.right.insert_node(val)
                else:
                    self.right = Node(val)
                    self.right.parent = self
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
            return self

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

    # This solves the problem of getting the total nodes that are <= to the search value
    # This problem uses Augmentation in the BST
    # But this problem is not efficient and doesnt solve every problem. especially when we get an unbalanced tree
    # Complexity : O(h) where h is the height of the BST
    def problem_search(self, val):
        start_node = self.search_val(val)
        if start_node.right is not None:
            nodes = fabs(start_node.key - start_node.right.key)
        else:
            nodes = start_node.key
        if start_node.parent is not None and start_node.parent.root < start_node.root:
            start_node_dup = start_node
            while start_node_dup.parent is not None:
                if start_node_dup.parent.root > start_node_dup.root:
                    break
                else:
                    start_node_dup = start_node_dup.parent
            if start_node.right is not None:
                nodes = fabs(start_node_dup.key - start_node.right.key)
            else:
                nodes = start_node_dup.key
            return int(nodes)
        else:
            return int(nodes)


# Inserting nodes into the Binary Tree
BST = Node(49)
BST.insert_node(46)
BST.insert_node(79)
BST.insert_node(43)
BST.insert_node(64)
BST.insert_node(83)
BST.insert_node(48)
BST.insert_node(48)
BST.insert_node(33)


# How many nodes are there that are <= t?:
# ex. t = 79 : then the nodes that are <= to 79 is 8
# print("The 79 is at key : ", BST.search_val(49))
input_val = int(input("Enter specific node : "))
print(BST.problem_search(input_val))
