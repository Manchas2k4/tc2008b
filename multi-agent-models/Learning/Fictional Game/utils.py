actions = ["Scissors", "Paper", "Stone"]

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

def translate_move(move):
    return actions[move]
    
def who_won(move_a, move_b):
    diff = move_a - move_b
    if move_a == 0:
        return 0 if move_a == move_b else (-1 if move_b == 1 else 1)
    elif move_a == 1:
        return 0 if move_a == move_b else (-1 if move_b == 2 else 1)
    else:
        return 0 if move_a == move_b else (-1 if move_b == 0 else 1)