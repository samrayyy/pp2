import re

def match_string(input_string):
    pattern = r'ab{2,3}'  # 'a' followed by two to three 'b's
    if re.match(pattern, input_string):
        return True
    else:
        return False

