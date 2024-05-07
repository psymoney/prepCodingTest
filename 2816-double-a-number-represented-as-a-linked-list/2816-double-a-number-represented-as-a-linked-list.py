# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(20_000)
        temp = head
        number = ''
        
        while head:
            number += str(head.val)
            head = head.next
        
        number = str(int(number) * 2)
        head = temp

        for i, v in enumerate(number):        
            head.val = int(v)
            if i != len(number) - 1 and not head.next:
                print(i, v)
                head.next = ListNode()
            head = head.next
                
        return temp
        