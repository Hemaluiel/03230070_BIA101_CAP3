
# Github Repo link
# Hema Luitel
# BBI 'A'
# 03230070

# REFERENCES
# https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/
# https://www.youtube.com/watch?v=SXdhA1x4bRU

# Read the input.txt file
def read_input(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
# extract two digit from each line
def extract_value(line):
    first_digit = None
    last_digit = None
    
    for char in line:
        if char.isdigit():
            first_digit = char
            break
            
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
            
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0


# solution
def print_solution(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                value = extract_value(line.strip())
                print(f"Line: {line.strip()} -> Value: {value}")
                total_sum += value
        print("The total sum is:", total_sum)
    except FileNotFoundError:
        print("File not found.")

filename = '070.txt'
print_solution(filename)

