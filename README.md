# A Star Search
### By: Ethan Philpott

## Running
To run, do `python3 main.py`

The program will ask you to input a filename and weight. Type them down and hit enter. For instance
```
> python3 main.py
Enter file name: ./inputs/Input3.txt
Enter weight: 1.4
```
## Outputs

### Output1a.txt

File: input1.txt

Weight: 1.0
```
2 0 6 4 
3 10 7 9 
11 5 8 1 

2 10 6 4 
11 3 8 9 
0 7 5 1 

1.0
7
22
D R D L U L D
7.0 7.0 7.0 7.0 7.0 7.0 7.0 7.0
```

### Output1b.txt

File: input1.txt

Weight: 1.2
```
2 0 6 4 
3 10 7 9 
11 5 8 1 

2 10 6 4 
11 3 8 9 
0 7 5 1 

1.2
7
22
D R D L U L D
8.4 8.2 8.0 7.8 7.6 7.4 7.2 7.0
```

### Output1c.txt

File: input1.txt

Weight: 1.4
```
2 0 6 4 
3 10 7 9 
11 5 8 1 

2 10 6 4 
11 3 8 9 
0 7 5 1 

1.4
7
22
D R D L U L D
9.799999999999999 9.399999999999999 9.0 8.6 8.2 7.8 7.4 7.0
```

### Output2a.txt

File: input2.txt

Weight: 1.0
```
2 0 6 4 
3 10 7 9 
11 5 8 1 

2 7 8 4 
10 6 9 1 
3 11 0 5 

1.0
13
32
R D D L L U R U R D R D L
13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0 13.0
```

### Output2b.txt

File: input2.txt

Weight: 1.2
```
2 0 6 4 
3 10 7 9 
11 5 8 1 

2 7 8 4 
10 6 9 1 
3 11 0 5 

1.2
13
29
R D D L L U R U R D R D L
15.6 15.399999999999999 15.2 15.0 14.799999999999999 14.6 14.4 14.2 14.0 13.8 13.6 13.4 13.2 13.0
```

### Output2c.txt

File: input2.txt

Weight: 1.4
```
2 0 6 4 
3 10 7 9 
11 5 8 1 

2 7 8 4 
10 6 9 1 
3 11 0 5 

1.4
13
29
R D D L L U R U R D R D L
18.2 17.799999999999997 17.4 17.0 16.6 16.2 15.799999999999999 15.399999999999999 15.0 14.6 14.2 13.8 13.4 13.0
```

### Output3a.txt

File: input3.txt

Weight: 1.0
```
8 7 2 4 
10 6 9 1 
0 11 5 3 

10 6 8 4 
9 7 0 2 
11 5 3 1 

1.0
17
169
R U R U L L D R D R R U L U L D R
13.0 13.0 15.0 15.0 15.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0 17.0
```

### Output3b.txt

File: input3.txt

Weight: 1.2
```
8 7 2 4 
10 6 9 1 
0 11 5 3 

10 6 8 4 
9 7 0 2 
11 5 3 1 

1.2
17
125
R U R U L L D R D R R U L U L D R
15.6 15.399999999999999 17.6 17.4 17.2 19.4 19.2 19.0 18.799999999999997 18.6 18.4 18.2 18.0 17.8 17.6 17.4 17.2 17.0
```

### Output3c.txt

File: input3.txt

Weight: 1.4
```
8 7 2 4 
10 6 9 1 
0 11 5 3 

10 6 8 4 
9 7 0 2 
11 5 3 1 

1.4
17
125
R U R U L L D R D R R U L U L D R
18.2 17.799999999999997 20.2 19.799999999999997 19.4 21.799999999999997 21.4 21.0 20.6 20.2 19.799999999999997 19.4 19.0 18.6 18.2 17.8 17.4 17.0
```

## Source Code
```python
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

# Takes an array of text and converts it into the correct format for the 11 Puzzle problem
def convert_text(text):
    # Strip lines
    text = [line.strip() for line in text]
    # Split lines into list
    text = [line.split() for line in text]
    # Convert list to int
    text = [[int(x) for x in line] for line in text]
    return text

# Calculate manhattan distance, given a puzzle with coordinates current_x, current_y and the goal puzzle
def calculate_manhattan(puzzle, goal_puzzle, current_x, current_y):
    # Gets item
    item = puzzle[current_x][current_y]
    # Search 2d array for item
    for x in range(len(goal_puzzle)):
        for y in range(len(goal_puzzle[x])):
            # If item found and is not a blank space
            if item == goal_puzzle[x][y] and item != 0:
                # Calculate manhattan distance
                return abs(x - current_x) + abs(y - current_y)
            # If item found and is a blank space then we return 0
            elif item == 0:
                return 0

# Calculate heuristic for the entire 11 puzzle state
def calculate_heuristic(puzzle, final_puzzle):
    # Go through state and calculate sum of manhattan distances
    sum = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            sum += calculate_manhattan(puzzle, final_puzzle, i, j)
    return sum

# Generates a new node for the 11 puzzle problem
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
    choose_state(state_list, final_puzzle, count)

def equal_states(state1, state2):
    # Check if states are equal
    if state1 == state2:
        return True
    return False

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
        print(" ".join(str(x) for x in state['f']))
        f.write(" ".join(str(x) for x in state['f']))

# Chooses state from puzzle list to expand next
def choose_state(state_list, final_puzzle, count):
    # Find lowest f value
    lowest_f = state_list[0]['f'][-1]
    lowest_index = 0
    for i in range(len(state_list)):
        if state_list[i]['f'][-1] < lowest_f:
            lowest_f = state_list[i]['f'][-1]
            lowest_index = i
    if (not equal_states(state_list[lowest_index]['puzzle'], final_puzzle)):
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

# Holds all the current puzzles
initial_heuristic = calculate_heuristic(initial_puzzle, final_puzzle)
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
```