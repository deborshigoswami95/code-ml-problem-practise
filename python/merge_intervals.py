class naive_solution:
  def get_overlap(self, a: List[int], b: List[int]):
    if a[0]<=b[0] & b[0]<=a[1]:
      return [a[0], max(a[1],b[1])]
    else:
      return None
  
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals)
    length = len(intervals)

    if length==1:
      return intervals

    for i in range(length-1):
      for j in range(i+1,length):
        merged_interval = self.get_overlap(intervals[i],intervals[j])
        if merged_interval!=None:
          intervals.append(merged_interval)
          intervals.pop(i)
          intervals.pop(j-1)
          return self.merge(intervals)

    return intervals
