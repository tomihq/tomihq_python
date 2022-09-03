import addition;
import pytest;

#Return true if test passes.
def test_add():
    assert addition.add(4, 5) == 9

#Return true if test passes
def test_sub():
    assert addition.sub(4, 5) == -1

#Pass the test - Will return true
def test_add():
    pass

#Test failed - 
def test_mul():
    assert False;

#Test success - 
def test_add():
    assert True;
    #Below code will be ignored
    assert addition.div(10, 5) == 2

