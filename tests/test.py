""" def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11) """
""" 
11
8
5
2 """

#Linear time - Tiene un solo ciclo.

""" def bigo(numbers):
    for i in numbers:
        print(numbers)

bigo([1, 7, 13, 19]) """


#Identation error
""" str = 'Pomodoro'
for l in str:
if l == 'o':
    str = str.split()
    print(str, end=", ") """


#1) Ejecuta d, color en d es green.
#2) Ejecuta e, color en e es yellow. Modifica al global de d porque esta refiriendose a la variable nonlocal(global de su padre) color.
#3) Muestra amarillo (porque lo modifico e)
#4) Cambia color a rojo.
""" def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d() """

num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

#Retorna 10.
cost_evaluation(num)
#Instancia el auto.
car = Car()
bike = Bike()
#Modifica el num de 5 a 7 en el auto.
car.num = 7
#No hace nada. Esta refiriendose a algo estatico.
Car.num = 2
#Muestra el numero global. Retorna 9.
print(num)

#¿Cual es la correcta que retornará true si hay una clase PRINCIPAL P con un objeto p y una SUBCLASE hija llamada C con un objeto c? 

#C P


class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
#Entra primero a C, no hace nada, luego pasa a A (Function inside A) y luego termina porque pedimos ejecutar de d el padre a() y ejecuta su self.
print(d.a())

