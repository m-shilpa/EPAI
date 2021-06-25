# Scopes and Closures

## Scopes:
The area in which a variable is accessible is called **scope**
There are different types of scopes. They are:
1. Built-in Scope
2. Global Scope
3. Local Scope
4. Non Local Scope

## Closures
Closures are functions which have free variables attached to them.

## Assignment
The functions mentioned below can be found <a href="https://github.com/m-shilpa/EPAI/blob/main/Session%207%20-%20%20Scopes%20and%20Closures/assignment.py">here</a>

### Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable.

**Solution:**

  * The function **check_docstring** contains two closures:
    1. **check_docstring_exists** - This function accepts a function as argument and checks if that function contains docstring or not. It returns a boolean value with True if the docstring exists else returns False.
    2. **check_docstring_length** - This function accepts a function as argument. It first checks if the docstring is present in the function that needs to be checked. If so, then it checks if the length of the docstring is greater than 50 or not. 
       Finally it prints the result. 
  
### Write a closure that gives you the next Fibonacci number.

**Solution:**

  * The function **fibonacci** helps in generating the next fibonacci number in the sequence. 
  * It contains the closure **next_fibonacci_number** which generates and stores the next fibonacci number, each time the function is called. 
  

### Write a closure that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts.

**Solution:**

  * The function **counter** is used to keep track of the number of times the given function was called. 
  * The closure **inc_counter** is used to increment the count of the number of times the function called, each time the function is called.


### Modify above such that now we can pass in different dictionary variables to update different dictionaries  

**Solution:**

  * A slight modification is done to the previous **counter** function to accept a dictionary as one of the arguments. This implementation can be seen in the function **counter1**.

