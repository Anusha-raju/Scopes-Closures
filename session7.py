from inspect import isfunction
#####----------Question 1---------#####


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
docstring = docstring()


#####--------Question 2---------#####
def fibonacci():
    """ This is a closure which calculates the next fibonacci number"""
    f,s = 0,1 # initial values of a fibonacci series
    def next(): # this function prints the next fibonacci number
        nonlocal f,s
        number = f
        f,s = s,f+s # calculates the next fibonacci number
        return number
    return next

fibonacci = fibonacci()


#####---------Question 3----------########
def add(*args):
    """ This function adds the arguments passed."""
    return sum(args)


def mult(*args):
    """ This function multiplies the arguments passed."""
    answer = 1
    for i in args:
        answer = answer * i
    return answer #returns the product

def div(a,b):
    """ This function divides a by b"""
    if b == 0:
        raise ValueError(" Zero division not possible!!!")
    else:
        return a/b


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



add1 = func_counter(add) #add function with counter using a global dictionary
mult1 = func_counter(mult) #mult function with counter using a global dictionary
div1 = func_counter(div) #div function with counter using a global dictionary



######---------Question 4----------########

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


#defining various dictionaries
addition = dict()
mulltiplication = dict()
division = dict()



add2 = func_counter_dict(add , addition) #add function with counter using a addition dictionary
mult2 = func_counter_dict(mult , mulltiplication) #add function with counter using a multiplication dictionary
div2 = func_counter_dict(div ,division) #add function with counter using a division dictionary
