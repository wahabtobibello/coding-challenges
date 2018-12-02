from linked_list import LinkedList, print_linked_list


def partition_linked_list(linked_list, partition):
    new_head = linked_list.head

    node = new_head
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
    
    linked_list.head = new_head


arr = [3, 5, 8, 5, 10, 2, 1]
linked_list = LinkedList(arr)
print_linked_list(linked_list)
partition_linked_list(linked_list, 5)
print_linked_list(linked_list)
