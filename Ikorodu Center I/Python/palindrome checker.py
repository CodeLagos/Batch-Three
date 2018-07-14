wordSpecial = input("Type a word: ")
word = [e for e in wordSpecial if e.isalnum()]
newWord = "".join(word)
count = 0
for i in range(len(word)):
    if (word[i] == word[-1-i]):
        count = count + 1
print(newWord)
if (count == (len(word))):
    print("The word", newWord, "is a palindrome")
else:
    print("The word '", newWord, "'is not a palindrome")
    
