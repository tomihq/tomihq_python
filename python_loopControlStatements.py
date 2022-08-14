#Break - Loop Control Statements - Cuando se cumple x condicion, termina la ejecucion de todo el loop.
""" for idx, food in enumerate(listOfFavoriteFood):
    if food == 'Fusilli':
        print("Se ha encontrado Fusilli");
        break; """

#Continue - Cuando se cumple x condicion, termina la ejecucion en ese indice y vuelve a ejecutar el loop con el siguien elemento.
""" for idx, food in enumerate(listOfFavoriteFood):
    if food == 'Fusilli':
        print("Se ha encontrado Fusilli");
        continue;
    print(food + " no pasa por continue");
 """
#Pass - Sirve para hacer algo cuando es exclusivo, pero despues que siga haciendo lo demas.

""" for idx, food in enumerate(listOfFavoriteFood):
    if food == 'Fusilli':
        print("Se ha encontrado Fusilli, se le descontarán 200 pesos");
        pass;
    print(food);
 """