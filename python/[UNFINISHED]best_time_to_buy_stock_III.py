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
                if len(max_profit_list)==2 and max_profit<max_profit_list[0]:
                    min_price=prices[i]
                    max_profit=0
                    continue
                elif len(max_profit_list)==2 and max_profit<max_profit_list[1]:
                    max_profit_list[0]=max_profit
                elif len(max_profit_list)==2 and max_profit>max_profit_list[1]:
                    max_profit_list[0]=max_profit_list[1]
                    max_profit_list[1]=max_profit
                else:
                    max_profit_list.append(max_profit)
                min_price=prices[i]
                max_profit=0

        if len(max_profit_list)==2 and max_profit<max_profit_list[0]:
            return sum(max_profit_list)
        elif len(max_profit_list)==2 and max_profit>max_profit_list[0]:
            return max_profit+max_profit_list[1]
        elif len(max_profit_list)<2:
            return sum(max_profit_list.append(max_profit))