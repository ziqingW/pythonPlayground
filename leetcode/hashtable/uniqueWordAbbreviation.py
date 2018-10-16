# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

# a) it                      --> it    (no abbreviation)

#      1
#      ↓
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
# A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        if len(dictionary) > 0:
            self.abbreviation = collections.defaultdict(dict)
            for word in dictionary:
                if len(word) < 3:
                    ab_word = word
                else:
                    ab_word = word[0] + str(len(word[1:-1])) + word[-1]  
                if word not in self.abbreviation[ab_word]:
                    self.abbreviation[ab_word][word] = True
        else:
            self.abbreviation = {}

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if self.abbreviation:
            if len(word) > 0:
                if len(word) < 3:
                    ab_word = word
                else:
                    ab_word = word[0] + str(len(word[1:-1])) + word[-1]
                if ab_word in self.abbreviation:
                    if len(self.abbreviation[ab_word].keys()) > 1:
                        return False
                    else:
                        if word not in self.abbreviation[ab_word]:
                            return False
        return True
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)