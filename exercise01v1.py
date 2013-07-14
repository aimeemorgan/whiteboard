###Given an unsorted array of integers in which all integers appear
###three times, except one integer which appears only one time:
###return the integer which only appears one time.

###solution 1 : sort then compare

###input: [12, 3, 3, 1, 2, 12, 3, 12, 1, 1]

def find_single(array):
	if len(array) % 3 != 1:
		return "Error -- array does not meet stated conditions."
	else:
		array.sort()
		for i in range(len(array)-2):
			if i == 0:
				if array[i] != array[i + 1]:
					if array[i+1] != array[i+2]:
						return array[i+1]
					else:
						return array[0]
			elif i <= (len(array) - 2):
				if (array[i] != array[i-1]) and (array[i] != array[i+1]):
					return array[i]
		return array[-1]

print find_single([12, 3, 3, 1, 2, 12, 3, 12, 1, 1])