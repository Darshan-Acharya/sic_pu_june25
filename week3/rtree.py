class Node:
    def __init__(self, data = 0):
        if data == 0:
            self.left = None
            self.data = int(input("Enter the data to insert: "))
            self.right = None
class Rtree:
    def __init__(self):
        self.root = None

    def add_node(self):
        new_node = Node()
        if self.root == None:
            self.root = new_node
        elif self.root.left == None:
            self.root.left == new_node
        else:
            self.root.right == new_node
    def zig_zag_traversal(self, temp):
        if temp == None:
            return
        print(temp.data, end = "   ")
        self.zig_zag_traversal(temp.right)
        self.zig_zag_traversal(temp.left)