function fill(grid, i, j) {
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[i].length || grid[i][j] != 0) {
        return 0;
    }
    return (grid[i][j] = 1) + fill(grid, i + 1, j) + fill(grid, i, j + 1)
        + fill(grid, i - 1, j) + fill(grid, i, j - 1);
}

function closedIsland(grid: number[][]): number {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (i * j * (i - grid.length + 1) * (j - grid[i].length + 1) == 0)
                fill(grid, i, j);
        }
    }
    let res = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            res += fill(grid, i, j) > 0 ? 1 : 0;
        }
    }

    return res;
}