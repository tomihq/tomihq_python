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


