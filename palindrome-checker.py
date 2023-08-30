def is_palindrome(string):
    string = string.lower()
    cleaned_string = ''.join(char for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
