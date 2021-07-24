# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class naive_Solution:
    def get_single_occurence_words(self, s):
        word_count=dict()
        for i in s:
            if i in word_count.keys():
                word_count[i]+=1
            else:
                word_count[i]=1
        return set([k for k, v in word_count.items() if v==1])
        
    
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        
        all_common_words = set(s1).intersection(set(s2))
        
        s1 = self.get_single_occurence_words(s1)
        s2 = self.get_single_occurence_words(s2)
        
        
        return list(((s1-s2).union(s2-s1)) - all_common_words
