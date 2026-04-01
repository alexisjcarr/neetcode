class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        root = self

        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.is_word = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs:
            return ""
        trie = TrieNode()

        # build trie
        for s in strs:
            trie.add_word(s)
        
        # interrogate trie
        curr, prefix = trie, []

        while len(curr.children) == 1 and not curr.is_word:
            char = next(iter(curr.children))
            prefix.append(char)
            curr = curr.children[char]

        return "".join(prefix)