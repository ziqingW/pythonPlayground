# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. 
# If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # total = list1 + list2
        # result = {}
        # for i,rest in enumerate(total):
        #     if rest not in result:
        #         result[rest] = [i]
        #     else:
        #         result[rest].append(i)
        # result = {rest: sum(result[rest]) for rest in result if len(result[rest])==2}
        # return [rest for rest in result if result[rest]==min(result.values())]
        result = {k:[v] for v,k in enumerate(list1)}
        for i, rest in enumerate(list2):
            if rest in result:
                result[rest].append(i)
        result = {rest: sum(result[rest]) for rest in result if len(result[rest])==2}
        return [rest for rest in result if result[rest]==min(result.values())]
            