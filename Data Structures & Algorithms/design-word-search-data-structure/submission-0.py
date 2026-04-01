class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        # Iterative backtracking using a stack (no recursion)
        stack = [(self.root, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == len(word):
                if node.is_word:
                    return True
                continue

            ch = word[idx]
            if ch == '.':
                # Explore all possible continuations for this position
                for child in node.children.values():
                    stack.append((child, idx + 1))
            else:
                if ch in node.children:
                    stack.append((node.children[ch], idx + 1))
                # else: this path is dead; do nothing

        return False
        
