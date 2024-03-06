import re

def find_sequences(input_string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, input_string)

