#This will return an error because function is not defined now.
""" print ('Total tax', calculate_tax(bill, tax_rate));

def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100;
 """

#This will work

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100);

print ('Total tax', calculate_tax(175.00, 15));