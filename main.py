# Ethan Philpott
# Project 1
# AI
# November 11, 2021
# Professor Wong
# main.py

import copy

# Get file name from command line
filename = input("Enter file name: ")

# Open file
f = open(filename, 'r')

# Get weight from command line
weight = input("Enter weight: ")
# Convert weight to float
weight = float(weight)

past_puzzles = []

# Takes a list of text and converts it into the correct format for the 11 Puzzle problem
# Takes:
#   text: list of strings representing the puzzle
# Returns:
#   text: a 2d list of strings representing the puzzle
def convert_text(text):
    # Strip lines
    text = [line.strip() for line in text]
    # Split lines into list
    text = [line.split() for line in text]
    # Convert list to int
    text = [[int(x) for x in line] for line in text]
    return text

# Calculate manhattan distance
# Takes:
#   puzzle: 2d list of strings for the puzzle
#   goal_puzzle: 2d list of strings for the goal puzzle
#   i: int y coordinate of the current item
#   j: int x coordinate of the current item
# Returns:
#   an int for manhattan distance
def calculate_manhattan(puzzle, goal_puzzle, i, j):
    # Gets item
    item = puzzle[i][j]
    # If item is a blank space then we return 0
    if item == 0:
        return 0
    # Search 2d array for item
    for y in range(len(goal_puzzle)):
        for x in range(len(goal_puzzle[y])):
            # If item found and is not a blank space
            if item == goal_puzzle[y][x] and item != 0:
                # Calculate manhattan distance
                return abs(y - i) + abs(x - j)

# Calculate heuristic for the entire 11 puzzle state
# Takes:
#   puzzle: 2d list of strings for the puzzle
#   final_puzzle: 2d list of strings for the goal puzzle
# Returns:
#   an int for the sum of manhattan distances
def calculate_heuristic(puzzle, final_puzzle):
    # Go through state and calculate sum of manhattan distances
    sum = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            sum += calculate_manhattan(puzzle, final_puzzle, i, j)
    return sum

# Generates a new node for the 11 puzzle problem
# Takes:
#   state: 2d list of strings for the puzzle
#   final_puzzle: 2d list of strings for the goal puzzle
#   i: int y coordinate of the current item
#   j: int x coordinate of the current item
#   swap_i: int y coordinate of the item to swap with
#   swap_j: int x coordinate of the item to swap with
#   action: string for the action taken
# Returns:
#   int representing if the node was added or not (1 if added, 0 if not)
def generate_node(state, final_puzzle, i, j, swap_i, swap_j, action):
     # Copy state
    new_state = copy.deepcopy(state)
    # Swap blank with item above
    puzzle = new_state['puzzle']
    puzzle[i][j], puzzle[swap_i][swap_j] = puzzle[swap_i][swap_j], puzzle[i][j]
    # If this is a duplicate state we just return because we don't count duplicate states
    if (puzzle in past_puzzles):
        return 0
    # Set up new h value
    new_state['h'] = calculate_heuristic(puzzle, final_puzzle)
    # Increment g value
    new_state['g'] += 1
    # Add action
    new_state['a'].append(action)
    # Add f value
    new_state['f'].append(new_state['g'] + new_state['h'] * weight)
    state_list.append(new_state)
    past_puzzles.append(new_state['puzzle'])
    # Returns 1 to increment counter
    return 1

# Creates new state for the 11 puzzle problem
# Takes:
#   index: int location of current state
#   state_list: list of dictionaries representing the current unexplored states
#   final_puzzle: 2d list of strings for the goal puzzle
#   counter: int for the number of states generated
# Returns:
#   None
def create_states(index, state_list, final_puzzle, count):
    # Get puzzle
    puzzle = state_list[index]['puzzle']
    # Find blank space
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            # Found a blank space
            if puzzle[i][j] == 0:
                # If we have an item above the blank
                if(i - 1 >= 0):
                    count += generate_node(state_list[index], final_puzzle, i, j, i - 1, j, "U")
                # If we have an item below the blank
                if(i + 1 < len(puzzle)):
                    # Copy state
                    count += generate_node(state_list[index], final_puzzle, i, j, i + 1, j, "D")
                # If we have an item to the left of the blank
                if(j - 1 >= 0):
                    count += generate_node(state_list[index], final_puzzle, i, j, i, j - 1, "L")
                # If we have an item to the right of the blank
                if(j + 1 < len(puzzle[i])):
                    count += generate_node(state_list[index], final_puzzle, i, j, i, j + 1, "R")
                state_list.pop(index)
    # Choose the next state
    choose_state(state_list, final_puzzle, count)

