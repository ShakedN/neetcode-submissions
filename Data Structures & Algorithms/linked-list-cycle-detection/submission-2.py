# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        nexti=head
        while nexti and nexti.next:
            curr=curr.next
            nexti=nexti.next.next  
            if nexti==curr:
                return True
        return False