from helpers.bst import BinarySearchTree


def outer(root):
    mylist = []

    def left_inner(node):
        if node:
            mylist.append(node.info)
            left_inner(node.left)
        return mylist

    def right_inner(node):
        if node:
            mylist.append(node.info)
            right_inner(node.right)
        return mylist

    left_ = left_inner(root)
    print(*left_, sep=" ")
    right_ = right_inner(root)
    print(*right_, sep=" ")

    return right_


def main():
    tree = BinarySearchTree()
    arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
    # 2 1 14 15 12
    for i in range(len(arr)):
        tree.create(arr[i])

    result = outer(tree.root)
    print(*result, sep=" ")


if __name__ == "__main__":
    main()
