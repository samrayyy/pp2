def is_palindrome(string):
    string = string.lower()
    string = ''.join(char for char in string if char.isalnum())
    return string == string[::-1]
