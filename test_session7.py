import pytest
import os
import inspect
import re
from session7 import docstring
from session7 import fibonacci
from session7 import add1,mult1,div1
from session7 import add2,mult2,div2
import session7
import test_session7

README_CONTENT_CHECK_FOR=['docstring', 'fibonacci', 'func_counter', 'func_counter_dict', 'closure']
#defining a few parameters to test docstring

def func1(name:"str" = "Name"):
    ''' This function takes one positional arguments.
        positional argument is name and is of type string.
        the function returns the name.
    '''
    return name

def func2():
    """ This function takes zero positonal arguments"""
    pass

func3 = "function3"
freevar = ('count',) #free variables of docstring

######----------Tests for docstring------######

def test_if_count_is_free_variable():
    """ This function checks if count is a free variable or not"""
    assert docstring.__code__.co_freevars == freevar, 'count was expected to have a free variable'
    
def test_if_docstring_is_a_closure():
    """This function checks if docstring is a closure"""
    assert isinstance(docstring.__closure__,tuple) == True, "the docstring defined is not a closure!!!!!"
    
def test_docstring_with_correct_input():
    """ This function tests the docstring function with func1"""
    assert docstring(func1) == True, "docstring not working as expected"
    
def test_docstring_with_wrong_input():
    """ This function tests the docstring function with func2"""
    assert docstring(func2) == False, "docstring not working as expected"
    
def test_docstring_with_improper_input():
    """This function tests with func3 variable as input"""
    
    with pytest.raises(TypeError,match = r".*Inappropriate INPUT*"):
        docstring(func3)



#####----------Tests for fibonacci------------#########

def test_if_fibonacci_is_a_closure():
    """This function checks if fibonacci is a closure"""
    assert isinstance(fibonacci.__closure__, tuple) == True, "the fibonacci defined is not a closure!!!!"
    
def test_output_of_fibonacci():
    """This function tests the output of fibonacci"""
    
    output = []
    for i in range(10):
        output.append(fibonacci())
    assert output == [0,1,1,2,3,5,8,13,21,34],"the fibonacci is not correctly defined"



######----------Tests for func_counter------------########
free_var = ('count', 'fn') #free variables of func_counter
   
def test_if_func_counter_is_a_closure():
    """This function checks if func_counter is a closure"""
    
    assert isinstance(add1.__closure__, tuple) == True, "the func_counter is not a closure"
    assert isinstance(mult1.__closure__, tuple) ==True, "the func_counter is not a closure"
    assert isinstance(div1.__closure__,tuple) == True, "the func_counter is not a closure"
    
    
def test_dictionary_is_global():
    """This funtion tests if the dicitonary used to update is a global dictionary"""
    
    
    if 'count_dict' in free_var:
        assert "not using a global dictionary"
      
def test_free_var_of_func_counter():
    """This funciton checks the free variables of func_counter"""
    
    assert add1.__code__.co_freevars == free_var, " the free variables are not defined"
    assert mult1.__code__.co_freevars == free_var, " the free variables are not defined"
    assert div1.__code__.co_freevars == free_var, " the free variables are not defined"
    
    
def test_add1():
    """This function tests the add1 closure of func_counter"""
    
    assert add1(1,2) == 3, "messing the simple add function"
    assert add1(7,2) == 9, "messing the simple add function"
    assert add1(1,5) == 6, "messing the simple add function"
    assert add1(1,12) == 13, "messing the simple add function"
    
    #testing the add key in global dictionary
    assert session7.count_dict['add'] == 4, "not updating the global dictionary!!!!!"
    
def test_mult1():
    """This function tests the mult1 closure of func_counter"""
    
    assert mult1(1,2) == 2, "messing the simple multiply function"
    assert mult1(7,2) == 14, "messing the simple multiply function"
    assert mult1(1,5) == 5, "messing the simple multiply function"
    
    #testing the mult key in global dictionary
    assert session7.count_dict['mult'] == 3, "not updating the global dictionary!!!!!"
    
