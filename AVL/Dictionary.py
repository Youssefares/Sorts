# TODO:
# [xx] 1. Load dictionary
# [xx] 2. Print size
# [xx] 3. Insert word
# [xx] 4. Look-up word
# [xx] 5. Remove word
# [xx] 6. Batch look-up
# [xx] 7. Batch deletion

from AVL.AVLTree import AVL
from BST_invariant import is_in_order


class Dictionary:
    def __init__(self):
        self.size = 0
        self.tree = AVL()

    def load_dictionary(self, filename):
        with open(filename) as file:
            for line in file:
                self.insert_word(line.strip())
        print("Load file successful.")

    def insert_word(self, word):
        if self.lookup_word(word):
            print("Error: Word already in dictionary - ", word)
            return False
        else:
            self.tree.insert(word)
            self.size += 1
            print("Word insert successful - ", word)
            return True

    def lookup_word(self, word):
        return self.tree.find(word) is not None

    def remove_word(self, word):
        if not self.lookup_word(word):
            print("Error: Word not found - ", word)
            return False
        else:
            self.tree.delete(word)
            self.size -= 1
            print("Word remove successful - ", word)
            return True

    def batch_lookup(self, filename):
        n_found = 0
        n = 0
        with open(filename) as file:
            for line in file:
                if len(line.strip()) > 0:
                    n += 1
                if self.lookup_word(line.strip()):
                    n_found += 1
                    print(line.strip(), ": YES")
                else:
                    print(line.strip(), ": NO")
        print("Batch lookup finished. Number of words found = ", n_found, " out of ", n)

    def batch_delete(self, filename):
        with open(filename) as file:
            for line in file:
                self.remove_word(line.strip())

    def print_size(self):
        print("Dictionary size: ", self.size)


# #load
# stupid_dictionary = Dictionary()
# stupid_dictionary.load_dictionary("dictionary.txt")
# print("Load successful")
# #printsize
# stupid_dictionary.print_size()
# #insert
# stupid_dictionary.insert_word("Who?")
# #lookup
# print(stupid_dictionary.lookup_word("bond"))
# print(stupid_dictionary.lookup_word("jimmy"))
# #remove
# stupid_dictionary.remove_word("bond")
# stupid_dictionary.remove_word("bond")
# #batchlookup
# stupid_dictionary.batch_lookup("queries.txt")
# #batchdelete
# stupid_dictionary.insert_word("real")
# stupid_dictionary.insert_word("shady")
# stupid_dictionary.insert_word("stand")
# stupid_dictionary.batch_delete("deletions.txt")

if __name__ == '__main__':
    my_dictionary = Dictionary()
    while True:
        print("Please enter one of the following:\n LOAD   : Load dictionary from \"dictionary.txt\"\n SIZE   : Print size\n INSERT : Insert new word\n LOOKUP : Lookup word\n",
    "REMOVE : Remove word\n BLOOKUP: Lookup words in \"queries.txt\"\n BREMOVE: Remove words in \"deletions.txt\"\n EXIT   : Exit program")
        user_input = input()
        if user_input == "LOAD":
            my_dictionary.load_dictionary("dictionary.txt")
            my_dictionary.print_size()
            my_dictionary.tree.print_height()
        elif user_input == "SIZE":
            my_dictionary.print_size()
        elif user_input == "INSERT":
            word = input("Enter word:   ")
            my_dictionary.insert_word(word)
            my_dictionary.print_size()
            my_dictionary.tree.print_height()
        elif user_input == "LOOKUP":
            word = input("Enter word:   ")
            if my_dictionary.lookup_word(word):
                print("YES")
            else: print("NO")
        elif user_input == "REMOVE":
            word = input("Enter word:   ")
            my_dictionary.remove_word(word)
            my_dictionary.print_size()
            my_dictionary.tree.print_height()
        elif user_input == "BLOOKUP":
            my_dictionary.batch_lookup("queries.txt")
        elif user_input == "BREMOVE":
            my_dictionary.batch_delete("deletions.txt")
            my_dictionary.print_size()
            my_dictionary.tree.print_height()
        elif user_input == "EXIT":
            print("شرفتنا يا فندم")
            break
        else:
            print("Invalid command. Please try again.")
            continue
        input(">>Press enter to continue<<\n")
