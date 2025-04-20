# string:str = "utsav";
# # print(string[1]) # print at give index
# # print(string.center(10,'-')) # center the string with length 1 para is width length and sceond is fillchar
# # print(string.count('t',0,2 )) #found given substrig in string also include string, ending index (optional)

# # name = ['u','t','s','a','v'];
# # print(''.join(name)) # used for join itreable (list,tuple) into single string
# # print(len(string)) # give length of the given string
# # print(max(string));
# # print(min(string))
# #  give max and min value as per ASCII value
# # print(string.replace('a','@',1)); # it repalce old substring with new substring , with specfic count(optional)

# # print(string.lower()) # convert and return string into lower case
# # print(string.upper()) # convert and return string into upper case

# # string = "Utsav Kumar Dhimmar ";
# # print(string.split(' ')) # convert string into list as per specice spearator with opinally maxsplit value


# print(2**2);
# print(pow(2,2));
# if 2**2 == pow(2,2):
# print(True);
# print(2**3)  # 2 * 2 * 2


# a = [1,2,3];
# b = [1,2,3];
# c = a;

# identity operators
# print(a is c); # True
# print(c is a); # True
# print(a is not c) # False
# print(a == b) #  True

# membership operator

# print('1' in a); # False because 1 string is not in a
# print('1'not in a and 1 in a)


# lst:list = [1,2,3,4,5];
# lst2:list = [5,6,7,8,9,10];

# # lst.append('test') # add element at last with no return value(None)
# # print(lst)
# # lst.clear() # clear all element from the list with no return value

# # copy_lst = lst;
# # lst[1]  = 'one';
# # # copy_lst[2]= 'two'
# # print(copy_lst)
# # lst.append(lst2)
# # print(lst)

# # cpy_lst = lst.copy() #create a shallow copy
# # cpy_lst[1] = 'one'
# # print(cpy_lst)

# # print(lst.count(2)); # given how many time element occure in given list
# # print(lst.index(4)); # give the index number of given parameter , optionlly support start index(0) and stop index(till end)

# # lst.insert(1,'one'); # add element at spefice index with no return value


# # print(lst.pop()) # remove and return last element from list

# # lst.remove(2) # remove first occurence of given element

# # lst.reverse() # reverse the given list with no return value

# lst = [4,2,51,1]
# # lst.sort() # sort in acending oredr
# # lst.sort(reverse=True) # sort in deceinding order

# print(lst)

# tp  = (1,2,3);
# print(tp[1])
# tuple are same as list but it can't be change after decalred
# print(tp.count(1)) # give how many time particular element occure
# print(tp.index(1)) # give index of an given element
# tp2 = (2,3,4);
# tp3 = tp + tp2 # add element

# print(tp3)

# set are unique and unorder
# set1:set = {1,2,3,4,4};
# set1.add(12); # add only one element at last can't add list , set or any other thing

# set2 = {4,5,6}
# set3 = set1 | set2; # union
# set3 = set1.union(set2) #union
# set3 = set1 & set2 == set1.intersection(set2) # both are same


# set1.clear()
# print(set1) # give set()

# set3 = set1.copy()
# print(set3); # create a shallow copy

# set1.discard('1') # remove the element from set if given element not exit in set than don't raised error but with remove raised error
# set1.remove('1'); # raised KeyError
# set1.pop(); # remove and return last element from the set
# print(set1.union(set2)) #update the set and return new set with updated value

# dict
# key:value pair

me = {
    "name": "Utsav",
    "age": 17,
    "marks": [1, 2, 3, 4],
    "isAdult": False,
}


# adding new item(field)

me["isStudent"] = True
me["marks"] = 100  # changing the value
# remove element from dict

# del me["isAdult"]
# me.pop('isAdult')
# removing specifice element

# me.popitem() # remving last key

# methods

# print(me.get('age')) # accessing data from given parameter
# me.clear() # return {}

# me.copy() # create a shallow copy

# NumPy
import numpy as np
# mean avg

# lst = [1,2,3];
# arr = np.array([1,2,3,1])

# print(np.mean(arr)) # give avarge

# middle value
# print(np.median(arr))
# frequency of an number -> not exit in numpy ,use scipy.stats

# from scipy import stats
# print(stats.mode(arr))
# Standard Deviation

# print(np.std(arr))

# Variance
# print(np.var(arr))

# Pandas

import pandas as pd
# dataframe from list
# data = [
#     ['utsav',17,True],
#     ['harray',20,False],
#     ['hevin',23,False]
# ]

# df = pd.DataFrame(data,columns=['name','age','isStudent']);

# data ={
#     'name':['utsav','mark','harray'],
#     'age' :[17,23,30],
#     'isStudent' : [True,False,False]
# }

# lable = ['name','age','isStudent']

# df  = pd.DataFrame(data,columns=lable);

# print(df)
# data = pd.read_csv('data.csv') # this file save As .csv

# print(data)

data = {
    "name": ["utsav", "mark", "harray"],
    "age": [17, 23, 30],
    "isStudent": [True, False, False],
}

lable = ["name", "age", "isStudent"]

df = pd.DataFrame(data)  # create a DataFreame on whole data
# df = pd.DataFrame(data['name']) #create a DataFrame on given column

# print(df.loc[0]) # print at 0 index data
# print(df.loc[0:2]) # print 0,1,2 index data
# d1 = df.iloc[0] # at 0 index

d1 = df.iloc[[0, 1]]  # ai 0,1 index
# d1 = df.iloc[:,[0,1]] # all data and 0,1 column
# d1 = df.iloc[1,[0,1]] # data on first column and column index 0 and 1

print(d1)
