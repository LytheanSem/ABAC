import sys
sys.setrecursionlimit(10001)

root = None
        

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)


def Tree_Minimum():
    # Replace "pass" with your code
    pass

def Tree_Maximum():
    # Replace "pass" with your code
    pass

def Tree_Successor(x):
    # Replace "pass" with your code
    pass

'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''

def Transplant(u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    pass 

def Tree_Delete(z):
    # Replace "pass" with your code
    pass    

def Tree_Search(k):
    global root

    # Replace "pass" with your code
    pass

def Tree_Insert(z):
    global root

    # Replace "pass" with your code
    pass

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )


        
