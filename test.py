# import numpy as np
# import pandas as pd



# exam_data = {
#     'name': ['Rinkesh', 'Aditi', 'Sonu', 'Anishka', 'Hiren', 'Raj', 'Hiren', 'Dev', 'Lalu', 'Jay'],
#     'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#     'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#     'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
# }
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];

# df = pd.DataFrame(exam_data,index=labels);

# print(df.iloc[:3])
# print(df[['name','score']])



# import pandas as pd

# data = pd.read_csv("data.csv");


# df = pd.DataFrame(data);

# print(df)

# 3. Write a Pandas program to create and display a DataFrame from a specified dictionary 
# data which has the index labels and perform following operations. 
# import numpy as np
# import pandas as pd

# exam_data = {
#     'name': ['Rinkesh', 'Aditi', 'Sonu', 'Anishka', 'Hiren', 'Raj', 'Hiren', 'Dev', 'Lalu', 'Jay'], 
#     'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
#     'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
#     'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
#     }

 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
# df = pd.DataFrame(exam_data,index=labels);

# # 1. Get the first 3 rows of above dataframe.
# top_3 = df.head(3);
# # print(top_3)  
# # 2. Select the 'name' and 'score' columns from above dataframe.  
# # print(df[['name','score']])

# # 3. Sort the dataframe first by 'name' in descending order. 

# sort_data = df.sort_values(by='name',ascending=True);
# # print(sort_data)

# # 4. Sort 'score' in ascending order. 


# sort_score = df.sort_values(by='score',ascending=True);
# # print(sort_score)
# # 5. Add new Column grade and insert the data  

# # df['grade'] = pd.cut(df['score'],bins=[0,10,20],labels=['high','low'])

# def grade(score):
#     if score >= 20 : return 'a';
#     elif score >= 15 : return 'b';
#     elif score >= 10  : return 'c'
#     elif score >= 8: return 'd';
#     else: return 'f'; 

# df['grade'] = df['score'].apply(grade);

# print(df)




# x = 10;

# def print_ten():
#     global x 
#     x = 100;
#     print(f'the value of x inside the function is : {x}' x);
    
# print_ten()


# print(f'value of x in global scope {x}');


# string = "UTSAV";
# print(string.center(9,'+'));

# string = "a ab abc Abcd a";
# print(string.count('a'));

# lst = ['hello','world','!!!'];
# print('-'.join(lst))

s = 'Hello';
print(min(s))

print('Hello from Ubuntu Linux')