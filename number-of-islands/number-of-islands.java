class Solution {
    public int numIslands(char[][] grid) {
      int count = 0;
      int m = grid.length;
      int n = grid[0].length;
      Set<String> seen = new HashSet<String>(); 
      
      for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
          if (dfs(r, c, seen, grid)) {
            count += 1;
          }
        } 
      }
      
      return count;
    }

    public boolean dfs(int r, int c, Set<String> seen, char[][] grid) {
      boolean out = r < 0 || c < 0 || r == grid.length || c == grid[0].length;
      if (out) return false;
      if (Character.toString(grid[r][c]).equals("0")) return false;
      String coords = String.format("%s,%s", r, c);
      if (seen.contains(coords)) return false;
      seen.add(coords);
      
      dfs(r + 1, c, seen, grid);
      dfs(r - 1, c, seen, grid);
      dfs(r, c + 1, seen, grid);
      dfs(r, c - 1, seen, grid);
      
      return true;  
    }
}