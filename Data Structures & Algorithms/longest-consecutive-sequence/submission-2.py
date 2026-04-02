class Solution:
    """
    BOX 1:
    find longest consecutive sequence (they don't need to be consecutive in the original array)

    examples:
       [2,20,4,10,3,4,5] => [2, 3, 4, 5] notice the earlier 4... in the future ask about this...
    
    brainstorm:
     - can create a set of vals and iterate over array
     max_len = 0
     for nums in nums: [2, ]
        len = 1
        check if num - 1 in set:
            while num + len in set;
                len += 1
            max_len = max(len, max_len)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len, num_set = 0, set(nums)

        for num in nums:
            len_ = 1
            if (num - 1) not in num_set:
                while (num + len_) in num_set:
                    len_ += 1
                max_len = max(max_len, len_)

        return max_len
      