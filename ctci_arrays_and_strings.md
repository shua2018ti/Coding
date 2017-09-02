# Find unique characters in a string
```python
def unique(string):
	arr = [0] * 256
	for character in string:
		arr[ord(character)] += 1
		if arr[ord(character)] > 1:
			return False
	return True
```

# Find if two strings are permutations of each other
```python
def perm(string1, string2):
	arr1 = [0] * 256
	arr2 = [0] * 256
	for character in string1:
		arr1[ord(character)] += 1
	for character in string2:
		arr2[ord(character)] += 1
	for index, character in enumerate(arr1):
		if arr2[index] != character:
			return False
	return False
```

# Replace all "%20" in a string with spaces
```python
def replace(string):
	valids = string.split("%20")
	return " ".join(valids)
```

# Compress a string with repeated characters by replacing the repeated characters with the count
```python
def compress(string):
	character = string[0]
	count = 1
	new_string = ""
	for index in range(2, len(string)):
		if string[index] == character:
			count += 1
		else:
			new_string += character + count
			character = string[index]
			count = 1
	return new_string
```

# Given an NxN matrix that represents an image, write a method to rotate the image by 90 degrees
```python
def rotate(image):
	rotated = [[] * len(image[0])] * len(image)
	column_idx = len(image[0]) - 1
	for row in image:
		row_idx = 0
		for pixel in row:
			rotated[row_idx][column_idx] = pixel
			row_idx += 1
		column_idx += 1
	return rotated
```

# Write an algorithm that if an element in a matrix is 0, the whole column and row are set to 0
```python
def zero(matrix):
	rows = set()
	columns = set()
	for row_idx, row_val in enumerate(matrix):
		for col_idx, col_val in enumerate(row_val):
			if col_val == 0:
				rows.add(row_idx)
				columns.add(col_idx)
	for row in rows:
		matrix[row] = [0] * len(matrix[0])
	for col in columns:
		for row in matrix:
			row[col] = 0
```

# Given an isSubstring method that checks if one word is a substring of another, check if one string is a rotation of another using only one call to isSubstring
```python
def is_rotation(string1, string2):
	return string2.isSubstring(string1 + string1)
```
