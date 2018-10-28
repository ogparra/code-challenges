

file = open("test.txt", "r")

# read from file
# determine array length
# convert string to int array
# determine target to be found
def parseTest(file):
	arr_len = int(float(file.readline()))
	str_arr = file.readline().split(" ")
	arr = map(int, str_arr)
		
	test = [arr_len, arr]

	return test


def findElement(size, arr):

	if(size == 0 or size == 1):
		return "Array is empty or has size 1"

	if(size == 2):
		if(arr[0] > arr[1]):
			element = arr[0] - arr[1]
			return element
		else:
			element = arr[1] - arr[0]
			return element

	else:
		m = size/2
		




# parse Test from file
# call binary search
# print result
def solveTestcase():
	test = parseTest(file)
	size = test[0]
	arr = test[1]
	target = test[2]
	result = rotatedSearch(arr, 0, size-1, target)
	print(result)
	

def main():
	if(file.mode == "r" ):
		tests = int(float(file.readline()))
		for test in range(tests):
			solveTestcase()

main()