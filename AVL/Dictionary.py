# TODO:
# [x] 1. Load dictionary
# [x] 2. Print size
# [x] 3. Insert word
# [x] 4. Look-up word
# [x] 5. Remove word
# [x] 6. Batch look-up
# [x] 7. Batch deletion

from AVL.AVL import AVL


class Dictionary:
    def __init__(self):
        self.size = 0
        self.tree = AVL()

    def load_dictionary(self, filename):
        with open(filename) as file:
            for line in file:
                self.insert_word(self, line.strip())

    def insert_word(self, word):
        if self.lookup_word(self, word):
            print("Error: Word already in dictionary.")
        else:
            self.tree.insert(word)

    def lookup_word(self, word):
        return self.tree.find(word) is not None

    def remove_word(self, word):
        if not self.lookup_word(self, word):
            print("Error: Word not found.")
        else:
            self.tree.delete(word)

    def batch_lookup(self, filename):
        n = 0
        with open(filename) as file:
            for line in file:
                if self.lookup_word(self, line.strip()):
                    n += 1
                    print(line.strip(), ": YES")
                else:
                    print(line.strip(), ": NO")
        print("Batch lookup finished. Number of found words = ", n)

    def batch_delete(self, filename):
        with open(filename) as file:
            for line in file:
                self.remove_word(self, line.strip())

    def print_size(self):
        print("Dictionary size: ", self.size)
