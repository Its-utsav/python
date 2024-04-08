# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.
# def square(n):
#     return n ** 2;

# print(square(3))

# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.

# def sum_of_two(a,b):
#     return a + b;

# print(sum_of_two(1,2))


# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# def multiply(a,b):
#     return a * b;

# print(multiply(1,2))
# print(multiply(4,'2'))


# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
from math import pi

# def circle_stats(r) -> float:
#     area = pi * r ** 2;
#     circumference = 2 * pi * r
    
#     return area,circumference;
    
# [a,c] = circle_stats(12)
# print(round(a,2),c);
# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

# def print_name(name="python"):
#     return f' Hello {name} 😎';
    
# print(print_name("utsav"))

# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

# def cube(x):
#     return x**3

# ans = lambda x: x ** 3;
# # lambda function use only one time use
# print(ans(2))

# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# def sum_all(*arg): # palceholder anything but '*' is require
#     print(type(arg))
#     return sum(arg);

# print(sum_all(1,2,3))


# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def lol(**kwargs):
#     for key,val in kwargs.items():
#         print(key,val);
        

# lol(name="utsav",age=12)



# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even_gen(limit):
#     for i in range(2,limit+1,2):
#         yield i # return value and keep in mempry
    
    
# for i in even_gen(10):
#     print(i)

# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.


# def fact(n:int) -> int:
#     if n == 1 or n == 0 : return 1;
#     else: return n * fact(n-1);
    
# print(fact(5))




