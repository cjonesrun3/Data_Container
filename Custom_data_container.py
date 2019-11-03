import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __add__(self, item):
        bisect.insort(self._items, item)

items = SortedItems([7, 2, 4, 5, 10])
print(list(items))
items.__add__(22)
print(list(items))
print(len(items))