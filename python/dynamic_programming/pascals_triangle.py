# https://leetcode.com/problems/pascals-triangle/description/

"""
This may look simple (cause it is) but it is a dynamic programming problem.

Why?

Because on the way to the Nth row, we are storing the computations for all N-1th rows

The Nth row only relies on tha values of the previous row.

The way this may be turned into a trickier DP problem is by saying,
Give me the pascal's triangle row for the 5th element of 100th row and 70th element of 101st row. 
Then the beginner might besat computing the result for each input even though we need 
to build up to the 100th row anyway
"""

from typing import List

class Solution(object):
    def generate(self,numRows: int) -> List[List[int]]:
        triangle=[[1]]
        if numRows==1:
            return triangle
        for i in range(1,numRows):
            tmp=[0]+triangle[i-1]+[0]
            row=[]
            for j in range(i+1):
                row.append(tmp[j]+tmp[j+1])
            triangle.append(row)
        return triangle

# TO DO: Fix this solution
if __name__=='__main__':
    sol=Solution()
    print(sol.generate(5))
    

