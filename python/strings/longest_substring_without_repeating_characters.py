# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
  
    def suboptimal_lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        max_len=1
        sub_dict={}
        k=0
        while k<len(s):
            if s[k] in sub_dict:
                max_len=max(max_len, len(sub_dict))
                k=sub_dict[s[k]]+1
                sub_dict={}
            else:
                sub_dict[s[k]]=k
                k+=1
        max_len=max(max_len, len(sub_dict))
        return max_len
