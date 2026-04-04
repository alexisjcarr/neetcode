class Solution:
    """
    BOX 1:
    Brainstorm:
        - At any mid, one half is fully sorted. Determine which, check if target falls there.
        - "One half is always sorted. Check which. If target in sorted half, search there; else search the other."

        [3,4,5,6,1,2], target = 1
        l    m      r

    Plan:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1       
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        