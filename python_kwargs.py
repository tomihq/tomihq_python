#Using args - Use kwargs if you have ONLY STRING, INTEGER but NO sets or objects. 

def sum_of(**kwargs):
    sum = 0;
    for k, v in kwargs.items():               
        sum += v;
    return round(sum, 2);

    #If we use args, we only use x (have each of the elements proporcionated by params). k will have coffee, cake and juice. v will have 2.99, 4.55 and juice 2.99

#All will work!
print(sum_of(coffee=2.99, cake=4.55, juice=2.99))
