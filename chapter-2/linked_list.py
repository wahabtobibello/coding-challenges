class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self, arr):
        self.head = Node(arr[0])

        node = self.head
        for i in range(1, len(arr)):
            end = Node(arr[i])
            node.next = end
            node = end

    def append_to_tail(self, data):
        end = Node(data)

        node = self.head
        while node.next != None:
            node = node.next
        node.next = end


def print_linked_list(linked_list):
    node = linked_list.head
    output = [str(node.data)]
    while node.next != None:
        output.append(str(node.next.data))
        node = node.next
    print('->'.join(output))
