def checkPalindrome (word):

    result = True
    if len(word) == 1:
        return result 
    else:
        for letterPos in range(len(word)):
            if word[letterPos] != word[len(word) - (letterPos+1)]:
                result = False
                break

    return result

w = input("Enter a word: ")
res = checkPalindrome(w)
print(res)
