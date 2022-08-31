#Simple inheritance
class Employees:
    def __init__(self, name, last) -> None:
        self.name = name;
        self.last = last;
        pass

#Inheritance
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        #We're initializing name, last from the parent class.
        super().__init__(name, last)
        #We're creating a local Supervisors variable.
        self.password = password;

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " +str(days) + " days";

adrian = Supervisors("Adrian", "A", "apple");
emily = Chefs("Emily", "E");
juno = Chefs("Juno", "J");

print(emily.leave_request(3));
print(adrian.password);
print(emily.name);

#Multiple Inheritance - A child can access father, and mother variables.

class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

#Multi-Level inheritance - When we have a parent, then a child, and the child has another child. The last child can have access to his father and grandfather variables/functions.

class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass
a = A();
c = C()
print(c.a)

#This will return true because C parent is B.
print(issubclass(C, B));

#This will return true because c is an instance of C.
print(isinstance(c, C));

#This will return true. Because c is an instance of C, C father is B and B is an instance of A.
print(isinstance(c, A));

#This will return false. Because a instance of A is father of B and C.
print(isinstance(a, C));

