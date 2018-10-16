# Design a data structure that supports all following operations in average O(1) time.

# 1. insert(val): Inserts an item val to the set if not already present.
# 2. remove(val): Removes an item val from the set if present.
# 3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

import random
import math
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomdict = {}
        self.randomlist = []
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.randomdict:
            self.randomdict[val] = self.size
            self.randomlist.append(val)
            self.size += 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomdict:
            pos = self.randomdict[val]
            temp = self.randomlist[pos]
            last = self.randomlist[-1]
            self.randomdict[last] = pos
            self.randomlist[pos] = last
            self.randomlist[-1] = temp
            del self.randomdict[val]
            self.randomlist.pop()
            self.size -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        r = math.floor(random.random() * self.size)
        return self.randomlist[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()