class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # move fast n steps
        for _ in range(n):
            fast = fast.next

        # move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove node
        slow.next = slow.next.next

        return dummy.next