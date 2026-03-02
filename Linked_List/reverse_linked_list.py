class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next      # 1) store next
            curr.next = prev           # 2) reverse link
            prev = curr                # 3) move prev
            curr = next_node           # 4) move curr

        return prev