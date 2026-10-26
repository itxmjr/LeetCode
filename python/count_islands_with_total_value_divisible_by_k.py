# ======================================
# LeetCode Problem: count islands with total value divisible by k
# Language: python
# Link: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
# Synced by: LinkCode
# Date: 10/26/2026, 10:18:37 AM
# ======================================


class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c]==0:
                return 0
            total = grid[r][c]
            grid[r][c] = 0
            return total + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]>0 and dfs(r, c)%k == 0:
                        res+=1
        return res