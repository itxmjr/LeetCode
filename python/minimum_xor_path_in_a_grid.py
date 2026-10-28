# ======================================
# LeetCode Problem: minimum xor path in a grid
# Language: python
# Link: https://leetcode.com/problems/minimum-xor-path-in-a-grid/
# Synced by: LinkCode
# Date: 10/29/2026, 1:04:58 AM
# ======================================


class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[set() for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j == 0:
                    dp[0][0].add(grid[0][0])
                    continue

                if i > 0:
                    for v in dp[i-1][j]:
                        dp[i][j].add(v ^ grid[i][j])
                if j > 0:
                    for v in dp[i][j-1]:
                        dp[i][j].add(v ^ grid[i][j])

        return min(dp[ROWS-1][COLS-1])  
        