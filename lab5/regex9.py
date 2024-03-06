import re

def insert_spaces(input_string):
    pattern = r'([A-Z][a-z]*)'  # Matches words starting with a capital letter
    spaced_string = re.sub(pattern, r' \1', input_string).strip()
    return spaced_string
