#Not pure function - We're manipulating global scope variable.
my_list = [1, 2, 3];

def add_to_list(item):
    return my_list.append(item);
    
add_to_list(4);

print (my_list);

#Pure function - We are not manipulating original list that his declaration on global scope, we're cloning it.
my_list2 = [1, 2, 3];

def add_to_list(item, my_list2):
    new_list2 = my_list2.copy();
    new_list2.append(item);
    return new_list2;

print(my_list2);
new_list2 = add_to_list(4,my_list2);
print(new_list2);

