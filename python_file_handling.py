import random
###########READING##################
#Reading file. Only the first line
file = open('test.txt', mode = 'r');
data = file.readline();
""" print(data); """

file.close();

#####################################################################################################################################################################
#Reading file. Reading multiple lines. Each line is almacened in one array index.
file = open('test.txt', mode = 'r');
data = file.readlines();
""" print(data); """

file.close();

#Reading file. Reading multiple lines. Each line is almacened in one array index.
with open('test.txt', mode = 'r') as file:
    data = file.readlines();
    """  print(data); """

###########WRITING##################
#We're writing a file. We're overwriting the old data if file had something, if the file didn't exists, it create it.
with open('test.txt', 'w') as file:
    #Write the first line
    file.write('This is a new line of the file')
    #Write the second, and the third line.
    file.writelines([' \nThis is the second line', ' \nThis is the third line'])
#####################################################################################################################################################################

###########EDITING##################
with open('test.txt', 'a') as file:
    #Add a new line without deleting the old text.
    file.write('\nThis is a new line of the file without deleting the old text')

#####################################################################################################################################################################

#Preventing exceptions with file.

#Opening
try:
    with open('test.txt', 'r') as file:
        data = file.readlines();
        print(data); 
except FileNotFoundError as e:
    print(e, ': El archivo no existe en la ruta especificada.')
except Exception as e:
    print(e, ': Oops, something went wrong.')

#Editing
try:
    with open('test2.txt', 'a') as file:
        data = file.readlines();
        print(data); 
except IOError as e:
    print(e, ': La edición no puede llevarse a cabo. El archivo a editar no existe en la ruta especificada.')
except Exception as e:
    print(e, ': Oops, something went wrong.')

#####################################################################################################################################################################

#Get name of the file via input - petnames.txt - And get a random pet of the list.

f_name = input('Type the file name: ')
f = open(f_name) #If you only want to read, you don't need to specify the "r" because it's the default mode.
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))