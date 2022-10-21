# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next
            
            result.next = ListNode(excess%10)
            result = result.next
            excess = excess//10
            
        return root.next   
    
#   """ add ele in order but not passing"""    
#         if l1 is None and l2 is None:
#             return None
#         h1 = l1
#         h2 = l2
#         l1 = h1
#         l2 = h2
#         rem = 0
#         while l1 is not None and l2 is not None:
#             a, b = l1.val, l2.val
#             if rem:
#                 l1.val = (l1.val+l2.val)%10 + rem
#             else:
#                 l1.val = (l1.val+l2.val)%10 
#             rem = (a+b)//10
#             # print(tem.val)
#             pre1 = l1
#             pre2 = l2
#             l1 = l1.next
#             l2 = l2.next
        
#         if l1 is not None and l2 is None:
#             while l1 is not None and l2 is None :
#                 a = l1.val
#                 if rem:
#                     l1.val = (l1.val + rem)%10
#                 rem = (a + rem)//10
#                 # print(rem)
#                 pre1 = l1
#                 l1 = l1.next

#             if rem:
#                 tem = ListNode()
#                 tem.val = rem
#                 # print(tem.val)
#                 pre1.next = tem
#             return h1
#         else:
#             l1 = pre1
#             while l2 is not None:
#                 a = l2.val
#                 tem = ListNode()
#                 if rem:
#                     tem.val = (l2.val + rem)%10
#                 rem = (a + rem)//10
#                 print(rem, l2.val)
#                 l1.next = tem
#                 pre1 = l1
#                 l1 = l1.next
#                 l2 = l2.next

#             if rem:
#                 tem = ListNode()
#                 tem.val = rem
#                 # print(tem.val)
#                 l1.next = tem
            
#             return h1
#         return h1
            

"""
2. Add Two Numbers
Medium

22269

4331

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
Accepted
3,192,454
Submissions
8,043,273
"""
