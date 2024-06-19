import sys
sys.setrecursionlimit(10001)


class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.left = None
            self.right = None

    def Inorder_Tree_Walk(self, x):
        if x is not None:
            self.Inorder_Tree_Walk(x.left)
            print(x.key)
            self.Inorder_Tree_Walk(x.right)

    def Tree_Minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def Tree_Maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def Tree_Successor(self, x):
        if x.right is not None:
            return self.Tree_Minimum(x.right)

        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    def Transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        if v is not None:
            v.p = u.p

    def Tree_Delete(self, z):
        if z.left is None:
            self.Transplant(z, z.right)
        elif z.right is None:
            self.Transplant(z, z.left)
        else:
            y = self.Tree_Minimum(z.right)
            if y.p != z:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.Transplant(z, y)
            y.left = z.left
            y.left.p = y

    def Tree_Search(self, x, k):
        if x is None or x.key == k:
            return x

        result = self.Tree_Search(x.left, k)
        if result is not None:
            return result

        return self.Tree_Search(x.right, k)

    def Tree_Insert(self, z):
        if self.root is None:
            self.root = z
        else:
            q = [self.root]

            while q:
                node = q.pop(0)
                if node.left is None:
                    node.left = z
                    z.p = node
                    break
                elif node.right is None:
                    node.right = z
                    z.p = node
                    break
                else:
                    q.append(node.left)
                    q.append(node.right)

    # Function to print
    def printCall(self, node, indent, last):
        if node is not None:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            print(str(node.key))
            self.printCall(node.left, indent, False)
            self.printCall(node.right, indent, True)

    # Function to call print
    def print_BSTree(self):
        self.printCall(self.root, "", True)


# Example usage for two binary trees
if __name__ == "__main__":
    # Create two instances of BinaryTree
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree3 = BinaryTree()

    # Create nodes and insert them into the first tree
    node1 = tree1.Node(5, "Data for key 5")
    node2 = tree1.Node(3, "Data for key 3")
    node3 = tree1.Node(8, "Data for key 8")
    tree1.Tree_Insert(node1)
    tree1.Tree_Insert(node2)
    tree1.Tree_Insert(node3)

    # Create nodes and insert them into the second tree
    node4 = tree2.Node(10, "Data for key 10")
    node5 = tree2.Node(7, "Data for key 7")
    node6 = tree2.Node(12, "Data for key 12")
    tree2.Tree_Insert(node4)
    tree2.Tree_Insert(node5)
    tree2.Tree_Insert(node6)

    # Print both trees
    print("Binary Tree 1:")
    tree1.print_BSTree()

    print("\nBinary Tree 2:")
    tree2.print_BSTree()

    node7 = tree3.Node(15, "Data for key 15")
    node8 = tree3.Node(13, "Data for key 13")
    node9 = tree3.Node(17, "data for key 17")
    tree3.Tree_Insert(node7)
    tree3.Tree_Insert(node8)
    tree3.Tree_Insert(node9)

    print("Binary Tree 3:")
    tree3.print_BSTree()
