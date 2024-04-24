"""
Written by Nikolas Thornton
https://www.nthorn.com/blog/diagonal_traversal
"""

import numpy as np
import math

#Print a 2d list
def print_list(list):
	for row in list:
		print(row)

#Convert string of square-length to list
def string_to_list(input):
	outp=[[]]
	x = -1 # Set to -1 since it is increased by 1 upon first use
	y = 0
	for char in input:
		x += 1
		if x == np.sqrt(len(input)):
			outp.append([])
			y += 1
			x = 0
		outp[y].append(char)
	return outp
	

#Convert matrix to diagonally-traversed string
def diagonal_conversion(matrix):
	l = len(matrix)  # Side length of matrix
	
	# The coordinates that will be walked-through later
	x_coords = []
	y_coords = []

	#Basis matrix for the slider
	basis = []
	for i in range(0, len(matrix)):
		basis.append(i)

	# This slides along the "basis" selecting a side-length number of consecutive items in it, where the far
	# end is denoted by the "header" and the back-end is denoted by the "tail" (i realize now i have the tail
	# at the beginning lol)
	def slider(header, y=False):
		output = []
		tail = header - len(basis) + 1

		# If header or tail is out of bounds of the basis, reset them to the start/end
		if tail < 0:
			tail += l - (header + 1)
		if header > l - 1:
			header -= header - (l - 1)

		# Iterate through the basis from the tail to header
		for index in range(tail, header + 1):
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


pre_diag_string="123456789" # MUST BE OF SQUARE-NUMBER LENGTH
post_diag_string=diagonal_conversion(string_to_list(pre_diag_string))

print("Pre-diagonal string: \"" + pre_diag_string + "\"")
print_list(string_to_list(pre_diag_string))

print("\nPost-diagonal string: \"" + post_diag_string + "\"")

pause = input("")