#Looping

listOfFavoriteFood = ["Fusilli", "Ravioli", "Hamburguer", "Sandwich"];

#Having index
""" for food in enumerate(listOfFavoriteFood, start = 1):
    print(food); """

""" #Having index manual
for idx, food in enumerate(listOfFavoriteFood):
    print("Comida numero: " + str(idx+1) + " es: " +food);  """

#No index
""" for food in listOfFavoriteFood:
    print(food); """

#Looping each times 

""" for i in range(10):
    print(i);

     """

count = 0;

""" while count<len(listOfFavoriteFood):
    print(listOfFavoriteFood[count])
    count+=1 """


