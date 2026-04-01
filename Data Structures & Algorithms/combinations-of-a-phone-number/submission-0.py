class Solution:
    """
                        [3, 4]

                        iterate over nums

                        
                 [d, e, f] [g, h, i]
                d       e           f choose first letter
            dg dh di  eg eh ei   fg fh fi choose second letter
    """
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res, t9word = [], []

        def backtrack(i):
            nonlocal res, t9word

            if len(t9word) == len(digits):
                res.append("".join(t9word))
                return

            # choose
            for lt in digits_map[digits[i]]:
                t9word.append(lt)

                # explore
                backtrack(i + 1)

                # unchoose
                t9word.pop()

        if digits:
            backtrack(0)

        return res

        