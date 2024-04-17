tp = ('a','b','c');

# some time we work with itreators and we also need to keep a count of itreation 
# to slove this python provide enumrate
x = enumerate(tp)
# print(x) # <enumerate object at 0x000001AA2F3F20C0>
x_list = list(x) # [(0, 'a'), (1, 'b'), (2, 'c')]
# print(x_list)

# Working with python
# file = open('test.py') # raise 100 % ERROR 
# file = open('test.txt', 'w+')  # This line creates the file
# print(file)

#  good but not a professional and may create issues

file = open("test.py",'w');

# try:
#     file.write('print("Hello world")');
# finally:
#     file.close()

# new way even consie

with open("test.py",'w') as file:
    file.write('print("Hello world")')
    
#  now no need to explicitly close


