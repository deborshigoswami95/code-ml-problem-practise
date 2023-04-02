# https://leetcode.com/problems/longest-palindromic-substring/description/

from typing import Union, Optional, List
from time import time

class baselineSolution:
    def longestPalindrome(self,s:str)->str:
        if len(s)<=1:
            return s
        i,j=0,0
        max_palindrome=s[0]
        while i < len(s) and j < len(s):
            k=0
            while j+1 < len(s) and s[j+1]==s[i]:
                j+=1

            while i-k>=0 and j+k<len(s) and s[i-k]==s[j+k]:
                if len(max_palindrome)<(j-i+1+2*k):
                    max_palindrome=s[i-k:j+k+1]
                k+=1
            i+=1
            j=i
        return max_palindrome
    

if __name__=='__main__':
    test_cases = [
        'asdcnjk',
        '',
        'a',
        'aa',
        'aaa',
        'baab',
        'bananas',
        'sdnbnviodhjbaabjdicjnd',
        'jsbqttcttqjsdc',
        'babjjhhbbbadab'
    ]

    solutions={
        'baseline solution':baselineSolution
    }

    for test in test_cases:
        for solution in solutions:
            sol=solutions[solution]()
            print('test --> {}'.format(test))
            print('solution  --> {}'.format(solution))
            start=time()
            print('result --> {}'.format(sol.longestPalindrome(test)))
            print('solution time --> {}'.format(time()-start))
            print('\n\n')
