from helpers.bst import BinarySearchTree


def level_order(root):
    level_order_list = []
    q = [root]
    while q:
        n = q.pop(0)
        level_order_list.append(n.info)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

    return level_order_list


def main():
    tree = BinarySearchTree()
    arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
    # 2 1 14 15 12
    for i in range(len(arr)):
        tree.create(arr[i])

    result = level_order(tree.root)


if __name__ == "__main__":
    main()
