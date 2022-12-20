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
    public void reorderList(ListNode head) {
        Stack<ListNode> stack = new Stack<>();

        ListNode ref1 = head; 
        ListNode ref2 = head;
        
        while (ref2.next != null) {
            ref1 = ref1.next;
            ref2 = ref2.next;
            if (ref2.next != null)
                ref2 = ref2.next;
        }
        
        while (ref1 != null) {
            stack.add(ref1);
            ref1 = ref1.next;
        }
        
        ListNode ref3 = head;
        while (!stack.isEmpty()) {
            ListNode temp = stack.pop();
            temp.next = ref3.next;
            ref3.next = temp;
            ref3 = temp.next;
        }
        ref3.next = null;
    }
}