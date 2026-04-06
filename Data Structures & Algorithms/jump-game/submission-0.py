class Solution:
    """
    BOX 1:
    Brainstorming:
        - Track max reachable index. If current index > max reachable, you're stuck.
        - "Greedy: maintain max_reach. If i>max_reach, return False. Else update max_reach."

    Plan:
    reach=0
    for i,j in enumerate(nums):
        if i>reach: return False
        reach=max(reach,i+j)
    return True
    """
    def canJump(self, nums: List[int]) -> bool:
        reach = 0

        for idx, num in enumerate(nums):
            if idx > reach: 
                return False

            reach = max(reach, idx + num)

        return True
        