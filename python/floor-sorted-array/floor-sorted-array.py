from __future__ import print_function
file = open("test.txt", "r")


# read from file
# determine array length
# convert string to int array
# determine key to be found
def parseTest():
	str_arr1 = file.readline().split(" ")
	arr1 = map(int, str_arr1)
	str_arr2 = file.readline().split(" ")
	arr2 = map(int, str_arr2)
	test = [arr1, arr2]

	return test


def findFloor(length, value, A):
	temp = -1
	for i in range (length):
		if(A[i] <= value):
			temp = i
		else:
			break
	return temp
			

# for each ordered array 
# determine the idx of the next highest value
# that is less than or equal to target value
def solveTest():
	test = parseTest()
	test_arr_len = test[0][0]
	value = test[0][1]
	A = test[1]
	idx = findFloor(test_arr_len, value, A)
	print(idx)


# for each test in the test file
# call findFloor
def main():
	if(file.mode == "r" ):
		num_tests = int(float(file.readline()))
		for test in range(num_tests):
			solveTest() 


main()