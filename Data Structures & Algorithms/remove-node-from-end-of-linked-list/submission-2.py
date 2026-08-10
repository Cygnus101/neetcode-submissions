# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        arr = []
        while ptr is not None:
            arr.append(ptr.val)
            ptr = ptr.next

        new_head = ListNode()
        new_ptr = new_head
        for i in range(0,len(arr)):
            if i == (len(arr) - n):
                del(arr[i])
        print(arr)
        for a in arr:
            new_ptr.next = ListNode(a)
            new_ptr = new_ptr.next

        return new_head.next
