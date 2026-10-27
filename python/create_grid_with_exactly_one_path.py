# ======================================
# LeetCode Problem: create grid with exactly one path
# Language: python
# Link: https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Synced by: LinkCode
# Date: 10/27/2026, 1:34:02 PM
# ======================================


class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        return ['.'*n] + ["#" * (n-1) + "."]*(m-1)

        