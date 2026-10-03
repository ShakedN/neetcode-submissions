# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # מקדמים את fast ב-n צעדים
        for _ in range(n):
            fast = fast.next

        # מקדמים את שניהם עד ש-fast בצומת האחרון
        while fast.next:
            slow = slow.next
            fast = fast.next

        # מדלגים על הצומת שצריך למחוק
        slow.next = slow.next.next
        return dummy.next