import pytest;
import spellcheck;

# Variables to be tested

#Success
alpha = "Checking the length & structure of the sentence."

#Error (lastChar isn't ".")
alpha2 = "Checking the length & structure of the sentence"

#Error. Words are fewer than 10
beta = "This sentence should fail the test."


@pytest.fixture
def input_value():
    #input = alpha
    input = beta
    return input

# First test function test_length()
def test_length(input_value):
    assert spellcheck.word_count(input_value)<10
    assert spellcheck.char_count(input_value)<50



# Second test function test_struc()
def test_struc(input_value):
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value)=="."



# Run these tests with `python3 -m pytest test_spellcheck.py`