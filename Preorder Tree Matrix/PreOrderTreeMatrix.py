#Maggie Mulhall
#
#This Program accepts a list of numbers from numbers.txt
# Objective:
#  Creates a binary tree
#  Reads the tree in preorder traversal
#  Outputs the resulted adjacency matrix

#!! BESURE TO PUT NUMBERS.TXT IN REFERENCEABLE PLACE!!

#Initalize list of node objects
nodes=[]

#Node class
class Node:
    def __init__(self, d):
        self.Data, self.Left, self.Right = d, None, None
    def get_nodeVal(self):
        return self.Data
    def get_nodeVal_Left(self):
        return self.Left
    def get_nodeVal_Right(self):
        return self.Right

#Tree class
class Tree:
    def __init__(self, d=None):
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)
            nodes.append(self.Root)

    #Getter of root
    def get_root(self):
        if self.Root:
            return self.Root.Data
    
    #Getter of root left node
    def get_left(self):
        return self.Root.Left
    
    #Getter of root right node
    def get_right(self):
        return self.Root.Right

    def insert(self, d):
        #Insert value in correct place in tree
        
        #Add new node object to node array
        def __insertHere__(n, d):
            if (n.Data > d):   # if no node left, insert here
                if (n.Left == None):
                    n.Left = Node(d)
                    nodes.append(n.Left)
                else:          # or try left child
                    __insertHere__(n.Left, d)
                    
            elif (n.Data < d): # if no node right, insert here
                if (n.Right == None):
                    n.Right = Node(d)
                    nodes.append(n.Right)
                else:          # or try right child
                    __insertHere__(n.Right, d)
                    
        if (self.Root == None): # check if tree is empty
            self.Root = Node(d)
            nodes.append(self.Root)
        else:
            if (self.Root.Data > d):          # try left child
                if (self.Root.Left == None):  # if empty, insert here
                    self.Root.Left = Node(d)
                    nodes.append(self.Root.Left)
                else:                         # if left is full, try left subtree
                    __insertHere__(self.Root.Left, d)
                    
            elif (self.Root.Data < d):        # try right child
                if (self.Root.Right == None): # if empty, insert here
                    self.Root.Right = Node(d)
                    nodes.append(self.Root.Right)
                else:                         # if right is full, try right subtree
                    __insertHere__(self.Root.Right, d)
                    
    #Print tree in preorder
    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---"*h, n.Data)
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")

#Read numbers in from file   
def readNums(fileName):
    f = open(fileName,"r")
    numbers = [int(line.strip()) for line in f.readlines()]
    return numbers

#Create matrix
def create_adjacency_matrix(nodes,numbers):
    n = len(nodes)
    
    matrix = [[0] * n for _ in range(n)]
    height=0
    for i in nodes:
        index=numbers.index(i.get_nodeVal())
        
        #If left child node, add the edge weight to matrix
        if i.get_nodeVal_Left():
            index_left=numbers.index(i.get_nodeVal_Left().get_nodeVal())
            weight_Left=abs(i.get_nodeVal() - i.get_nodeVal_Left().get_nodeVal())
            matrix[height][index_left] = weight_Left
        
        #If right child node, add the edge weight to matrix
        if i.get_nodeVal_Right():
            index_right=numbers.index(i.get_nodeVal_Right().get_nodeVal())
            weight_Right=abs(i.get_nodeVal() - i.get_nodeVal_Right().get_nodeVal())
            matrix[height][index_right] = weight_Right
        
        height+=1
    return matrix

def pre_order_traversal(root):
    if not root:
        return []
    result = [root.Data]
    result += pre_order_traversal(root.Left)
    result += pre_order_traversal(root.Right)
    return result

#call and display matrix
def call_matrix(nodes,numbers):
    matrix = create_adjacency_matrix(nodes,numbers)
    for row in matrix:
        print(row)

#Main function of operations
def main():
    #Import numbers from txt file
    fileName="numbers.txt"
    numbers_unsorted=readNums(fileName)
        
    #Initalize tree and add numbers
    myTree = Tree()
    for num in numbers_unsorted:
        myTree.insert(num)
    
    #Sort tree in PreOrder
    print("Preorder tree:")
    sorted=pre_order_traversal(myTree.Root)
    myTree.printPreorder()
   
    #Initalize matrix
    call_matrix(nodes,sorted)

#Call main function
main()