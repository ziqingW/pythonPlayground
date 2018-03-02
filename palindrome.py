word = raw_input("Give me your word: ")
if word == word[::-1]:
  print "This is a palindrome."
else:
  print "No, it's not a palindrome."