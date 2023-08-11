class Node:
    def __init__(self, val):
        self.map = {}
        self.val = val
        self.terminal = False

class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            node.map[letter] = node.map.get(letter, Node(letter))
            node = node.map[letter]
        
        node.terminal = True

    def search(self, word: str) -> bool:
        node = self.root

        for letter in word:
            try:
                node = node.map[letter]
            except:
                return False
        
        if node.terminal:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root

        for letter in prefix:
            try:
                node = node.map[letter]
            except:
                return False
        return True
