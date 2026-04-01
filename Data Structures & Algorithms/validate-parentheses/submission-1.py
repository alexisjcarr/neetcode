class Solution:
    """
    Explore:
            ([{}])
    stack = ["([{"]

    Plan:
     - map of close-to-open
     - stack = []

     - for paren in string:
        - if p in opens: add to stack
        - if p in closes: 
            - if stack, pop off stack and compare map[p] to stack.pop():
                - if not equal, return False
    return not len(stack)
    """
    def isValid(self, s: str) -> bool:
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for p in s:
            if p in map.values():
                stack.append(p)

            else:
                if not stack or map[p] != stack.pop():
                    return False

        return not len(stack)
