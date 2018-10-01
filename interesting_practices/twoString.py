# input format: s1, s2 (both are string)
# check if any character is shared in both strings

def twoStrings(s1, s2):
    s1Table = {char: i for (i, char) in enumerate(s1)}
    for char in s2:
        if char in s1Table:
            return "YES"
    return "NO"