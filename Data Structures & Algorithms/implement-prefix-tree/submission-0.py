class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isEnd = True
    def search(self, word: str) -> bool:
        node=self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isEnd
    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True





