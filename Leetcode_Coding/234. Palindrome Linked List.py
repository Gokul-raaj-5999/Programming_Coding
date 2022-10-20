# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def check(head):
            if head is None:
                return True
            res = check(head.next) and (self.temp.val == head.val)
            self.temp = self.temp.next
            return res
            
            
        self.temp = head
        return check(head)

"""
234. Palindrome Linked List
Easy

12101

671

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""
