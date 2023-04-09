# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution:
    def maxProfit(self,prices:List[int])-> int:
        min_price=float('inf')
        max_profit_list=[]
        max_profit=0

        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            if prices[i]-min_price>max_profit:
                max_profit=prices[i]-min_price
            else:
                max_profit_list.append(max_profit)
                min_price=prices[i]
                max_profit=0

        return sum(max_profit_list) + max_profit
            