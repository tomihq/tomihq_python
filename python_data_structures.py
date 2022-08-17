#Lists - Can almacenate any datatype. We can access each value using the index. The first element is in the [0] position.

list1 = [1, 2, 3, 4, 5];
print(list1[2]); #Will return 3.
list2 = ['A', 'B', 'C'];
list3 = ['Hello', 1, True, 48.22];
list4 = [1, [2, 3, 4], 5, 6];

#Printing all my lists values.
print(*list2); #As values
print(list2, sep = " "); #As array

#Insert element to a list specifing the index.
list2.insert(len(list2), 'Tomás'); #Tomas is added in the last index of our list.
print(*list2);

#Insert element to a list (in the last index without specification)
list2.append('Tomás2'); #Tomas2 is added in the last index of our list.
print(*list2);

#Insert elements to a list. 
list2.extend(['Tomas3', 'Tomas4', 'Tomas5']);

#Delete elements in a list.
list2.pop(6); #Delete the element that figures in the index 6.

del list2[2]; #Delete the element that figures in the index 2.

print(*list2);

#Loop data
for x in list2:
    print(x);

#####################################################################################################################################################################

#Tuples - We can access each value using the index. The first element is in the [0] position.

my_tuple = (1, 'string', 4.5, True, 'string');
print(type(my_tuple)) #Returns class "tuple"

#Returns how much times is repeated the 'string' word in the tuple.
print(my_tuple.count('string')); 

#Returns the index where is the value that we proporcionate.
print(my_tuple.index(4.5));

#Loop data
for x in my_tuple:
    print(x);

""" my_tuple[1] = 'hola';  """#This will return an error. Tuples are immutable.


#####################################################################################################################################################################

#Sets - Duplicated values won't be shown, it's a collection of unaltered items (We can't use INDEX to access an element.).
set_a = {1, 2, 3, 4, 5, 5};
""" print(set_a) #This will return 1, 2, 3, 4, 5,  """

#adding items to a set
""" set_a.add(6); """ #This will add number 6 to the set.

#removing items from a set
""" set_a.remove(2);  """#This will remove number 2 from the set.
""" set_a.discard(2); """ #This will remove number 2 from the set.

""" print(set_a); """

##### Maths operations for sets #####

set_b = {4, 5, 6, 7, 8};

#Union (union or |) - Match all values.
print(set_a.union(set_b)); #This will return 1, 2, 3, 4, 5, 6, 7, 8
print(set_a | set_b); #This will return 1, 2, 3, 4, 5, 6, 7, 8

#Intersection (intersection or &) - Return values that are in the two sets.
print(set_a.intersection(set_b)); #This will return the values that are inside the two sets. 4, 5.
print(set_a & set_b); #This will return the values that are inside the two sets. 4, 5.

#Difference (difference or -)- Returns the element that are in the left set but no in the right one. This is applied on Maths differences, working with sets.
print(set_a.difference(set_b)); #This will return 1, 2, 3
print(set_a - set_b); #This will return 1, 2, 3

#SymmetricDiference (symmetric_difference or ^) - Returns elements that are not in the both sets.
print(set_a.symmetric_difference(set_b)) #This will return, 1, 2, 3, 6, 7, 8
print(set_a ^ set_b) #This will return, 1, 2, 3, 6, 7, 8

#####################################################################################################################################################################

#Dictionary - Use keys, not index. Much faster than lists.

my_simple_dictionary = {1: 'coffee', 2: 'tea', 3: 'green_tea'};
print(type(my_simple_dictionary));
print(my_simple_dictionary[1]); #This will return 'coffee. We're accesing by the key 1.

#delete element to dictionary
del my_simple_dictionary[3]; #This will remove greeen_tea
print(my_simple_dictionary)

#modify element from dictionary
my_simple_dictionary[2] = 'red tea';
print(my_simple_dictionary);


my_simple_dictionary2 = {'name': 'Tomas', 'name': 'Mark'}; #Dictionary can have the same key, but the last will delete the first one.
print(my_simple_dictionary2['name']);


#Iterate dictionary

#This will show the element saved in each key.
for x in my_simple_dictionary:
    """     print(x) """
    
#This will show the key, and the element.
for key, value in my_simple_dictionary.items():
    print(str(key) + " : " + value);

