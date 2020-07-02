class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.data)
            node = node.next

        return nodes # " ".join(nodes)

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = self.next

def insert_node_at_head(llist, data):

    if llist is None:
        llist = SinglyLinkedListNode(data)

    else:
        new = SinglyLinkedListNode(data)
        new.next = llist
        llist = new
    return llist

    # def add_after(self, position):
    #
    #     if not self.head:
    #         raise Exception("Linked list is empty")
    #
    #     count = 0
    #     for node in self:
    #         if count == position:
    #             new_node.next = node.next
    #             node.next = new_node
    #             return
    #         count += 1


def insert_node_at_position(head, data, position):
    if not head:
        raise Exception("Linked list is empty")

    count = 0
    node = head
    while node is not None:
        if count == position-1:
            new_node = SinglyLinkedListNode(data)
            new_node.next = node.next
            node.next = new_node
            break
        count += 1
        node = node.next

    return head




def main():
    contents = [16, 13, 7]  # 0, 1, 2
    contents = [1, 3, 4, 10]  #
    data = 1
    position = 2

    llist = SinglyLinkedList()
    for i in contents:
        llist.insert_node(i)

    result = llist.__repr__()
    print(result)

    new_list_head = insert_node_at_position(llist.head, data, position)

    result = llist.__repr__()
    print(result)


if __name__ == "__main__":
    main()
