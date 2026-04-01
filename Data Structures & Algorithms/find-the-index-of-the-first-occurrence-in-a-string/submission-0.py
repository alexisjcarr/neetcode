class Solution:
    """
    The brute force approach wastes work by restarting from scratch after each mismatch. 
    KMP improves this by preprocessing the needle to build a "longest proper prefix which is also suffix" (LPS) array. 
    When a mismatch occurs, the LPS array tells us how many characters we can skip, leveraging the pattern structure to avoid redundant comparisons.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        # build LPS
        if needle == "":
            return 0

        lps = [0] * len(needle)

        prevLPS, i = 0, 1

        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1

            elif prevLPS == 0:
                lps[i] = 0
                i += 1

            else:
                prevLPS = lps[prevLPS - 1]

        # KMP
        i, j = 0, 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

            if j == len(needle):
                return i - len(needle)

        return -1
      