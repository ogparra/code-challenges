
file = open("test.txt", "r")

# read from file
# determine array length
# convert string to int array
# determine target to be found
def parseTest(file):
	arr_len = int(float(file.readline()))
	str_arr = file.readline().split(" ")
	arr = map(int, str_arr)
	target = int(float(file.readline()))
		
	test = [arr_len, arr, target]

	return test


def rotatedSearch(arr, left, right, target):
	print("left: %d" % left)	
	print("right: %d" % right)	
	# Check to see if the left and right value equal each other
	if(left == right):
		if(arr[left] == arr[right]):
			return left
		else:
			return -1

	# Check if middle element is equal to target
	mid = (left + right)/2
	if (arr[mid] == target): 
		return mid

	# Pivot point is a the right of the middle element
	if(arr[left] <= arr[mid]):
		if( (target >= arr[left]) and (target <=[mid]) ):
			return rotatedSearch(arr, left, mid - 1, target)
		return rotatedSearch(arr, mid + 1, right, target)

	# Pivot is at the left of the middle element
	if( (target >= arr[mid]) and (target <= arr[right]) ):
		return rotatedSearch(arr, mid + 1, right, target)
	
	return rotatedSearch(arr, left, mid - 1, target)
	



# parse Test from file
# call binary search
# print result
def solveTestcase():
	test = parseTest(file)
	size = test[0]
	arr = test[1]
	target = test[2]
	idx = rotatedSearch(arr, 0, size-1, target)
	print(idx)
	

def main():
	if(file.mode == "r" ):
		tests = int(float(file.readline()))
		for test in range(tests):
			solveTestcase()

main()