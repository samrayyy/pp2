def rep(input_string):
    ascii_string = ""
    for char in input_string:
        if char.isalpha():  
            ascii_string += str(ord(char)) + " "
        else:
            ascii_string += char + " "
    return ascii_string.strip()

def main():
    input_string = input()
    ascii_string = rep(input_string)
    print(ascii_string)


