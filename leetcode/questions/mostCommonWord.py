# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

import re
import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = re.sub(r"['.,;!?]", " ", paragraph.lower())
        para = re.sub(r" +", " ", para).strip().split(" ")
        counter = collections.Counter(para)
        for word in banned:
            if word in counter:
                del counter[word]
        return counter.most_common()[0][0]
        
            
        