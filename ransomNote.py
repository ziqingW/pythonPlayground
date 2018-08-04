# robber wants to cut words from magazine to make a note, 
# the words from magazine must be complete and case sensitive
# input fotmat: magazine(arr), note(arr)

def ransomNote(magazine, note):
    magazineWords = {}
    for i in range(len(magazine)):
        if magazine[i] in magazineWords:
            magazineWords[magazine[i]].append(i)
        else:
            magazineWords[magazine[i]] = [i]
    for word in note:
        if word in magazineWords and len(magazineWords[word]) > 0:
            magazineWords[word].pop(0)
        else:
            print("No")
            return
    print("Yes")
        