from RedBlackTree import *
import time
# ---- BS Tree -----


from BinarySearchTree import *

# bst = BSTree()
# a = [4, 5, 12, -5, -87, 9, 1023]

import random

# random.shuffle(a)

# for k in a:
#     x = BST_Node(k)
#     bst.Tree_Insert(x)

# bst.print_BSTree()

n = int(input("Enter n: "))

st1 = time.process_time()

bst2 = BSTree()
for k in range(1, n):
    x = BST_Node(k)
    bst2.Tree_Insert(x)

# bst2.print_BSTree()


counter = 0
k = 2*n
for i in range(n):
    v = random.randint(0, k)
    x = bst2.Tree_Search(v)
    if x != None:
        counter += 1
print(counter)
et1 = time.process_time()
print(f"running time: {et1-st1}")


# ---- RB Tree -----


# rbt = RBTree()
# a = [8, 6, 4, 5, 3]
# for k in a:
#     x = RB_Node(k)
#     rbt.RB_Insert(x)
# rbt.print_RBTree()

# k = len(a)//2

n = int(input("Enter n: "))
st = time.process_time()
rbt2 = RBTree()
for k in range(1, n+1):
    x = RB_Node(k)
    rbt2.RB_Insert(x)

# rbt2.print_RBTree()

counter = 0
k = 2*n
for i in range(n):
    v = random.randint(0, k)
    x = rbt2.Tree_Search(v)
    if x != rbt2.NULL:
        counter += 1
print(counter)

et = time.process_time()
print(f"running time: {et - st}")
