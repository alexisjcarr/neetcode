"""
Explore:
 - return groups of anagrams from a word list

Brainstorm:
 - can make counters of each word and map to indexes
 {idx: Counter(word)}

Approach:
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())
        