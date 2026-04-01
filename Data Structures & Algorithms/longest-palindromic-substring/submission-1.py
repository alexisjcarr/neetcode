class Solution:
    """
    A palindrome expands symmetrically from its center.

    Every palindrome has one of two centers:

        - Odd length → a single character center (e.g. "racecar")
        - Even length → between two characters (e.g. "abba")

    So instead of checking all substrings, we:

        - Treat every index as a possible center
        - Expand left and right while characters match
        - Track the longest palindrome found during expansion
        
    This avoids extra space and redundant checks.
    """
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for idx in range(len(s)):
            # odd length
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                left -= 1
                right += 1

            # even length
            left, right = idx, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                left -= 1
                right += 1

        return res

        