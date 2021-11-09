import copy

# Takes an array of text and converts it into the correct format for the 11 Puzzle problem
def convert_text(text):
    # Strip lines
    text = [line.strip() for line in text]
    # Split lines into list
    text = [line.split() for line in text]
    # Convert list to int
    text = [[int(x) for x in line] for line in text]
    return text

# Calculate manhattan distance
def calculate_manhattan(state, goal, current_x, current_y):
    # Gets item
    item = state[current_x][current_y]
    # Search 2d array for item
    for x in range(len(goal)):
        for y in range(len(goal[x])):
            # If item found and is not a blank space
            if item == goal[x][y] and item != 0:
                # Calculate manhattan distance
                return abs(x - current_x) + abs(y - current_y)
            # If item found and is a blank space then we return 0
            elif item == 0:
                return 0

# Calculate heuristic for the entire 11 puzzle state
def calculate_heuristic(state, final):
    # Go through state and calculate sum of manhattan distances
    sum = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            sum += calculate_manhattan(state, final, i, j)
    return sum

# Creates new state for the 11 puzzle problem
def create_states(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # If we have an item above the blank
                if(i - 1 >= 0):
                    # Copy state
                    up = copy.deepcopy(state)
                    # Swap blank with item above
                    up[i][j], up[i - 1][j] = up[i - 1][j], up[i][j]
                # If we have an item below the blank
                if(i + 1 < len(state)):
                    # Copy state
                    down = copy.deepcopy(state)
                    # Swap blank with item below
                    down[i][j], down[i + 1][j] = down[i + 1][j], down[i][j]
                # If we have an item to the left of the blank
                if(j - 1 >= 0):
                    # Copy state
                    left = copy.deepcopy(state)
                    # Swap blank with item to the left
                    left[i][j], left[i][j - 1] = left[i][j - 1], left[i][j]
                # If we have an item to the right of the blank
                if(j + 1 < len(state[i])):
                    # Copy state
                    right = copy.deepcopy(state)
                    # Swap blank with item to the right
                    right[i][j], right[i][j + 1] = right[i][j + 1], right[i][j]

# Get file name from command line
#filename = input("Enter file name: ")
filename = "./samples/Input1.txt"

# Open file
f = open(filename, 'r')

# Get weight from command line
# weight = input("Enter weight: ")
# Convert weight to float
# weight = float(weight)

# Read file lines 1 to 3
initial = f.readlines()[0:3]
initial = convert_text(initial)

# Reset readline to beginning
f.seek(0)

# Read file lines 5 to 7
final = f.readlines()[4:7]
final = convert_text(final)