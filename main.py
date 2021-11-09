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
state = f.readlines()[0:3]
state = convert_text(state)

# Reset readline to beginning
f.seek(0)

# Read file lines 5 to 7
final = f.readlines()[4:7]
final = convert_text(final)

# Go through state and calculate sum of manhattan distances
sum = 0
for i in range(len(state)):
    for j in range(len(state[i])):
        sum += calculate_manhattan(state, final, i, j)

print(sum)