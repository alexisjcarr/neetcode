class Solution:
    """
    BOX 2:
        Invariant: Sliding window. Track max char frequency in window. Shrink when replacements needed > k.
        Window valid when (size - max_freq) ≤ k. max_freq never decreases — only care if window can grow.

    Plan:
        - sliding window
        - left, window = 0, defaultdict(int)
        - max_freq = 0
        - max_len

        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])
            while (right - left + 1) - max_freq >= k:
                left += 1
                window[s[left]] -= 1
            max_len = max(max_len, right - left + 1)

        return max_len
    """
    def characterReplacement(self, s: str, k: int) -> int:
        left, count = 0, collections.defaultdict(int)
        max_freq, max_len = 0, 0

        for right in range(len(s)):
            count[s[right]] += 1

            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len