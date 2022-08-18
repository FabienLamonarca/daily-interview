class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printlist(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverse_iteratively(self, head):
        curr = head
        prev = None
        while curr is not None:
            next_element = curr.next
            curr.next = prev
            prev = curr
            curr = next_element

    # Recursive Solution
    def reverse(self, curr):
        # If head is empty or has reached the list end
        if curr.next is None:
            return curr

        tail = curr.next
        # Reverse the rest list
        self.reverse(tail)

        # Put first element at the end
        curr.next.next = curr
        curr.next = None



# Test Program
node0 = ListNode(4)
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(0)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

print("Initial list: ")
node0.printlist()
# 4 3 2 1 0
# node0.reverse_iteratively(node0)
node0.reverse(node0)
print("List after reversal: ")
node4.printlist()
# 0 1 2 3 4
