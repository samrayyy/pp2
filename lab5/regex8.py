import re

def split_at_uppercase(input_string):
    pattern = r'[A-Z][a-z]*'  # Matches uppercase letter followed by zero or more lowercase letters
    return re.findall(pattern, input_string)

