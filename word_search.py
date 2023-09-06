import time
from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    @lru_cache(maxsize=None)
    def search(self, word, index=0, count=0, node=None):
        if node is None:
            node = self.root
        if index == len(word):
            return count >= 2
        if word[index] in node.children:
            next_node = node.children[word[index]]
            if next_node.is_end_of_word:
                if self.search(word, index + 1, count + 1):
                    return True
            return self.search(word, index + 1, count, next_node)
        return False

def find_two_largest_compounded_words(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    words.sort(key=len, reverse=True)
    largest_word = None
    second_largest_word = None
    for word in words:
        if trie.search(word):
            if largest_word is None:
                largest_word = word
            elif second_largest_word is None:
                second_largest_word = word
                break
    return largest_word, second_largest_word

with open('Input_02.txt', 'r') as file:
    words = file.read().splitlines()

start_time = time.time()

largest_word, second_largest_word = find_two_largest_compounded_words(words)

end_time = time.time()

print('Largest Compound Word:', largest_word)
print('Second Largest Compound Word:', second_largest_word)
print('Time taken:', end_time - start_time, 'seconds')


