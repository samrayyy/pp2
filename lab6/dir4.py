def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
