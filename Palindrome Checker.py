print("Welcome to Palindrome Checker")

def palindrome(word):
    word = word.lower().replace(" ","")
    return word == word[::-1]
    


inp = input("Enter the word/number: ")
if palindrome(inp):
    print(f"The given {inp} is a palindrome")

else:
    print(f"The given {inp} is not a palindrome")
