class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Compare characters
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
            else:
                # This runs if we never hit 'break'
                # (i.e., one word is a prefix of the other)
                if len(w1) > len(w2):
                    return False

        return True
        