def reverseString(word):
    lastIndex = len(word) - 1
    result=" "
    for i in range(len(word)):
        result = result + word[lastIndex-i]
    return result
print("the same string:",reverseString("Hello PNC"))
print("the same string:",reverseString("Welcome 2021"))