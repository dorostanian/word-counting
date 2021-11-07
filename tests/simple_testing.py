import unittest
from collections import OrderedDict

from count_it.word_counter import TextFile


class TestTextFileWordCount(unittest.TestCase):

    def test_tokenization(self):
        t: TextFile = TextFile(path="./test_file_1.txt")
        t.tokenize()
        expected_words = ['the', 'big', 'brown', 'fox', 'number', 'jumped', 'over', 'the', 'lazy', 'dog', 'the', 'big', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog', 'the', 'big', 'brown', 'fox']
        self.assertEqual(expected_words, t._all_words)

    def test_custom_sort(self):
        t: TextFile = TextFile(path="./test_file_1.txt")
        sorted_words = t._custom_sort(
            _words_list=['the',  'brown','big', 'fox'],
            sort_ascending=True
        )
        expected_list = ['big', 'brown', 'fox', 'the']
        self.assertEqual(expected_list, sorted_words)
        # check descending
        sorted_words = t._custom_sort(
            _words_list=['the',  'brown','big', 'fox'],
            sort_ascending=False
        )
        expected_list = ['the', 'fox','brown', 'big']
        self.assertEqual(expected_list, sorted_words)

    def test_total_count(self):
        t: TextFile = TextFile(path="./test_file_1.txt")
        t.tokenize()
        self.assertEqual(23, t.get_total_count())

    def test_counts(self):
        t: TextFile = TextFile(path="./test_file_1.txt")
        t.tokenize()
        sorted_dict = t.count_and_sort(sort_ascending=True)
        expected_dict = OrderedDict(({'big': 3, 'brown': 3, 'dog': 2, 'fox': 3, 'jumped': 2, 'lazy': 2, 'number': 1, 'over': 2, 'the': 5}).items())
        self.assertEqual(expected_dict, sorted_dict)

if __name__ == '__main__':
    unittest.main()