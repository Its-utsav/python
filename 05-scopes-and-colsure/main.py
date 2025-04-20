# name = "python" # direcr memory allocate
# # global variable
# # everything ok thill python scopes

# def print_name():
#     name = "LOL";
# print(f'coluser {name}')

#  now both name variable are deffirent from each other , it may be co-insidence that both 'python' and "LOL" have same variable name

# but anywork on print_name function that may affect name variable NOTE name variable that is declare in function will affect not a gloal var

name = "react"


# print(f"print from global scope 1. {name}")
def print_name():
    name = "next"


# print(f'print from function {name}');

# print_name()
# print(f"print from global scope 2. {name}")


a = 12


def fun(b):
    c = a + b
    return c


# ans = fun(12);

# print(ans)


def fun2():
    global a
    a = 1000  # don't change the value of global variables NOT GOOD


# fun2()
# print(f' now a is {a}')


x = 1


def f1():
    # x = 12000; # if this statement is comment then x value will be 1(global scope)
    x = 12000

    def f2():
        print(x)

    return f2  # function f2 references return to the f1 function


ans = f1()
# ans()

# f1 called than
# 1. x = 12000 then f2 return
# 2. f2 called f2 print x var so it will be use x that is i f1 function scope (since f1 return the f2 function referense so we need to call that fucntion ans var)
x = 3


def any_task(n):
    def act(x) -> int:
        return x**n

    return act


ans1 = any_task(2)
ans2 = any_task(3)

print(ans1(3))
print(ans2(3))

# def any_task(2):
#     def act(3)->int:
#         return 3 ** 2;  # 9
#     return act;

# def any_task(3):
#     def act(3)->int:
#         return 3 ** 3;  # 27 3x3x3
#     return act;
