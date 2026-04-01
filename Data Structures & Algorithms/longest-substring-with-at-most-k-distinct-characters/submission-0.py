class Solution:
    """
    An optimization on the standard sliding window: instead of shrinking the window with a while loop, we only shrink by one step when invalid. 
    This keeps the window size from ever decreasing by more than one, which means we only need to track when the window grows. 
    The final answer is the maximum window size achieved, which equals n - left at the end.
    """
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_size = 0
        counter = collections.Counter()

        for right in range(len(s)):
            counter[s[right]] += 1

            if len(counter) <= k:
                max_size += 1

            else:
                counter[s[right - max_size]] -= 1

                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]

        return max_size
        