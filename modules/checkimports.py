import sys;

sys.path.insert(1, r'F:\YO\Conocimiento\Meta\Python\modules\Workplace');
import trial;

print(trial.names);

#Importing all the module when we need only one function. Uses more memory.
""" import math """

#From math module import the function sqrt only.
from math import sqrt;

root = sqrt(9);
print(int(root))

#Importing math module using alias
import math as m;

root = m.sqrt(9);
print(root);

#Importing function from module using alias
from math import factorial as f

factorial = f(10);
print(factorial)

#Import multiple functions of a module.
from math import factorial, log10, sqrt;

x = log10(50); 
print(x)

#Importing all the functions from a module and using these without mention package name.
from math import *
x = log10(50)
print(x)

