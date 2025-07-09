class Node:
    def __init__(self, data = 0):
        if data == 0:
            self.left = None
            self.data = int(input("Enter the data: "))
            self.right = None
class BST:
    def __init__(self):
        self.root = None
        print("Empty Node is Created..!")
    
    def add_node(self):
        new_node = Node()
        if self.root == Node:
            self.root = new_node
            return
        
        else:
            temp1 = new_node
            temp2 = None
            while temp1 != None:
                temp2 = temp1
                if new_node.data < temp1.data:
                    temp1 = temp1.left
                else:
                    temp1 = temp1.right
            if new_node.data < temp2.data:
                temp2.left = new_node
            else:
                temp2.right = new_node
    
    def search_tree(self, temp, search_data):
        if 