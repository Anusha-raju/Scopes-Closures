# Session 7

## TOPIC: Scopes & Closures





#### ***ASSIGNMENT***

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) 
2. Write a closure that gives you the next Fibonacci number (+ 2 tests) 
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) 
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) 





#### ***Solution:***



1]  docstring is a closure which counts the length of docstring in the input function

```python
def docstring():
    """ This a closure which counts the length of the docstring"""
    count = 0 # this is free variable which keeps the count of characters in docstring of the function
    def counter(fn):
        ''' This function counts the characters in 'fn':function and prints relavent message.
        INPUT: fn : Function
        OUTPUT: RELEVANT message regarding the length of docstring
        '''
        if not isfunction(fn):
            raise TypeError("Inappropriate INPUT:please send in a function")
        nonlocal count
        count = len(fn.__doc__)
        if count > 50:
            return True
        else:
            return False
    return counter
```



***Test Cases:***

|              Function              |                        Functionality                         |
| :--------------------------------: | :----------------------------------------------------------: |
|   test_if_count_is_free_variable   |   this function checks if count is a free variable or not    |
|   test_if_docstring_is_a_closure   |        This function checks if docstring is a closure        |
| test_docstring_with_correct_input  | This function tests the docstring function with func1(right input) |
|  test_docstring_with_wrong_input   | This function tests the docstring function with func2(wrong input) |
| test_docstring_with_improper_input |       This function tests with func3 variable as input       |





2]

 FIBONACCI numbers: The **Fibonacci sequence** is a series of numbers where a number is the addition of the last two numbers, starting with 0, and 1. The **Fibonacci Sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

fibonacci returns a function which when called returns the next fibonacci number 

```pyhton
def fibonacci():
    """ This is a closure which calculates the next fibonacci number"""
    f,s = 0,1 # initial values of a fibonacci series
    def next(): # this function prints the next fibonacci number
        nonlocal f,s
        number = f
        f,s = s,f+s # calculates the next fibonacci number
        return number
    return next
```





***Test Cases:***

|            Function            |                 Functionality                  |
| :----------------------------: | :--------------------------------------------: |
| test_if_fibonacci_is_a_closure | This function checks if fibonacci is a closure |
|    test_output_of_fibonacci    |  This function tests the output of fibonacci   |



3]

func_counter is a closure which counts the number of times a function is called and stores the count in a global dictionary.

```
count_dict = dict() #global dictionary
def func_counter(fn):
    ''' This is a closure which counts the number of times a function: fn
        is called and stores the count in a global dictionary
        INPUT: fn : Function
        OUTPUT: returns the function: fn
    '''
    count = 0
    def function_counter(*args, **kwargs):
        nonlocal count
        if not isfunction(fn):
            raise TypeError("please send in a function")
        count += 1
        count_dict[fn.__name__] = count
        return fn(*args, **kwargs)
    return function_counter
```





***Test Cases:***

|             Function              |                        Functionality                         |
| :-------------------------------: | :----------------------------------------------------------: |
| test_if_func_counter_is_a_closure |      This function checks if func_counter is a closure       |
|     test_dictionary_is_global     | This funtion tests if the dicitonary used to update is a global dictionary |
|   test_free_var_of_func_counter   |   This funciton checks the free variables of func_counter    |
|             test_add1             |     This function tests the add1 closure of func_counter     |
|            test_mult1             |    This function tests the mult1 closure of func_counter     |
|             test_div1             |     This function tests the div1 closure of func_counter     |
|      test_global_dictionary       |    This function tests the global dicitonary{count_dict}     |





4] func_counter_dict is a closure which counts the number of times a function is called and stores the count in a dictionary.

```python
def func_counter_dict(fn:'Function' , dictionary:'dict'):
    ''' This is a closure which counts the number of times a function: fn
        is called and stores the count in a dictionary.
        INPUT:  fn: Function
                dictionary: dict
        OUTPUT: returns the function: fn
    '''
    count_var = 0
    def counter_1_dict(*args, **kwargs):
        nonlocal count_var
        if isinstance(dictionary, dict) and isfunction(fn):
            count_var += 1
            dictionary[fn.__name__] = count_var
        else:
            raise TypeError("Please enter a dictionary type variable and send in a function")
        return fn(*args, **kwargs)
    return counter_1_dict
```





***Test Cases:***

|               Function               |                        Functionality                         |
| :----------------------------------: | :----------------------------------------------------------: |
| test_func_counter_dict_is_a_closure  |    This function checks if func_counter_dict is a closure    |
| test_if_the_dictionary_is_not_global | This funciton tests if the count is updated in different dictionary and not in global dictionary |
|  test_free_var_of_func_counter_dict  | This funciton checks the free variables of func_counter_dict |
|              test_add2               |  This function tests the add2 closure of func_counter_dict   |
|              test_mult2              |  This function tests the mult2 closure of func_counter_dict  |
|              test_div2               |  This function tests the div2 closure of func_counter_dict   |





