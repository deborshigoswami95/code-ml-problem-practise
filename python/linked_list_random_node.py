from random import randint

class Solution:
    # The solution is basically a modified Fischer Yates Algorithm 
    # If the length of the list was unknown, how would we choose random list?
    # assuming the list is being streamed, we basically apply "Reservoir Sampling" which is the big data generalization of Fischer Yates
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.length = 0
        node = head
        while node!=None:
            node = node.next
            self.length+=1
    
    def getChoice(self, k):
        if randint(1,k)==1:
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        random_node=self.head
        current_proba_denominator=self.length
        while current_proba_denominator>=0:
            if self.getChoice(current_proba_denominator):
                return random_node.val
            else:
                current_proba_denominator-=1
                random_node=random_node.next
        return None
