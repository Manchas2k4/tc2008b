def integer_input(prompt):
    value = 0

    while True:
        entry = input(prompt)
        try:
            value = int(entry)
        except ValueError:
            print("Invalid input. Please enter an integer number.")

    return value

def integer_input_between(prompt, a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    value = 0

    while True:
        entry = input(prompt)
        try:
            value = int(entry)
            if value >= min_val and value <= max_val:
                break
        except ValueError:
            print("Invalid input. Please enter an integer number.")

    return value