class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        Map<String, Integer> countS = new HashMap<>();
        Map<String, Integer> countT = new HashMap<>();
        
        for(int i = 0; i < s.length(); i++) {
            String sChar = Character.toString(s.charAt(i));
            if (countS.containsKey(sChar)) {
                countS.put(sChar, countS.get(sChar) + 1);
            } else {
                countS.put(sChar, 1);
            }
            
            String tChar = Character.toString(t.charAt(i));
            if (countT.containsKey(tChar)) {
                countT.put(tChar, countT.get(tChar) + 1);
            } else {
                countT.put(tChar, 1);
            }
        }
        
        for(int i = 0; i < s.length(); i++) {
            String sChar = Character.toString(s.charAt(i));
            if (!countS.get(sChar).equals(countT.get(sChar))) {
                return false;
            }
        }
        return true;  
    }
}