def removeMinuses(word):
    newWord=""
    for i in range(len(word)):
        char=word[i]
        if char !="-":
            newWord +=char
    return newWord
condition=True
while condition:
    string=input("Enter string:")
    print("word without minus:"+str(removeMinuses(string)))
    letter=input("Do you want to continue(Y/N):")
    if letter=="Y" or letter=="y":
        condition=True
    if letter=="N" or letter=="n":
       condition=False