

from __future__ import print_function
from math import floor

file = open("test.txt", "r")

# read from file
# determine array length
# convert string to int array
# determine key to be found
def parseTest(file):
	arr_len = int(float(file.readline()))
	str_arr = file.readline().split(" ")
	arr = map(int, str_arr)
	key = int(float(file.readline()))
		
	test = [arr_len, arr, key]

	return test

# search the left and right of an ordered array
# return idx of key position if found
# else return -1 
def binarySearch(size, arr, key):
	L = 0
	R = size - 1
	m = int(floor((L+R)/2))

	while( L <= R):
		m = int(floor((L+R)/2))
		if(arr[m] < key):
			L = m + 1
		elif(arr[m] > key):
			R = m - 1
		else:
			return m
	return -1

# parse Test from file
# call binary search
# print result
def solveTest(file):
	test = parseTest(file)
	size = test[0]
	arr = test[1]
	key = test[2]
	key_idx = binarySearch(size, arr, key)
	print(arr)
	if(key_idx != -1): 
		print("Key found at idx: %d \n" % key_idx)
	else:
		print("Key not found: %d \n" % -1)

def main():
	if(file.mode == "r" ):
		num_tests = int(float(file.readline()))
		for test in range(num_tests):
			test += 1
			print("Test Case %d" % test)
			solveTest(file) 

# execute main
main()