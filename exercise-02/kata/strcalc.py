import re

def add(numbers):
    if not numbers:
        return 0
    
    # Parse custom delimiter from input string
    delimiter = ","
    if numbers.startswith("//"):
        match = re.search("//(.+)\n", numbers)
        if match:
            delimiter = re.escape(match.group(1))
            numbers = numbers[len(match.group(0)):]

    # Split input string into numbers using the delimiter
    numbers_list = re.split("[\n" + delimiter + "]", numbers)

    # Convert numbers to integers and sum them
    result = 0
    negatives = []
    for num in numbers_list:
        if num:
            int_num = int(num)
            if int_num < 0:
                negatives.append(int_num)
            elif int_num <= 1000:
                result += int_num

    # Raise exception if negatives are found
    if negatives:
        raise Exception("negatives not allowed: " + ",".join(str(n) for n in negatives))

    return result
