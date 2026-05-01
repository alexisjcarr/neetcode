from functools import lru_cache


class Solution:
    """
    explore
        - you can either take 1 step or 2...
        
    brainstorm
        1 1 1 
         V
         2

         1 1 1 1 1 
          V
          2
            
    """
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
