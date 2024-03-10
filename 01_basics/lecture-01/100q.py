import pandas as pd

n = int(input("Enter student number: "));

student_data = [];

def sum_of_marks(marks_lst):
    return sum(marks_lst)

def cal_per(t_marks):
    per = ((t_marks) * 100) / 6;
    return per;

for i in range(n):
    sid = int(input('input sid: '));
    sname = input(f"Enter name of {sid}");
    sub_marks = [];
    
    for j in range(1,7):
        sub_marks.append(int(input(f"Enter marks {j} :")))
        
        
    total_marks = sum_of_marks(sub_marks);
    percenatges = cal_per(total_marks)
        
    student_data.append([sid,sname]+ sub_marks + [total_marks,percenatges]);

print(student_data);
    
    
label = ['id','name','sub1','sub2','sub3','sub4','sub5','sub6','total_marks','percenatges'];

df = pd.DataFrame(student_data,columns=label);


print(df)

