#global scope
my_global = 10; #this variable can be accessed from any parts of our code.

def fn1():
      #enclosed scope (function) enclosed_v only exists inside the function or the functions inside our primary function (fn1)
      enclosed_v = 8 
      print(local_v) #This will return an error. local_v is a local variable inside fn2.
      
      #local scope (function) local_v only exists inside the function (fn2) where is declared
      def fn2():
          local_v = 5;
          print(enclosed_v); #This is ok
      fn2();
fn1();

""" print(enclosed_v); """ #This will thrown an error, because we're trying to access a enclosed variable of fn1 on global scope.
""" print(local_v)""" #This will thrown an error, because we're trying to access a local variable of fn2 on global scope.

#Conclusion - The variables that are inside something, are local to that. If there is a parent, the parent variables will work in the child one.

