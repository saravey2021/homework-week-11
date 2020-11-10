def numberOfUpperCase(word):  
   countUpperCase = 0 
   for n in range(len(word)):
      if word[n].upper()==word[n]:
         countUpperCase = countUpperCase + 1
   return countUpperCase
word = input("Enter word: ")
print("Number of uppercase letter: " + str(numberOfUpperCase(word)))
