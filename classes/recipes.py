""" class RecipeExample():
    ##cls - It acts as a placeholder for passing the class as its first argument
    ##Which will be used for creating the new empty object.
    def __new__(cls: type[Self]) -> Self:
        pass

    #It's like the constructor in others PL. Take a new object as its first argument.
    #It's a convention sending self as the first argument.
    def __init__(self) -> None:
        pass
 """

class Recipe():

    def __init__(self, dish, items, time) -> None:
        self.dish = dish; 
        self.items = items;
        self.time = time;

    def contents(self):
        print("The " + str(self.dish) + " has " + str(self.items) + \
            " and takes " + str(self.time) + " min to prepare");

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45);
pasta = Recipe("Pasta", ["spaghetti", "sauce"], 55);

print(pizza.contents());
print(pasta.contents());