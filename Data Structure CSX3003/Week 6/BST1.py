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


def Tree_Minimum(x):
    while x.left != None:
        x = x.left
    return x


def Tree_Maximum(x):
    while x.right != None:
        x = x.right
    return x


def Tree_Successor(x):
    if x.right != None:
        return Tree_Minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y


'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''


def Transplant(T, u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p


def Tree_Delete(T, z):
    if z.left == None:
        Transplant(T, z, z.right)
    elif z.right == None:
        Transplant(T, z, z.left)
    else:
        y = Tree_Minimum(z.right)
        if y.p != z:
            Transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        Transplant(T, z, y)
        y.left = z.left
        y.left.p = y


def Tree_Search(x, k):
    global root
    if x == None or k == x.key:
        return x
    if k < x.key:
        return Tree_Search(x.left, k)
    else:
        return Tree_Search(x.right, k)


def Tree_Insert(z):
    global root

    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

# Function to print


def printCall(node, indent, last):
    if node != None:
        print(indent, end=' ')
        if last:
            print("R----", end=' ')
            indent += "     "
        else:
            print("L----", end=' ')
            indent += "|    "

        print(str(node.key))
        printCall(node.left, indent, False)
        printCall(node.right, indent, True)

# Function to call print


def print_BSTree(root):
    printCall(root, "", True)


# Create nodes with keys and data
node1 = node(5, "Data for key 5")
node2 = node(3, "Data for key 3")
node3 = node(8, "Data for key 8")
node4 = node(2, "Data for key 2")
node5 = node(4, "jutgjhghjg")
node6 = node(7, "Data for key 7")
node7 = node(9, "Data for key 9")

# Insert nodes into the binary search tree
Tree_Insert(node1)
Tree_Insert(node2)
Tree_Insert(node3)
Tree_Insert(node4)
Tree_Insert(node5)
Tree_Insert(node6)
Tree_Insert(node7)

# Print the binary search tree to verify the insertion
print_BSTree(root)

search_key1 = 4
result_node1 = Tree_Search(root, search_key1)

print(f" search data: {result_node1.data}")

if result_node1:
    print(f"Node with key {search_key1} found. Data: {result_node1.data}")
else:
    print(f"Node with key {search_key1} not found.")

# Test Tree_Search() with a key that does not exist in the tree
search_key2 = 6
result_node2 = Tree_Search(root, search_key2)

if result_node2:
    print(f"Node with key {search_key2} found. Data: {result_node2.data}")
else:
    print(f"Node with key {search_key2} not found.")

# print("Deleting node with key 3...")
# Tree_Delete(root, node2)
# print("Binary Search Tree after deletion:")
# print_BSTree(root)

# # Test the Tree_Delete function by deleting another node
# print("Deleting node with key 5...")
# Tree_Delete(root, node1)
# print("Binary Search Tree after deletion:")
# print_BSTree(root)

# Tree_Search(root, 5)
# print_BSTree(root)

# new_node = node(5, "data")
# Tree_Insert(new_node)

# result_node = Tree_Search(root, 5)
# if result_node:
#     print(result_node.data)
# else:
#     print("Node not found.")

# print_BSTree(root)
