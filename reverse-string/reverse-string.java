class Solution {
    public void reverseString(char[] s) {
        reverse(0, s.length - 1, s);
    }
    
    private void reverse(int left, int right, char[] s) {
        if (left >= right)
            return;
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
        
        reverse(left, right, s);
    }
}