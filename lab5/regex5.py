import re

def match_string(input_string):
    pattern = r'a.*b$'  # 'a' followed by anything, ending in 'b'
    if re.match(pattern, input_string):
        return True
    else:
        return False
