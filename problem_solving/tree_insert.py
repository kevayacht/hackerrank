from helpers.bst import BinarySearchTree


def main():
    tree = BinarySearchTree()
    arr = [4, 2, 3, 1, 7, 6]
    for i in range(len(arr)):
        tree.create(arr[i])
    tree.insert(6)


if __name__ == "__main__":
    main()
