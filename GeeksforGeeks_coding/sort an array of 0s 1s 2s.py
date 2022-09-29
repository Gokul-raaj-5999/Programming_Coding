#User function Template for python3

class Solution:
    def sort012(self,a,n):
        # code here
        while mid <= hi:
        # If the element is 0
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            # If the element is 1
            elif a[mid] == 1:
                mid = mid + 1
            # If the element is 2
            else:
                a[mid], a[hi] = a[hi], a[mid]
                hi = hi - 1
            return a
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends

"""
Sort an array of 0s, 1s and 2s
EasyAccuracy: 51.36%Submissions: 100k+Points: 2
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.  

Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2"""