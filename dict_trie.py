class Trie():
        def __init__(self, words):
                self.root = TrieNode(None, "")
                for word in words:
                        self.insertWord(word)

        def insertWord(self, word):
                currNode = self.root
                for letter in word:
                        if letter in currNode.children:
                                currNode = currNode.children[letter]
                        else:
                                newNode = TrieNode(currNode, letter)
                                currNode.children[letter] = newNode
                                currNode = newNode
                currNode.words.append(word)
                
        def containsPrefix(self, word):
                currNode = self.root
                for letter in word:
                        if not letter in currNode.children:
                                return False
                        else:
                                currNode = currNode.children[letter]
                return True

        def containsWord(self, word):
                currNode = self.root
                for letter in word:
                        if not letter in currNode.children:
                                return False
                        else:
                                currNode = currNode.children[letter]
                return word in currNode.words

class TrieNode():
        def __init__(self, parent, letter):
                self.children = {}
                self.words = []
                self.parent = parent
                self.letter = letter

class Dictionary():
    def __init__(self, filepath):
        valid_words = None
        with open(filepath) as dictionary:
            valid_words = set(word.strip().lower() for word in dictionary if len(word.strip()) > 0)
        self.valid_words = Trie(valid_words)

    def containsPrefix(self, word):
        return self.valid_words.containsPrefix(word)

    def contains(self, word):
        return self.valid_words.containsWord(word)


dict_filepath = 'dictionary.txt'
dictionary = Dictionary(dict_filepath)
