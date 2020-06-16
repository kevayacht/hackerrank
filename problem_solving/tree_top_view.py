from helpers.bst import BinarySearchTree


# version 1
def topView(root):
    queue = []
    dicNodes = {0: root.info}
    queue.append([root, 0])

    while queue:
        node, position = queue.pop(0)
        if node.left:
            queue.append([node.left, position - 1])
            if not (position - 1) in dicNodes:
                dicNodes[position - 1] = node.left.info
        if node.right:
            queue.append([node.right, position + 1])
            if not position + 1 in dicNodes:
                dicNodes[position + 1] = node.right.info

    keys = sorted(dicNodes.keys())
    topView = [dicNodes[x] for x in keys]
    print(*topView)


# version 2
def top_view(root):
    def inner_view(node, depth, pos):

        if node.left:
            inner_view(node.left, depth + 1, pos - 1)

        if node.right:
            inner_view(node.right, depth + 1, pos + 1)

        if (pos in ans and depth < ans[pos][0]) or pos not in ans:
            ans[pos] = (depth, node)

    ans = {}
    inner_view(root, 0, 0)
    keys = sorted(ans.keys())
    for key in keys:
        print(ans[key][1].info, end=' ')


# my final solution.
def my_top_view(root):
    queue = [(root, 0)]
    top_view_dict = {0: root.info}

    while queue:
        # pop queue for use in iteration
        node, position = queue.pop(0)

        if node.left:
            # append to queue for pop use in next iteration
            queue.append((node.left, position - 1))
            # save in dict
            if not position - 1 in top_view_dict:
                top_view_dict[position - 1] = node.left.info  # write only value to the dict entry

        if node.right:
            # append to queue for pop use in next iteration
            queue.append((node.right, position + 1))
            # save in dict.
            if not position + 1 in top_view_dict:
                top_view_dict[position + 1] = node.right.info  # write only value to the dict entry

    keys = sorted(top_view_dict.keys())
    results = [top_view_dict[x] for x in keys]
    return results


def main():
    tree = BinarySearchTree()
    arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
    # 2 1 14 15 12
    for i in range(len(arr)):
        tree.create(arr[i])

    result = my_top_view(tree.root)
    print(*result, sep=" ")


if __name__ == "__main__":
    main()
