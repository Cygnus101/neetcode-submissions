# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.val == val:
            head = ptr.next 
            ptr = head
        if ptr is None:
            return None
        prev = head
        ptr = ptr.next
        while ptr:
            if ptr.val == val:
                prev.next = ptr.next
                ptr = ptr.next
            else:
                ptr = ptr.next
                prev = prev.next
        return head
