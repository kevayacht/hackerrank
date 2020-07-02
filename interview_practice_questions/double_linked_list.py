
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.data)
            node = node.next

        return nodes  # " ".join(nodes)


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# def SortedInsert(head, data):
#     node = Node(data,None,None)
#     if (head == None):
#         return node
#     elif (data < head.data):
#         node.next = head
#         head.prev = node
#         return node
#     else:
#         node = SortedInsert(head.next, data)
#         head.next = node
#         node.prev = head
#         return head

def insert_node_at_position(head, data):
    if not head:
        raise Exception("Linked list is empty")

    count = 0
    node = head
    while node is not None:
        if node.data < data < node.next.data:
            new_node = DoublyLinkedListNode(data)

            new_node.next = node.next
            new_node.prev = node

            node.next.prev = new_node
            node.next = new_node

            break

        count += 1
        node = node.next

    return head


def main():
    contents = [1, 3, 4, 10]  # 0, 1, 2
    data = 5

    llist = DoublyLinkedList()
    for i in contents:
        llist.insert_node(i)

    result = llist.__repr__()
    print(result)

    new_list_head = insert_node_at_position(llist.head, data)

    result = llist.__repr__()
    print(result)


if __name__ == "__main__":
    main()
