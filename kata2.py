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
    for num in numbers_list:
        if not num.isdigit():
            raise ValueError
    return sum(int(num) for num in numbers_list if num.isdigit())