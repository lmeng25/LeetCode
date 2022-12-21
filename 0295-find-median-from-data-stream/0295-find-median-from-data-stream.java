class MedianFinder {

    public MedianFinder() {
        list = new ArrayList<>();
        median = 0;
        size = 0;
    }
    
    public void addNum(int num) {
        int index = Collections.binarySearch(list, num);
        if (index < 0)
            index = -(index + 1);
        list.add(index, num);
        
        size++;
        
        if (size % 2 == 0)
            median = (list.get(size / 2) + list.get(size / 2 - 1)) * 0.5;
        else
            median = list.get(size / 2);
    }
    
    public double findMedian() {
        return median;
    }
    
    private ArrayList<Integer> list;
    private double median;
    private int size;
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */