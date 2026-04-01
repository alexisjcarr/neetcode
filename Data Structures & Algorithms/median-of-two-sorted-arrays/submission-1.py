class Solution:
    """
    We want the median of two sorted arrays without fully merging them.

    Think of placing the two arrays side by side and making a cut (partition) so that:
        - The left side of the cut contains exactly half of the total elements (or half + 1 if odd).
        - All elements on the left side are <= all elements on the right side.

    If we can find such a partition, then:
        - The median must come from the border elements around this cut:
            - The largest element on the left side,
            - And the smallest element on the right side.

    To find this cut efficiently, we:
        - Only binary search on the smaller array.
        - For a chosen cut in the smaller array, the cut in the larger array is fixed (so total elements on the left is half).
        - Check if this partition is valid:
                Aleft <= Bright and Bleft <= Aright
        - If not valid:
            - Move the cut left or right (like normal binary search) until it becomes valid.
    Once we have a valid partition, we compute the median using the max of left side and min of right side.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        left, right = 0, len(a) - 1

        while True:
            i = (left + right) // 2  # a
            j = half - i - 2  # b

            a_left = a[i] if i >= 0 else float("-inf")
            a_right = a[i + 1] if (i + 1) < len(a) else float("inf") 
            b_left = b[j] if j >= 0 else float("-inf")
            b_right = b[j + 1] if (j + 1) < len(b) else float("inf")

            # partition is correct
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)

                # even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                right = i - 1

            else:
                left = i + 1