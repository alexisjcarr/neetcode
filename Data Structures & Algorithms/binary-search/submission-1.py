class Solution:
    """
    Explore:
     - search for target:
        - if exists, return idx
        - else return -1

    Brainstorm:
     - binary search

    Plan:
     - l, r = 0, len(nums) - 1

     - while l < r:
      - calc mid
      - if target == nums[mid]: return mid
      - elif target > nums[mid]: l = mid + 1
      - else: r = mid - 1
    - return -1
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

        return -1
        