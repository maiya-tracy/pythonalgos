def selection_sort(some_list):
	for i in range(len(some_list)):
		mini = some_list[i]
		mini_index = i
		for num in range (i, len(some_list)):
			if some_list[num] < mini:
				mini = some_list[num]
				mini_index = num
		some_list[mini_index], some_list[i] = some_list[i], some_list[mini_index]
	return some_list


print(selection_sort([7,1,4,9,2,3,6,10,8,5]))
print(selection_sort([3,6,1]))
print(selection_sort([1,9,3,8]))