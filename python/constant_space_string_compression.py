# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        
        current_pos = 1
        #group_end_pos = -1
        group_size = 1
        previous_char = chars[0]
        chars.append('END')
        
        while current_pos < len(chars[1:]):
            if chars[current_pos]==previous_char:
                group_size+=1
                current_pos+=1
            else:
                if group_size==1:
                    previous_char=chars[current_pos]
                    current_pos+=1
                else:
                    compressed_chars=list(previous_char+str(group_size))
                    for i in range(group_size):
                        chars.pop(current_pos-group_size)       
                    for i in reversed(compressed_chars):
                        chars.insert(current_pos-group_size, i)
                    
                    current_pos = current_pos-group_size+len(compressed_chars)
                    previous_char=chars[current_pos]
                    current_pos+=1
                    group_size=1
                    #print(chars)
                    
        if group_size==1:
            chars.pop(-1)
            #print(chars)
            return len(chars)
        else:
            compressed_chars=list(previous_char+str(group_size))
            for i in range(group_size):
                chars.pop(current_pos-group_size)       
            for i in reversed(compressed_chars):
                chars.insert(current_pos-group_size, i)
            chars.pop(-1)
            #print(chars)
            return len(chars)
