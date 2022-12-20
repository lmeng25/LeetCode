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
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode ref = head;
        int size = 0;
        
        while (ref != null) {
            size++;
            ref = ref.next;
        }

        if (size == 1)
            return null;
        
        if (size == n) {
            head = head.next;            
            return head;
        }
        
        ListNode ref1 = head;
        for (int nth = 0; nth < size - n - 1; nth++)
            ref1 = ref1.next;
        
        ref1.next = ref1.next.next;
        
        return head;
    }
}