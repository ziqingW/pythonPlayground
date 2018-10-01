word = raw_input("What's your word?")
vowel = ['a','e','i','o','u']
index = None
for i in range(len(word)):
  if word[i] in vowel:
    index = i
    break
word = word[index:] + word[:index] + "ay"
print word  