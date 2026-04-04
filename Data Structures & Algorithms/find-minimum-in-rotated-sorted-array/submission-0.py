class Solution:
    """
    BOX 2:
    Brainstorming:
    - could just sort and return nums[0] => O(nlogn) | O(nlogn)
    - could iterate while keeping track of global min => O(n) | O(1)
    - binary search log(n) | O(1)

    [3,4,5,6,1,2]
     l   m     r

    Plan:
     
    """
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r)//2

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]

        