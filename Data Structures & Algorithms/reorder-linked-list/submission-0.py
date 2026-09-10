# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse list of second half
        second = slow.next
        slow.next = None

        prev = None

        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the lists
        dummy = ListNode()

        curr = dummy

        while prev:
            curr.next = head
            head = head.next
            curr = curr.next

            curr.next = prev
            prev = prev.next
            curr = curr.next
                
        curr.next = head


        
