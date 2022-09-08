public class Codec {

    private LinkedList<String> list = new LinkedList<>();
    
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        String res = "";
        for (String s : strs) {
            list.add(s);
            res += s;
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        while (!list.isEmpty())
            res.add(list.pop());
        
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));