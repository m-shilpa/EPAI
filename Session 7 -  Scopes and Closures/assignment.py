""" Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable """

def check_docstring():
  
  """  Function to check if docstring exists and length of docstring is greater than 50  """

  length=50

  def check_docstring_exists(fn):

    """ Function to check if the function has a docstring. If so, then the function returns True else returns False """
    
    if fn.__doc__:
      return True
    else:
      return False

  def check_docstring_length(fn):

    """ Function to check if the length of the docstring is greater than or equal to the set length  """
     
    if check_docstring_exists(fn):

      if len(fn.__doc__.strip()) > length:
        print("Docstring length is > 50 ")
      else:
        print("Docstring length is <= 50 ")

    else:
      print('Function does not have a docstring')
      
  return check_docstring_length

   
  """ Write a closure that gives you the next Fibonacci number """


def fibonacci():
  """ 
  Function to generate the next fibonacci number   
  """

  fib_seq = (0,1)
  counter = 0

  def next_fibonacci_number():
    """ 
    Function to print the next fibonacci number 
    Logic: A tuple is used to store the last two fibonacci numbers. 
           Sum of the tuple generates the next fibonacci number
           Everytime the next fibonacci number is generated, it is stored in the tuple along with the previous number and the cycle continues.
    """
    
    nonlocal fib_seq
    nonlocal counter

    # counter is used to print the first 2 fibonnaci numbers 0, 1

    if counter <=1:
      print(counter)
      counter+=1
    else:
      next = sum(fib_seq)
      fib_seq = (fib_seq[-1], next)
      print(next)
  return next_fibonacci_number


""" Write a closure that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts """

cnt = dict()

def add(num1,num2):
  """ Function to add two numbers """

  return num1 + num2

def mul(num1,num2):
  """ Function to multiply two numbers """

  return num1 * num2

def div(num1,num2):
  """ Function to divide two numbers """

  if num2==0:
    return 0
  else:
    return num1 / num2


def counter(fn):
  """ Function to keep track of the number of times the given function was called. """

  counter = 0

  def inc_counter(*args,**kwargs):
    """ Function that increments the counter and stores in a dictionary each time the given function is called. """

    global cnt
    nonlocal counter
    counter +=1
    cnt[fn.__name__] = counter
    return fn(*args,**kwargs)
  return inc_counter


""" Modify above such that now we can pass in different dictionary variables to update different dictionaries"""

def counter1(fn,conter_dict):
  """ Function to keep track of the number of times the given function was called. """
  
  counter = 0

  def inc_counter(*args,**kwargs):
    """ Function that increments the counter and stores the result in the dictionary passed in arguments, each time the given function is called. """
    
    nonlocal counter
    counter +=1
    conter_dict[fn.__name__] = counter
    return fn(*args,**kwargs)
  return inc_counter
