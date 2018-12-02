class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def append_to_tail(self, data):
        end = Node(data)
        node = self
        while node.next != None:
            node = node.next
        node.next = end


def generate_linked_list(arr):
    head = Node(arr[0])

    node = head
    for i in range(1, len(arr)):
        end = Node(arr[i])
        node.next = end
        node = end

    return head


def print_linked_list(head):
    node = head
    output = [str(node.data)]
    while node.next != None:
        output.append(str(node.next.data))
        node = node.next
    print('->'.join(output))
