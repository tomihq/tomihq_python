from re import T

#Variables can't be declared with a white space.
#The below code will throw an error syntax

""" person name = 'Tomas' """ 

#########

print("Hello") 
print("World")

#Addition 1 + 2 + 3.
x = 1 + 2 \
+ 3 

print (x)

# Esto es un comentario jeje 
name = "John";

if name == "John": #Comentario 2 
    print(name);


#Variables

myName = 'Tomás';

n1, n2, n3 = 1, 2, 3

print(myName);
print(n1);
print(n2);
print(n3);

""" del n3;

print(n3); """

name = 'Tomas' # String
listOfNames = ['Tomas', 'Gonzalo']; # Lista - Se pueden modificar
tupleOfNames = ('Tomas', 'Gonzalo') #Tupla - No se puede modificar
integerNumber = 1; #Entero
floatNumber = 1.4; #Flotante
complexNumber = 1 + 4j; #Complejo
dictionaryVariable = {'name': 'Tomás', 'age': 21, 'profession': 'Lead team'}; #Dictionary
print(dictionaryVariable["name"]);
setVariable = {'name', 'Tomás', 'name', 'Gonzalo'}; #Set formado incorrectamente, se repiten los valores.
print(setVariable);
setVariable = {'name', 'age', 10, 'year'}; #Set formado correctamente

#String single line
stringData = 'Tomás';

#String multiple lines
stringDataName = 'This is a very long string which needs \
to wrap across multiple lines because \
otherwise my code is unreadable.';

#String manipulated as an array
name = 'John';
print(name[0]) #Returns J

#Concatenation
name = 'John';
name2 = 'Tomas';

print(name + ' and ' + name2);

#String length
print(len(name));

#Input on console
print("¿Cual es tu nombre?")
name = input()
print("Así que tu nombre es " + name) 

#Funciones
def helloWorld(name):
    return print('Hola ' +name);

helloWorld('Tomas');


