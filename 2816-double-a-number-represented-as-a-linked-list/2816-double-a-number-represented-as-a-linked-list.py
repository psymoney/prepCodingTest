# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        if head.val <= 4:
            prev = head
            prev.val *= 2
            head = head.next
        else:
            prev = ListNode(0)
            prev.next = head
        
        temp = prev
        if not head: return temp
        while True:
            v = head.val * 2
            if v >= 10:
                prev.val += 1
            head.val = v % 10
            if not head.next:
                break
            prev = head
            head = head.next
        
        return temp
            