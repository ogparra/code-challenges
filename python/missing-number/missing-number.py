
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


def findMissingnumber(size, arr):

	if( (size == 0) or (len(arr) == 1)): 
		return "No missing number"

	current_sum = 0
	for i in range(size-1):
		current_sum += arr[i]

	total_sum = (size + 1) * size / 2

	
	
	return total_sum - current_sum

# parse Test from file
# call binary search
# print result
def solveTestcase():
	test = parseTest(file)
	size = test[0]
	arr = test[1]
	result = findMissingnumber(size, arr)
	print(result)
	

def main():
	if(file.mode == "r" ):
		tests = int(float(file.readline()))
		for test in range(tests):
			solveTestcase()

main()