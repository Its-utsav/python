# what is decorator :
#  a function that take argument as function and return that function with modified version of function
 
# def add_msg(func):
#     def wrapper():
#         print("before calling the function");
#         func();
#         print(f"i think function name is {func.__name__}")
#         print("after calling the function");
#     return wrapper;


# # simple function
# def hello():
#     print("Hello world")
        
# @add_msg
# def hello2():
#     print("Hello World x 2");
    
# # hello()
# hello2()

# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         ans = func(*args,**kwargs)
#         end = time.time();
#         print(f'function {func.__name__} ran in {end-start}');
#         return ans
#     return wrapper

# @timer
# def ex_fun(n):
#     time.sleep(n);
    
    
# ex_fun(2);
# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args);
        kwargs_value = ', '.join(f'{k} : {v}' for k,v in kwargs.items())
        print(f'function name {func.__name__} arguments {args_value} keywords argument {kwargs_value} ')
        return func(*args,**kwargs);
    
    return wrapper;

@debug
def greet(name,greeting = "hello"):
    print(f'{name} , {greeting}')
    

greet("python",greeting='hello ji')




# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.