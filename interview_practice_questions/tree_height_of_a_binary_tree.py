class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1


def lca(root, n1, n2):
    """
    Lowest common ancestor.

    Recursive function to deep dive and find the lowest common ancestor in a BST.
    :param root:
    :param n1:
    :param n2:
    :return:
    """
    if root is None:
        return None

    if n1 < root.info and n2 < root.info:
        return lca(root.left, n1, n2)

    if n1 > root.info and n2 > root.info:
        return lca(root.right, n1, n2)

    return root


def check_bst(root, lefty=None, righty=None):
    """
    Checks if a BST is a valid BST:
    1. left is min
    2. right is max
    3. data is distinct.

    """
    if root is None:
        return True

    if lefty is not None and root.info <= lefty.info:
        return False

    if righty is not None and root.info >= righty.info:
        return False

    return check_bst(root.left, lefty, root) and check_bst(root.right, root, righty)


def isBSTUtil(root, prev):
    # traverse the tree in inorder fashion
    # and keep track of prev node
    if root is not None:
        if isBSTUtil(root.left, prev):
            return False

        # Allows only distinct valued nodes
        if prev is not None and root.data <= prev.data:
            return False

        prev = root
        return isBSTUtil(root.right, prev)

    return True


def isBST(root):
    prev = None
    return isBSTUtil(root, prev)


def checkBST(root):
    bst_list = []

    def inorder(node):
        if node.info:

            # if root node has a left, we go in with recursion until we hit the left most (in order traversal.)
            if node.left:
                inorder(node.left)

            bst_list.append(node.info)

            if node.right:
                inorder(node.right)

        return bst_list

    inorder_list = inorder(root)
    set_ = set(inorder_list)
    set_list = list(set_)
    sorted_set_list = sorted(set_list)
    return sorted_set_list == inorder_list

def main():
    tree = BinarySearchTree()

    arr = [4, 6, 5, 7, 2, 1, 3]
    # arr = [1, 2, 3, 4, 5, 6, 7]
    for i in range(len(arr)):
        tree.create(arr[i])

    # result = height(tree.root)
    # print(result)

    # n1 = 1
    # n2 = 6
    # res = lca(tree.root, n1, n2)
    # print(res)

    # res = check_bst(tree.root, None, None)
    res = checkBST(tree.root)
    print(res)


if __name__ == "__main__":
    main()
