#--1--
# def biggie_size(arr):
	# for val in range(len(arr)):
		# if arr[val] > 0:
			# arr[val] = "big"
	# return(arr)

# print(biggie_size([-1,3,5,-5]))

#--2--
# def count_positives(arr):
	# num = 0
	# for i in range(len(arr)):
		# if arr[i] > 0:
			# num+=1
	# arr[len(arr)-1] = num
	# return arr
	
# print(count_positives([-1,1,1,1]))
# print(count_positives([1,6,-4,-2,-7,-2]))

#--3--
# def sum_total(arr):
	# total = 0
	# for j in arr:
		# total+=j
	# return total

# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

#--4--
# def average(arr):
	# total = 0
	# for j in arr:
		# total+=j
	# return total/len(arr)

# print(average([1,2,3,4]))
# print(average([6,3,-2]))

#--5--
# def length(arr):
	# return len(arr)

# print(length([37,2,1,-9]))
# print(length([]))

#--6--
# def minimum(arr):
	# if len(arr) < 1: return False
	# min = arr[0]
	# for i in arr:
		# if i < min:
			# min = i
	# return min

# print(minimum([37,2,1,-9]))
# print(minimum([]))

#--7--
# def maximum(arr):
	# if len(arr) < 1: return False
	# max = arr[0]
	# for i in arr:
		# if i > max:
			# max = i
	# return max

# print(maximum([37,2,1,-9]))
# print(maximum([]))

#--8--
# def ultimate_analysis(arr):
	# if len(arr) < 1: return False
	# ultDict = {"sumTotal": 0, "average": 0, "minimum": arr[0], "maximum": arr[0], "length": 0}
	# ultDict["length"] = len(arr)
	# for i in arr:
		# if i > ultDict["maximum"]:
			# ultDict["maximum"] = i
			# ultDict["sumTotal"]+=i
		# elif i < ultDict["minimum"]:
			# ultDict["minimum"] = i
			# ultDict["sumTotal"]+=i
		# else:
			# ultDict["sumTotal"]+=i
	# ultDict["average"] = ultDict["sumTotal"]/ultDict["length"]
	# return ultDict

# print(ultimate_analysis([37,2,1,-9]))
# print(ultimate_analysis([]))

#--9--
# def reverse_list(arr):
	# for i in range(int(len(arr)/2)):
		# tmp = arr[i]
		# arr[i] = arr[len(arr)-1-i]
		# arr[len(arr)-1-i] = tmp
	# return arr

# print(reverse_list([37,2,1,-9]))