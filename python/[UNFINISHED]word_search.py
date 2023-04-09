# https://leetcode.com/problems/word-search/

from typing import List,Tuple,Union
from time import time

class Solution:
    def traverse_next(self,prev_pos:Tuple[int],curr_pos:Tuple[int],next_letter:str)->Union[bool,Tuple[int]]:
        if curr_pos[0]-1 >= self.x_lim[0] and prev_pos != (curr_pos[0]-1,curr_pos[1]) and self.board[curr_pos[0]-1][curr_pos[1]]==next_letter:
            return True
        elif curr_pos[0]+1 < self.x_lim[1] and prev_pos != (curr_pos[0]+1,curr_pos[1]) and self.board[curr_pos[0]+1][curr_pos[1]]==next_letter:
            return True
        elif curr_pos[1]-1 >= self.y_lim[0] and prev_pos != (curr_pos[0],curr_pos[1]-1) and self.board[curr_pos[0]][curr_pos[1]-1]==next_letter:
            return True
        elif curr_pos[1]+1 < self.y_lim[1] and prev_pos != (curr_pos[0],curr_pos[1]+1) and self.board[curr_pos[0]][curr_pos[1]+1]==next_letter:
            return True
        else:
            return False
        
    def check_word_existence(self,prev_pos:Tuple[int],curr_pos:Tuple[int],word)->bool:
        if not len(word):
            return True
        next_letter=word[0]
        


        return 



    def exist(self,board:List[List[str]], word:str)->bool:
        self.x_lim=(0,len(board))
        self.y_lim=(0,len(board[0]))
        self.board=board

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.board[i][j]==word[0]:
                    print((i,j))
                    found_word=self.check_word_existence((i,j),word)
                    if found_word==True:
                        return True

        return False
    

if __name__=="__main__":
    test_cases=[
        {
            'board':[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
            'word':'ABCCED'
        },
        {
            'board':[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
            'word':'SEE'
        }
    ]


    for test in test_cases:
        start=time()
        print('\n\n')
        print('solution: {}'.format(Solution().exist(test['board'],test['word'])))
        print('time to solve: {}'.format(time()-start))
        print('\n\n')
