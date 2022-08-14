#Casting

user_num_1 = "5"
user_num_2 = "5"
user_sum = user_num_1 + user_num_2
print(user_sum) # El resultado será 55

#Casting print errors
""" 
num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum) #El resultado de esto dará error, porque en un print solamente se pueden concatenar con el + strings """

#Solution to the problem ahead

""" num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
print("The sum of: " + str(num_1) + " and " + str(num_2) + " is " + str(user_sum)) """ #El resultado de esto dará error, porque en un print solamente se pueden concatenar con el + strings
