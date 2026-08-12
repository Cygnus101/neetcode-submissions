# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mega = []
        for list_i in lists:
            node = list_i
            while node:
                mega.append(node.val)
                node = node.next
        mega = sorted(mega)
        head = ListNode()
        ptr = head
        for a in mega:
            a_n = ListNode(a)
            ptr.next = a_n
            ptr = ptr.next
        return head.next