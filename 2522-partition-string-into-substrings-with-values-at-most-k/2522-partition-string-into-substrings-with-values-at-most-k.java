class Solution {
    public int minimumPartition(String s, int k) {
        int ans = 1;
        long cur = 0;
        for (int i = 0; i < s.length(); i++) {
            int digit = s.charAt(i) - '0';
            long tmp = cur * 10 + (long) digit;
            if (tmp <= (long) k) {
                cur = tmp;
            } else {
                if (digit > k) {
                    return -1;
                }
                ans++;
                cur = (long) digit;
            }
        }
        return ans;

    }
}