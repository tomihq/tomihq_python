
menu = ["espresso", "mocha", "latte", "cappucino", "cortado", "americano"];

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

#WTF IS THIS - LONG LIFE TO JAVASCRIPT

#MAP - WTF IS THIS - Take all objects in a list and applies a function.
map_coffee = map(find_coffee, menu)
print(map_coffee);
for x in map_coffee:
    print(x)

#FILTER - WTF IS THIS - Take all objects in a list and applies a function, and take the results and creates a new list with only the true values 

filter_coffee = filter(find_coffee, menu);
print(filter_coffee);
for x in filter_coffee:
    print(x)
