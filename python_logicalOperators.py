
#Logical operators

a = True; 
b = True; 

if a and b: 
    print ("Ambos son true");

a = True; 
b = False; 

if a or b: 
 """    print("Uno de los dos es true"); """

a = False; 
b = False;

if not(a) and not(b): 
   """  print ("a es true y b es true porque estan siendo negados !a !b") """


#Control flow
#Conditionals

bill_total = 50;
discount = 20;

""" if bill_total>=150:
    print("It's expensive");
elif bill_total>=100 and  bill_total<150 :
    print("It's 50% cheap!")
else: 
    print ("It's 100% cheap"); """

bill_total -= discount;
""" print("Total bill with discount:" + str(bill_total)) """
