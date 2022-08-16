# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def to_int(self, power=0, acc=0):
        acc = acc + self.val * pow(10, power)
        if self.next:
            return self.next.to_int(power + 1, acc)
        return acc

    def adjust_power(self, power=0):
        lp = ListNode(self.val * pow(10, power))
        if self.next:
            lp.next = self.next.adjust_power(power + 1)
        return lp


def reverse(node):
    if node.next is None:
        return node
    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1


class Solution:
    @staticmethod
    def add_two_numbers(l1, l2):
        pass


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = Solution.add_two_numbers(l1, l2)

    while l3:
        print(l3.val)
        l3 = l3.next


if __name__ == '__main__':
    main()

# 7 0 8
