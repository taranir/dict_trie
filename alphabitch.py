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

col_1_row_2 = [["CU", "A", "P", "IT", "M"],
            ["S", "RI", "R", "A", "E"],
            ["H", "E", "D", "E", "Y"],
           ["CH", "N", "OS", "IC", "R"],
           ["I", "EA", "L", "E", "S"]]

col_1_row_3 = [["G", "R", "N", "C", "IT"],
            ["P", "A", "OT", "K", "E"],
            ["IN", "L", "IT", "A", "S"],
           ["TH", "H", "E", "O", "S"],
           ["PO", "ST", "LO", "UT", "K"]]

col_2_row_1 = [["A", "DU", "F", "IC", "E"],
            ["C", "L", "CE", "E", "S"],
            ["IN", "L", "PI", "TI", "E"],
           ["E", "OF", "CA", "R", "T"],
           ["PO", "S", "IT", "R", "ON"]]

col_2_row_2 = [["K", "OP", "I", "LL", "S"],
            ["S", "R", "I", "LO", "S"],
            ["H", "OV", "U", "E", "G"],
           ["D", "H", "L", "N", "M"],
           ["M", "I", "A", "G", "S"]]

col_2_row_3 = [["ST", "VE", "O", "TO", "ES"],
            ["P", "N", "R", "I", "VE"],
            ["HO", "O", "L", "BO", "NE"],
           ["E", "U", "OR", "E", "S"],
           ["WO", "H", "RY", "D", "D"]]

col_2_row_4 = [["FO", "E", "T", "RAP", "R"],
            ["Y", "RN", "UB", "O", "TH"],
            ["BO", "RT", "A", "BE", "HY"],
           ["PO", "S", "OG", "R", "S"],
           ["B", "LD", "I", "E", "N"]]

col_2_row_5 = [["B", "I", "CI", "N", "D"],
            ["W", "A", "R", "A", "KE"],
            ["VE", "UK", "AD", "E", "S"],
           ["G", "O", "V", "A", "S"],
           ["GR", "G", "K", "L", "S"]]

col_3_row_2 = [["IG", "NO", "T", "E", "S"],
            ["SH", "QU", "N", "OR", "CE"],
            ["H", "T", "R", "L", "R"],
           ["E", "AS", "A", "T", "Y"],
           ["MA", "IS", "T", "AN", "I"]]

col_3_row_3 = [["DE", "H", "N", "O", "D"],
            ["P", "A", "V", "NK", "S"],
            ["T", "S", "OT", "RV", "S"],
           ["TH", "O", "A", "K", "E"],
           ["GL", "H", "E", "E", "S"]]

col_3_row_5 = [["CO", "IT", "IT", "E", "O"],
            ["C", "OL", "S", "IG", "NS"],
            ["P", "P", "E", "IB", "CT"],
           ["G", "A", "YF", "A", "AL"],
           ["SP", "R", "IZ", "IC", "HT"]]

col_4_row_2 = [["EN", "AC", "UR", "C", "ER"],
            ["P", "CO", "PP", "A", "H"],
            ["RE", "A", "T", "AG", "TS"],
           ["H", "A", "T", "I", "I"],
           ["W", "P", "E", "CH", "E"]]

col_4_row_4 = [["S", "ES", "U", "A", "E"],
            ["PE", "RN", "E", "L", "E"],
            ["Y", "W", "A", "R", "PHY"],
           ["POD", "O", "O", "M", "ES"],
           ["T", "O", "P", "GRA", "K"]]

col_4_row_5 = [["U", "E", "ION", "E", "R"],
            ["BO", "U", "TT", "C", "AN"],
            ["FA", "K", "K", "R", "H"],
           ["S", "E", "AR", "AB", "LE"],
           ["SH", "SH", "EL", "E", "LE"]]

col_5_row_1 = [["M", "U", "FF", "IO", "NS"],
            ["C", "AT", "CH", "K", "AN"],
            ["T", "O", "N", "E", "S"],
           ["SO", "HA", "TE", "R", "S"],
           ["B", "LU", "CT", "AN", "E"]]


col_5_row_5 = [["B", "I", "EX", "I", "MES"],
            ["W", "HIN", "U", "NC", "D"],
            ["WAS", "O", "R", "L", "E"],
           ["R", "ES", "I", "NTI", "G"],
           ["X", "O", "GTO", "L", "TS"]]

letters = col_3_row_5
words = [row[0] for row in letters]
for col in xrange(1, 5):
    new_words = []
    for row in xrange(5):
        for word in words:
            new_word = word + letters[row][col]
            if dictionary.containsPrefix(new_word.lower()):
                new_words += [new_word]
    words = new_words
actual_words = filter(lambda word: dictionary.contains(word.lower()), words)
print actual_words


