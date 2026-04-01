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

        for paren in s:
            if paren in map.values():
                stack.append(paren)

            else:
                if not stack or map[paren] != stack.pop():
                    return False

        return not stack
