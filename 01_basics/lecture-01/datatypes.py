# def string_Que(str1,str2):
#     print(f"length of first string is {len(str1)}");
#     str3 = f"{str1} {str2}";
#     print(f"Concateneted two string {str3}");
#     str_rev = str1[::-1];
#     print(f"reverse the string {str_rev}");
    
# string_Que("utsav","dhimmar");


# def list_Que(list1):
#     sortList = sorted(list1);
#     print(sortList);

#     print(f"sum of given list is {sum(list1,0)}");
#     lastEle = list1[-1];
    
#     print(f"last elements form in {list1} is {lastEle}");
    
    
# list_Que([11,90,123,67,23]);

# def str_Que(string):
#     strList = list(string); 
#  
#     vowels = ['a',"A","e","E",'i',"I",'o','O',"u","U"]; 
#     # strList = [char for char in strList if char not in vowels];
#     newStr = [];
#     for char in strList:
#         if char not in vowels:
#             newStr.append(char);
        
#     print(newStr);
#     return newStr;
    
# str_Que("Utsav");


def marks():
    n = int(input('Enter total number that you want to enter data: '));
    studen_List = [];
    print(f"Enter Data For {n} students \n");
    rollNo = 1;
    for i in range(n):
        print(f"Enter Data for {rollNo} student");
        mark1 = int(input("Enter marks for subject 1: "));
        mark2 = int(input("Enter marks for subject 2: "));
        mark3 = int(input("Enter marks for subject 3: "));
        
        total_mark = sum([mark1,mark2,mark3]);
        per = (total_mark * 100) / 90;
        
        grade = None;
        if per > 70 :
            grade = 'DIST';
        elif per > 60:
            grade = 'FIRST';
        elif per > 50:
            grade = 'SECOND';
        elif per > 40:
            grade = 'PASS';
        else:
            grade = 'FAIL';
            
        cstudent = [rollNo,total_mark,per,grade];
        
        studen_List.append(cstudent);
        rollNo+=1;
        
        
    for i in studen_List:
        print(f"{i[0]} student's total marks {i[1]} , percentage {i[2]:.2f} ,and grade is {i[3]} ");
        
marks()