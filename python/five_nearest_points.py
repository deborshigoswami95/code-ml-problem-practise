"""
  Implement a class that accepts a set of points and K: number of results to return
  & returns the K closest points to origin (0,0)
  
  To create an optimized solution, implement the HEAP data structure to speed up the query
"""

import heapq as hp

class KShortestPoints:
    def __init__(self, k):
        self.points = []
        self.k = k

    def inputPoint(self, p):
        distance = p[0]**2 + p[1]**2    
        hp.heappush(self.points, (-distance, p))
        if len(self.points)>k:
            hp.heappop(self.points)

    def findClosestK(self):
        if not len(self.points):
            return None
        else:
            solution=[]
            for i in self.points:
                solution.append(i[1])
            return solution
