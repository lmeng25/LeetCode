class MyCalendar {

    private ArrayList<int[]> list;
    
    public MyCalendar() {
        list = new ArrayList<>();    
    }
    
    public boolean book(int start, int end) {
        for (int[] n : list) {
            if (n[0] < end && n[1] > start)
                return false;
        }
        list.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */