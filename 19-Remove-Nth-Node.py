# Definition of singly-linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fast = slow = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        else:
            slow.next = slow.next.next

        return head
