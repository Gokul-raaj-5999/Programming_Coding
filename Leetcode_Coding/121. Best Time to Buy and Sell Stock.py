class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for i in range(0, len(arr)):
            if arr[i] < minprice:
                minprice = arr[i]
            elif arr[i] - minprice > profit:
                profit = arr[i] - minprice
        return profit
    
    
#-------------------another solution------------------
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
        
"""
Runtime: 1143 ms, faster than 86.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 24.9 MB, less than 85.25% of Python3 online submissions for Best Time to Buy and Sell Stock.

121. Best Time to Buy and Sell Stock
Easy

18229

584

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
Accepted
2,431,289
Submissions
4,473,702
"""
