class Solution:
    """
    BOX 3:
    Plan:
    - create set of nums
    - iterate through nums array:
        if not (nums - 1):
            len_ = 1
            while (nums + len_) in set:
                len_ += 1
            max_len = max(max_len, len)

    return max_len
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set, max_length = set(nums), 0

        for num in nums:
            if (num - 1) not in num_set:
                length = 1

                while (num + length) in num_set:
                    length += 1

                max_length = max(max_length, length)

        return max_length