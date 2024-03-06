def camel_to_snake(camel_case_string):
    snake_case_string = ''
    for char in camel_case_string:
        if char.isupper() and snake_case_string:
            snake_case_string += '_'
        snake_case_string += char.lower()
    return snake_case_string

