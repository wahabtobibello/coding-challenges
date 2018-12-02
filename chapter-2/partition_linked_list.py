from linked_list import generate_linked_list, print_linked_list


def partition_linked_list(head, partition):
    new_head = head

    node = head
    next_node = node.next

    while next_node != None:
        if node.data >= partition and next_node.data < partition:
            node.next = next_node.next
            next_node.next = new_head
            new_head = next_node
            next_node = node.next
        else:
            node = next_node
            next_node = node.next
    return new_head


arr = [3, 5, 8, 5, 10, 2, 1]
head = generate_linked_list(arr)
print_linked_list(head)
new_head = partition_linked_list(head, 5)
print_linked_list(new_head)
