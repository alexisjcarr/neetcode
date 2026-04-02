class Solution:
    """
    BOX 2
    """
    def characterReplacement(self, s: str, k: int) -> int:
        left, count_window = 0, collections.defaultdict(int)
        max_freq, max_length = 0, 0

        for right in range(len(s)):
            count_window[s[right]] += 1
            max_freq = max(max_freq, count_window[s[right]])

            while (right - left + 1) - max_freq > k:
                count_window[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
        