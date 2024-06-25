def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers_list = numbers.split(",")
    return sum([int(number) for number in numbers_list])