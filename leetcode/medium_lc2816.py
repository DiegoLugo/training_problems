# 2816. Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        number_str = ""
        while curr is not None:
            number_str += str(curr.val)
            curr = curr.next
        number = int(number_str) * 2
        number_str = str(number)
        head = ListNode()
        curr_node = ListNode()
        for idx, digit in enumerate(number_str):
            if idx == 0:
                head = ListNode(int(digit), None)
                curr_node = head
            else:
                curr_node.next = ListNode(int(digit), None)
                curr_node = curr_node.next
        return head