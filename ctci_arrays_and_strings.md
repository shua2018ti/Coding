# Find unique characters in a string
```python
def unique(string):
	arr = [0] * 256
	for character in string:
		arr[ord(character)] += 1
		if arr[ord(character)] > 1:
			return false
	return true
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
			return false
	return true
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