import unittest
from word_search import Trie, find_two_largest_compounded_words

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.root.children["a"].children["p"].children["p"].children["l"].children["e"].is_end_of_word)

    def test_search(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("appleapp"))
        self.assertFalse(self.trie.search("applepie"))

class TestFindTwoLargestCompoundedWords(unittest.TestCase):
    def test_find_two_largest_compounded_words(self):
        words = ["apple", "app", "pie", "applepie", "appleapple", "banana"]
        largest, second_largest = find_two_largest_compounded_words(words)
        self.assertEqual(largest, "appleapple")
        self.assertEqual(second_largest, "applepie")

if __name__ == "__main__":
    unittest.main()

