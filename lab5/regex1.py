import re

def match_string(input_string):
    pattern = r'ab*'  # 'a' followed by zero or more 'b's
    if re.match(pattern, input_string):
        return True
    else:
        return False
test_strings = ['ab', 'abb', 'abbb', 'a', 'ac', 'abc', 'b', 'bb']
for test_string in test_strings:
    print(f"{test_string}: {match_string(test_string)}")