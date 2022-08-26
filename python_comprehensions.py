#List comprehension
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: Creating a new list and manipulating each value of the old list and adding "+3" to each value.
#This will return 5, 6, 8, 10...
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: Creating a new list and manipulating each value of the old list and adding "*2" to each value.
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)


# Ex3: Creating a new list that have all the numbers divisible by four.
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Creating a new list that have each value-1 when number is divisible by four.
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)


#Dictionary comprehension

""" # Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange) """

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# x**2 is like x*x but more faster. Each value will be multiplied by itself.
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists - zip will return each value of two tuples. 
#1: Jan, 2: Feb, 3: Mar
#new_dict ={key:value for (key, value) in zip(list1, list2)}
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)


#Set comprehension - Same as lists but using {} not []

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

#Generator comprehension - Same as lists but SOME MUCH FASTER.

#This will return 2, 3, 5, 7, 11 - This create a generator, not a list.
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")
