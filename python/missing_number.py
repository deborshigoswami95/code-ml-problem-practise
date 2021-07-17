"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

def solution_naive(nums: List[int]) -> int:
  """
  This is an inefficient solution
  """
  length = len(nums)
  all_nums = [i for i in range(length+1)]
  for i in nums:
      all_nums.remove(i)
  return all_nums[0]
