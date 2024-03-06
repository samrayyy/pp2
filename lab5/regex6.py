import re

def replace_characters(input_string):
    pattern = r'[ ,.]'  # Matches space, comma, or dot
    replacement = ':'    # Replace with colon
    return re.sub(pattern, replacement, input_string)

