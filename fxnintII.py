#---------1-------------
# x = [ [5,2,3], [10,8,9] ] 
# students1 = [
     # {'first_name':  'Michael', 'last_name' : 'Jordan'},
     # {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
    # 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    # 'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)
# students1[0]["last_name"] = 'Bryant'
# print(students1)
# sports_directory["soccer"][0] = 'Andres'
# print(sports_directory)
# z[0]["y"] = 30
# print(z)

#---------2-------------
# students = [
         # {'first_name':  'Michael', 'last_name' : 'Jordan'},
         # {'first_name' : 'John', 'last_name' : 'Rosales'},
         # {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         # {'first_name' : 'KB', 'last_name' : 'Tonel'}
    # ]

# def iterateDictionary(some_list):
	# for i in range(len(some_list)):
		# for key1, key2 in some_list[i].items():
			# print (key1 + ' - ' + key2)

# iterateDictionary(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#---------3-------------
# def iterateDictionary2(key_name, some_list):
	# for i in range(len(some_list)):
		# print(some_list[i].get(key_name))

# iterateDictionary2('first_name', students)
# Michael
# John
# Mark
# KB

# iterateDictionary2('last_name', students)
# Jordan
# Rosales
# Guillen
# Tonel

#---------4-------------
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# def printInfo(some_dict):
	# for key, val in some_dict.items():
		# print(len(val),key.upper())
		# for item in val:
			# print(item)


# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon