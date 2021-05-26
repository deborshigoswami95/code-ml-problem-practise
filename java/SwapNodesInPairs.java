// Problem: https://leetcode.com/problems/swap-nodes-in-pairs/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */




class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        if (head==null || head.next==null)
            return head;
        
        ListNode Node = new ListNode();
        Node = head;
        
        ListNode newHead = new ListNode();
        newHead = head.next;
        
        ListNode prevNode = new ListNode();
        
        
        while (Node != null) {
            if (Node.next==null){
                break;
            }
            if (prevNode.next!=null) {
                 prevNode.next = Node.next;
            } 
        
            ListNode tmpNode = new ListNode();
            tmpNode = Node.next;
            Node.next = tmpNode.next;
            tmpNode.next = Node;
            prevNode = Node;
            Node=Node.next;
        }
        
        return newHead;
    }
}
