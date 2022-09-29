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
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        Map<Integer, Integer> map = new HashMap<>();
        ListNode ref = head;
        
        while (ref != null) {
            map.put(ref.val, map.getOrDefault(ref.val, 0) + 1);
            ref = ref.next;
        }
        
        while (head != null && map.get(head.val) > 1)
            head = head.next;
        
        if (head == null)
            return null;
        
        ListNode prev = head;
        ListNode curr = head.next;
        while (curr != null) {
            if (map.get(curr.val) > 1) {
                prev.next = curr.next;
                curr = curr.next;
            }
            else {
                prev = curr;
                curr = curr.next;
            }
        }
        
        return head;
    }
}