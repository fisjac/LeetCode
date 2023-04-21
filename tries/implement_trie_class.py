class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            i = ord(char) - ord("a")
            if current.children[i] == None:
                current.children[i] = Node()

            current = current.children[i]
        current.endOfWord = True


    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            i = ord(char) - ord("a")
            if current.children[i] == None:
                return False
            current = current.children[i]

        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            i = ord(char) - ord("a")
            if current.children[i] == None:
                return False
            current = current.children[i]

        return True

class Node:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
