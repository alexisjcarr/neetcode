class Solution:
    """
    BOX 1:
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, count_window = 0, defaultdict(int)
        s1_count = Counter(s1)

        for right in range(len(s2)):
            count_window[s2[right]] += 1

            if (right - left + 1) > len(s1):
                count_window[s2[left]] -= 1

                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left += 1

            if count_window == s1_count:
                return True

        return False
       