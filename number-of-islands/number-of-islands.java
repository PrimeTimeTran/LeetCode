class Solution {
    Set<String> seen;
    char[][] grid;
    public int numIslands(char[][] g) {
      grid = g;
      int count = 0;
      int m = grid.length, n = grid[0].length;
      seen = new HashSet<String>(); 
      
      for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
          if (dfs(r, c, grid)) count += 1;
        } 
      }
      return count;
    }

    public boolean dfs(int r, int c, char[][] grid) {
      boolean out = r < 0 || c < 0 || r == grid.length || c == grid[0].length;
      if (out) return false;
      if (Character.toString(grid[r][c]).equals("0")) return false;
      String coords = String.format("%s,%s", r, c);
      if (seen.contains(coords)) return false;
      seen.add(coords);
      
      dfs(r + 1, c, grid);
      dfs(r - 1, c, grid);
      dfs(r, c + 1, grid);
      dfs(r, c - 1, grid);
      
      return true;  
    }
}