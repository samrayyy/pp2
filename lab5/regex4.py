import re

def find_sequences(input_string):
    pattern = r'[A-Z][a-z]+'  # Sequence of one uppercase letter followed by lowercase letters
    return re.findall(pattern, input_string)
