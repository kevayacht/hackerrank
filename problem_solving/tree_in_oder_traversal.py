from helpers.bst import BinarySearchTree


def outer(root):
    mylist = []

    def inner(node):
        if node:
            inner(node.left)
            mylist.append(node.info)
            inner(node.right)
        return mylist

    final_list = inner(root)
    return final_list


def main():
    tree = BinarySearchTree()
    arr = [4, 6, 5, 7, 2, 1, 3]
    for i in range(len(arr)):
        tree.create(arr[i])

    result = outer(tree.root)
    print(*result, sep=" ")


if __name__ == "__main__":
    main()
