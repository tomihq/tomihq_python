def sum_of(a, b):
    return a + b;

""" print(sum_of(10, 20, 30))  """ #This will throw an error

#How we can fix this? Using args. It's like an "spread" in JavaScript. We storage all the data in only one variable, and iterate it to manipulate.

#Using args - Use args if you have ONLY STRING, INTEGER but NO sets or objects. 

def sum_of2(*args):
    sum = 0;
    for x in args: #If we use args, we only use x (have each of the elements proporcionated by params)
        sum += x;
    return sum;

#All will work!
print(sum_of2(10, 20, 30))
print(sum_of2(10, 20, 40, 50, 60))
print(sum_of2(10, 20, 40, 40, 40, 40))
print(sum_of2(10, 20, 1, 2, 3, 4, 5))

