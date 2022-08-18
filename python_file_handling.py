#Reading file. Only the first line
file = open('test.txt', mode = 'r');
data = file.readline();
print(data);

file.close();

###########
#Reading file. Reading multiple lines. Each line is almacened in one array index.
file = open('test.txt', mode = 'r');
data = file.readlines();
print(data);

file.close();

#################

#Reading file. Reading multiple lines. Each line is almacened in one array index.
with open('test.txt', mode = 'r') as file:
    data = file.readlines();
    print(data);


