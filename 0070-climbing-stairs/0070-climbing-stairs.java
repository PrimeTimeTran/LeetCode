class Solution {
    public int climbStairs(int n) {
        int f0 = 1, f1 = 1; 
        for (int i = 1; i <= n-1; ++i) {
            int ff = f0; 
            f0 = f1; 
            f1 = ff + f1; 
        }
        return f1; 
    }
}