def test_div1():
    """This function tests the div1 closure of func_counter"""
    
    assert div1(6,2) == 3, "messing the simple division function"
    assert div1(18,2) == 9, "messing the simple division function"
    assert div1(5,1) == 5, "messing the simple division function"
    
    #testing the div key in global dictionary
    assert session7.count_dict['div'] == 3, "not updating the global dictionary!!!!!"
    
    
def test_global_dictionary():
    """This function tests the global dicitonary{count_dict} """
    
    assert session7.count_dict == {'add':4, 'mult':3, 'div':3}, "global dicitonary not upadted as expected"
    
    



##########-------------Tests for func_counter_dict-----------#######
free_var_2 = ('count_var', 'dictionary', 'fn') #free variables of func_counter_dict

def test_func_counter_dict_is_a_closure():
    """This function checks if func_counter_dict is a closure"""
    
    assert isinstance(add2.__closure__, tuple) == True, "the func_counter_dict is not a closure"
    assert isinstance(mult2.__closure__, tuple) ==True, "the func_counter_dict is not a closure"
    assert isinstance(div2.__closure__,tuple) == True, "the func_counter_dict is not a closure"

def test_if_the_dictionary_is_not_global():    
    """This funciton tests if the count is updated in different dictionary and not in global dictionary"""
    
    if not('dictionary' in free_var_2):
        assert "the dictionary used to updated here is a global dicitonary"
    
def test_free_var_of_func_counter_dict():
    """This funciton checks the free variables of func_counter_dict"""
    
    assert add2.__code__.co_freevars == free_var_2, " the free variables are not defined"
    assert mult2.__code__.co_freevars == free_var_2, " the free variables are not defined"
    assert div2.__code__.co_freevars == free_var_2, " the free variables are not defined"   
    
    
    
def test_add2():
    """This function tests the add2 closure of func_counter_dict"""
    
    assert add2(1,2) == 3, "messing the simple add function"
    assert add2(7,2) == 9, "messing the simple add function"
    assert add2(1,5) == 6, "messing the simple add function"
    assert add2(1,12) == 13, "messing the simple add function"
    
    #testing the add key in addition dictionary
    assert session7.addition['add'] == 4, "not updating the addition dictionary!!!!!"
    
    
def test_mult2():
    """This function tests the mult2 closure of func_counter_dict"""
    
    assert mult2(1,2) == 2, "messing the simple multiply function"
    assert mult2(7,2) == 14, "messing the simple multiply function"
    assert mult2(1,5) == 5, "messing the simple multiply function"
    
    #testing the mult key in mulltiplication dictionary
    assert session7.mulltiplication['mult'] == 3, "not updating the mulltiplication dictionary!!!!!"
    
    
    
def test_div2():
    """This function tests the div2 closure of func_counter_dict"""
    
    assert div2(6,2) == 3, "messing the simple division function"
    assert div2(18,2) == 9, "messing the simple division function"
    assert div2(5,1) == 5, "messing the simple division function"
    
    #testing the div key in division dictionary
    assert session7.division['div'] == 3, "not updating the division dictionary!!!!!"
    
    

#######-----------General tests-----------###########


def test_session7_readme_exists():
    """ Checks if README file exists"""
    assert os.path.isfile("README.md"), "README.md file missing!"
    
def test_session7_readme_500_words():
    """ Checks if README file has a minimum of 500 words"""
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session7_readme_proper_description():
    """ Checks if README file has description of all the functions/classes."""
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/classes well in your README.md file"
    
def test_session7_readme_file_for_more_than_10_hashes():
    """Checks if README file has proper formatting (minimum of 10 hashes)"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
    
    
def test_session7_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
    """
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"
        
        
def test_session7_function_name_had_cap_letter():
    """ test fails if Capital letter(s) used for function names """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
        
def test_function_count():
    """ tests number of test function > 20 in test_poker file"""
    functions =inspect.getmembers(test_session7, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'
    
    
def test_function_repeatations():
    """ tests if any repeated tests in test_poker file"""
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'