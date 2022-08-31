class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())

#MRO nos muestra el orden de las clases de las que hereda

print(F.mro())

""" 

class A:
    pass

class B(A):
    pass

class C(B):
    pass


c = C()
print(c.a())
#Error. c no tiene ningun metodo a()
 """
""" 
a = 5
class A:
      a = 7
      pass

class B(A):
      pass

class C(B):
      pass

c = C()
print(c.a())
 """

bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)