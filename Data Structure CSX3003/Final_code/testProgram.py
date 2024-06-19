import random, time
# ---- BS Tree -----

from BinarySearchTree import *

# bst = BSTree()
# a = [4, 5, 12, -5, -87, 9, 1023, 3, 55, 66, 77, 88, 9999, 0, 14]
#
# import random
#
# random.shuffle(a)
#
# for k in a:
#     x = BST_Node(k)
#     bst.Tree_Insert(x)
#
# bst.print_BSTree()

# n = 100000
# bst = BSTree()
# a = [i for i in range(1,n+1)]
# for k in a:
#     x = BST_Node(k)
#     bst.Tree_Insert(x)
#
# counter = 0
# st = time.process_time()
#
# k = 2*n # n is the number of keys inserted
# for i in range(n):
#     v = random.randint(0, k)
#     x = bst.Tree_Search(v) # bst is the Binary Search Tree
#     if x is not None:
#         counter += 1
#
# et = time.process_time()
# # bst.print_BSTree()
# print(et-st)
# print(counter)


# ---- RB Tree -----

from RedBlackTree import *

n = 55

rbt = RBTree()
a = [i for i in range(5,n+1,5)]
print(a)
for k in a:
    x = RB_Node(k)
    rbt.RB_Insert(x)
# rbt.print_RBTree()


rbt.delete(35)
rbt.print_RBTree()

from BinarySearchTree import *

bst = BSTree()
for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)

bst.Tree_Delete(bst.Tree_Search(35))
bst.print_BSTree()



# import random, time
# counter = 0
# st = time.process_time()
# k = 2*n # n is the number of keys inserted
# for i in range(n):
#     v = random.randint(0, k)
#     x = rbt.Tree_Search(v) # rbt is the Red-Black Tree
#     if x != rbt.NULL:
#         counter += 1
#
# et = time.process_time()
# print(et-st)
# print(counter)


