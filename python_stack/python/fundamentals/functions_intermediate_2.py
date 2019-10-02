# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15 # 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
students[0]['last_name'] = 'Bryant' # 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
sports_directory['soccer'][0] = 'Andres' # 3. In the sports_directory, change 'Messi' to 'Andres'
z[0]['y'] = 30 # 4. Change the value 20 in z to 30

# 2. Iterate Through a List of Dictionaries

def iterateDictionary(arr):
    for student in students:
        for key, val in student.items():
            print(key, " = ", val)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for i in range (len(students)):
        print(some_list[i][key_name])
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(some_dict[key])} {key.upper()}")
        for i in range (len(val)):
            print(some_dict[key][i])

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

# def printInfo(some_dict):
#     for y in some_dict:
#         print(len(some_dict[y]), y)
#         for i in range(0,len(some_dict[y]),1):
#             print(some_dict[y][i])
        
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)