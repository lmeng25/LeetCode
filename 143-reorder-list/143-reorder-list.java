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
        // Queue<ListNode> queue = new Queue<>();
        
        ListNode ref = head;
        ListNode ref2 = head;
        
        while (ref != null) {
            stack.add(new ListNode(ref.val));
            ref = ref.next;
        }
        
        int counter = stack.size() / 2;
        int size = stack.size();
        
        while (counter > 0) {
            ListNode ref3 = stack.pop();
            ref3.next = ref2.next;
            ref2.next = ref3;
            ref2 = ref3.next;
            counter--;
            
            if (counter == 0) {
                if (size % 2 == 0)
                    ref3.next = null;
                else
                    ref2.next = null;
            }
        }
    }
}