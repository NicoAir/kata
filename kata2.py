import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    delimiter = ',|\n'
    if numbers.startswith('//'):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[2:]
        numbers_list = re.split(re.escape(delimiter), numbers)
    else:
        numbers_list = re.split(delimiter, numbers)
    numbers_list = [char if element == '' else char for element in numbers_list for char in (list(element) if element != '' else [''])] 
    for num in numbers_list:
        if not num.isdigit():
            position = numbers.find(num)
            raise ValueError(f"'{delimiter}' expected but '{num}' found at position {position}.")
    return sum(int(num) for num in numbers_list if num.isdigit())