class Underscore:
	def map(self, iterable, callback):
		for i in range(len(iterable)):
			iterable[i] = callback(iterable[i])
		return iterable

	def find(self, iterable, callback):
		for j in range(len(iterable)):
			if callback(j) == True:
				return j

	def filter(self, iterable, callback):
		k = 0
		while (len(iterable)-k > 0):
			if callback(iterable[k]) == False:
				iterable.pop(k)
			else:
				k+=1
		return iterable

	def reject(self, iterable, callback):
		l = 0
		while (len(iterable)-l > 0):
			if callback(iterable[l]) == True:
				iterable.pop(l)
			else:
				l+=1
		return iterable

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

print(evens)



print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==1)) # should return [1,3,5]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]