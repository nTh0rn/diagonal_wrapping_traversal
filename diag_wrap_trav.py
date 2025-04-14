"""
Written by Nikolas Thornton
https://www.nthorn.com/blog/diagonal_traversal
"""
import math

# Print a 2d list
def print_list(list):
    for row in list:
        print(row)

# Convert string of square-length to list
def string_to_list(string):
    output=[]
    side_len = math.isqrt(len(string))
    for i in range(0,len(string)):
        if (i) % side_len == 0:
            output.append([])
        output[-1].append(string[i])
    return output

# Convert matrix to diagonally-traversed string
def diagonal_conversion(matrix):
    l = len(matrix)  # Side length of matrix
    
    # The coordinates that will be walked-through later
    x_coords = []
    y_coords = []

    # Basis matrix for the slider
    basis = []
    for i in range(0, len(matrix)):
        basis.append(i)

    # Slides along the basis, start/end denoted by head/tail.
    def slider(head, y=False):
        output = []
        tail = head - len(basis) + 1

        # If head or tail is out of bounds of the basis, reset them to the start/end
        if tail < 0:
            tail += l - (head + 1)
        if head > l - 1:
            head -= head - (l - 1)

        # Iterate through the basis from the tail to head
        for index in range(tail, head + 1):
            output.append(basis[index])

        # Reverse this output if its for the y-direction
        if y == True:
            output.reverse()
        return output

    # Generate x and y coordinates
    for i in range(0, l * 2 - 1):
        for item in slider(i):
            x_coords.append(item)
        for item in slider(i, True):
            y_coords.append(item)

    # Walk along the matrix using the generated x and y coordinates.
    final_string = ""
    for i in range(0, l * l):
        final_string += matrix[y_coords[i]][x_coords[i]]
    return final_string


original_string="123456789" # MUST BE OF SQUARE-NUMBER LENGTH
diagonal_string=diagonal_conversion(string_to_list(original_string))

print("Original string: \"" + original_string + "\"")

print("Original string as matrix:")
print_list(string_to_list(original_string))

print("\nDiagonal string: \"" + diagonal_string + "\"")

pause = input("")