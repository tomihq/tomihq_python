#Step 1: Create the class.
class MyClass:
    a = 5;
    print("Hello from MyClass");
    def hello(self): #Use self to prepare the function to be used in the initialized instance.
        return "Hello world, your number is: " +str(self.a)
    pass ##Python allow us to use this when we don't want to write nothing yet and don't get an error.

#Step 2: Creating a new instance of the class.
#Step 3: Initializing a new instance of the class.
myclass = MyClass();
print(myclass.hello());
