class Solution:
    """
    BOX 1
    """
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_freq, window = collections.Counter(t), collections.defaultdict(int)
        l, min_len, min_ptrs = 0, float("inf"), [0, 0]
        have, need = 0, len(t_freq)

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in t_freq and window[char] == t_freq[char]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_ptrs = [l, r + 1]
                
                window[s[l]] -= 1

                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1

                l += 1


        left, right = min_ptrs

        return s[left:right]

