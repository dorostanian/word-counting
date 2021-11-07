import sys
import re
from typing import List, Dict
from collections import Counter, OrderedDict


class TextFile:

    _sorted_words_dict: OrderedDict
    _all_words: List[str] = []
    _total_count: int = 0

    def __init__(self, path):
        self._path = path

    def tokenize(self):
        with open(self._path, 'r') as f:
            text = f.read()
            regex = r'\b\w+\b'
            self._all_words = [w.lower() for w in re.findall(regex, text) if w.isalpha()]
            self._total_count = len(self._all_words)

    def get_total_count(self):
        return self._total_count


    def _custom_sort(self, _words_list: List[str], sort_ascending: bool) -> Dict[str, int]:
        for i in range(len(_words_list) - 1):
            for j in range(i + 1, len(_words_list)):
                if sort_ascending:
                    if _words_list[i] > _words_list[j]:
                        temp = _words_list[i]
                        _words_list[i] = _words_list[j]
                        _words_list[j] = temp
                else:
                    if _words_list[i] < _words_list[j]:
                        temp = _words_list[i]
                        _words_list[i] = _words_list[j]
                        _words_list[j] = temp

        return _words_list

    def count_and_sort(self, sort_ascending: bool = True) -> OrderedDict:
        words_count: Counter[str] = Counter(self._all_words) # we could also count ourselves using a dict incrementing a counter by iterating over the words
        self._sorted_words_dict: OrderedDict =  OrderedDict(({
                word: words_count[word]
                for word in self._custom_sort(list(words_count.keys()), sort_ascending)
            }).items())

        return self._sorted_words_dict



if __name__ == '__main__':
    t = TextFile(path=sys.argv[1])
    t.tokenize()
    total_words = t.get_total_count()
    print(f"Number of words: {total_words}")
    for word, count in t.count_and_sort(sort_ascending=True).items():
        print(f"{word} {count}")
