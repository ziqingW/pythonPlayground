# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.hash.keys() or not self.hash[key]:
            self.hash[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.hash.keys():
            self.hash[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hash.keys():
            return self.hash[key]
        return False
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)