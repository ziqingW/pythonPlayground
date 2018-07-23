def findDiff(text1, text2):
    text1 = set(text1)
    text2 = set(text2)
    if len(text1) >= len(text2):
        for cha in set(text1):
            if cha not in set(text2):
                return cha
    else:
        for cha in set(text2):
            if cha not in set(text1):
                return cha
    


print(findDiff('aaabbcdd', 'abdbacade'))

    