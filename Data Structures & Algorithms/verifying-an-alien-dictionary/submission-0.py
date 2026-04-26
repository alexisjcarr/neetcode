class Solution:
    """
    explore:
        - given an alien alphabet, return if the words are sorted in lexicographical order

    brainstorm:
        - hash each char of the alphabet to its index, iterate through each word and create a list
        of the mappings. Return if they are in order

    plan:
        - alphabet, maps = {}, []
        - for idx, char in enumerate(order):
            - alphabet[char] = idx

        - for idx, word in enumerate(words):
            - for char in word:
                - maps[idx].append(alphabet[char])
    
        return sorted(maps) == maps
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet, maps = {}, [[] for _ in words]

        for idx, char in enumerate(order):
            alphabet[char] = idx

        for idx, word in enumerate(words):
            for char in word:
                maps[idx].append(alphabet[char])

        for i in range(len(maps) - 1):
            if maps[i] > maps[i + 1]:
                return False
    
        return True
