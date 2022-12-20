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
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> pq = new PriorityQueue<>((l1, l2) -> l1.val - l2.val);
        
        if (lists.length == 0)
            return null;
        
        for (int i = 0; i < lists.length; i++) {
            ListNode temp = lists[i];
            while (temp != null) {
                pq.add(temp);
                temp = temp.next;
            }
        }
        
        ListNode head = pq.poll();
        ListNode ref = head;
        
        while (!pq.isEmpty()) {
            ref.next = pq.poll();
            ref = ref.next;
        }
        if (ref != null)
            ref.next = null;
        
        return head;
    }
}