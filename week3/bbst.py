#Node creation
#BST class *add Node delete Node pre-in-post order traversal menu class start app
class Node:
    def __init__(self, data=0):
        if data == 0:
            self.left = None
            self.data = int(input("Enter the data for Node: "))
            self.right = None

class BST():
    def __init__(self):
        self.root = None

    def add_node(self):
        new_node = Node()
        if self.root == None:
            self.root = new_node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if temp2.data < new_node.data:
            temp2.right = new_node
        else:
            temp2.left = new_node
    
    def in_order(self, temp):
        if temp == None:
            print("Tree is empty")
            return
        self.in_order(temp.left)
        print(temp.data, end = "  ")
        self.in_order(temp.right)

    def pre_order(self, temp):
        if temp == None:
            print("Tree is empty")
            return
        print(temp.data, end = "  ")
        self.pre_order(temp.left)
        self.pre_order(temp.right)


    def post_order(self, temp):
        if temp == None:
            print("Tree is empty")
            return
        self.post_order(temp.left)
        self.post_order(temp.right)
        print(temp.data, end = "  ")
    def node_search(self, temp, search_data):
        if 


        