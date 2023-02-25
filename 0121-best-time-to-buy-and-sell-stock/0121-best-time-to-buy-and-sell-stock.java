class Solution {
  public int maxProfit(int[] prices) {
    int l = 0;
    int r = 1;
    int profit = 0;
    while (r < prices.length) {
      if (prices[r] > prices[l]) {
        int cur = prices[r] - prices[l];
        profit = Math.max(cur, profit);
      } else {
        l = r;
      }
      r += 1;
    }
    return profit;
  }
}