# Checks if the puzzles are equal
# Takes:
#   puzzle1: 2d list of strings for the puzzle
#   puzzle2: 2d list of strings for the puzzle
# Returns:
#   True if equal, False if not
def equal_puzzles(puzzle1, puzzle2):
    # Check if puzzles are equal
    if puzzle1 == puzzle2:
        return True
    return False

# Prints the output to the terminal and file
# Takes:
#   initial: 2d list of strings for the puzzle
#   state: a dictionary representing the current state
#   count: int for the number of states generated
# Returns:
#   None
def print_output(initial, state, count):
    with open('./outputs/output.txt', 'w') as f:
        # Prints 2d list for initial puzzle
        for i in range(len(initial)):
            for j in range(len(initial[i])):
                print(initial[i][j], end=" ")
                f.write(str(initial[i][j]) + " ")
            print()
            f.write("\n")
    
        # Add newline
        print()
        f.write("\n")

        # Prints 2d list for current state
        for i in range(len(state['puzzle'])):
            for j in range(len(state['puzzle'][i])):
                print(state['puzzle'][i][j], end=" ")
                f.write(str(state['puzzle'][i][j]) + " ")
            print()
            f.write("\n")

        # Add newline
        print()
        f.write("\n")

        # Print weight
        print(float(weight))
        f.write(str(float(weight)) + "\n")

        # Print depth
        print(state['g'])
        f.write(str(state['g']) + "\n")

        # Print count
        print(count)
        f.write(str(count) + "\n")

        # Print actions
        print(" ".join(state['a']))
        f.write(" ".join(state['a']) + "\n")

        # Print f values
        print(" ".join(str(round(x, 4)) for x in state['f']))
        f.write(" ".join(str(round(x, 4)) for x in state['f']))

# Insert in order of lowest f value to greatest
# Takes:
#   state_list: list of dictionaries representing the current unexplored states
#   final_puzzle: 2d list of strings for the goal puzzle
#   count: int for the number of states generated
# Returns:
#   None
def choose_state(state_list, final_puzzle, count):
    # Find lowest f value
    lowest_f = state_list[0]['f'][-1]
    lowest_index = 0
    for i in range(len(state_list)):
        if state_list[i]['f'][-1] < lowest_f:
            lowest_f = state_list[i]['f'][-1]
            lowest_index = i
    if (not equal_puzzles(state_list[lowest_index]['puzzle'], final_puzzle)):
        create_states(lowest_index, state_list, final_puzzle, count)
    else:
        print_output(initial_puzzle, state_list[lowest_index], count)

# Open file
f = open(filename, 'r')

# Read file lines 1 to 3
initial_puzzle = f.readlines()[0:3]
initial_puzzle = convert_text(initial_puzzle)

# Reset readline to beginning
f.seek(0)

# Read file lines 5 to 7
final_puzzle = f.readlines()[4:7]
final_puzzle = convert_text(final_puzzle)

# Get the initial heuristic value
initial_heuristic = calculate_heuristic(initial_puzzle, final_puzzle)
# Holds all the current puzzles, we add the initial state first
state_list = [
    {
        "g": 0,
        "h": initial_heuristic,
        "a": [],
        "f": [initial_heuristic * weight],
        "puzzle": initial_puzzle
    }   
]
past_puzzles.append(state_list[0]['puzzle'])

choose_state(state_list, final_puzzle, 1)