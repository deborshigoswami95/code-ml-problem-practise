# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def get_carry(self, num):
        return num//10, num%10
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode()
        carry = 0
        solution = s
        
        while l1!=None or l2!=None:
            if l1==None:
                s.val+=l2.val
                l1=ListNode()
            elif l2==None:
                s.val+=l1.val
                l2=ListNode()
            else:
                s.val+=l1.val+l2.val
                
            carry, s.val = self.get_carry(s.val)
 
            if l1.next==None and l2.next==None and carry==0:
                    break
                
            s.next=ListNode()
            s.next.val=carry
            s=s.next
            l1=l1.next
            l2=l2.next
        
        return solution
