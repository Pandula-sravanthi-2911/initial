#importing csv
import csv
from meeting_calculation import *
from time_conversion import *
no_of_employees=int(input("enter the count of employees : "))
employee_fields=['emp_id','emp_in_time','emp_out_time','emp_break_start_time','emp_break_end_time','meeting_time']
FILE_NAME="employee.csv"
employee_details=[]
print("enter time in 24 hours format")
for i in range(no_of_employees):
    row=list(input("enter employee emp_id, emp_in_time, emp_out_time, emp_break_start_time,emp_break_end_time ").split(","))
    row.append([])
    employee_details.append(row)
with open(FILE_NAME,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(employee_fields)
    csvwriter.writerows(employee_details)
schedule=int(input("to schedule meeting enter 1 and to exit enter 0 : "))
while(schedule==1):
    emp1_id=input("enter id of first employee : ")
    emp2_id=input("enter id of second employee : ")
    duration=int(input("enter duration of meeting in minutes "))
    employee1_details=[]
    employee2_details=[]
    for j in range(no_of_employees):
        if employee_details[j][0]==emp1_id:
            employee1_details.append(employee_details[j][1])
            employee1_details.append(employee_details[j][2])
            employee1_details.append(employee_details[j][3])
            employee1_details.append(employee_details[j][4])
            meeting=employee_details[j][5]
            employee1_details= hour_min_conversion(employee1_details)
            employee1_details.append(meeting)
        if employee_details[j][0]==emp2_id:
            employee2_details.append(employee_details[j][1])
            employee2_details.append(employee_details[j][2])
            employee2_details.append(employee_details[j][3])
            employee2_details.append(employee_details[j][4])
            meeting=employee_details[j][5]
            employee2_details= hour_min_conversion(employee2_details)
            employee2_details.append(meeting)
    meeting_emp1=employee1_details[4]
    meeting_emp2=employee2_details[4]
    if employee1_details[2:4] not in  meeting_emp1:
        meeting_emp1.append(employee1_details[2:4])
    if employee2_details[2:4] not in  meeting_emp2:
        meeting_emp2.append(employee2_details[2:4])
    print(employee1_details)
    print(employee2_details)
    print(meeting_emp1)
    print(meeting_emp2)
    available_l1=find_available(employee1_details[0],employee1_details[1],duration,meeting_emp1)
    available_l2=find_available(employee2_details[0],employee2_details[1],duration,meeting_emp2)
    print(" available of 1",available_l1)
    print("available of 2 ",available_l2)
    if len(available_l1)==0 or len(available_l2)==0 :
        print("meeting can not be scheduled ")
    else:
        meet=check_available(available_l1,available_l2,duration)
        if(len(meet)==0):
            print("Sorry!! cannot schedule meeting today let us try next working day")
        else:
            print('the meeting is scheduled at  ',end='')
            min_hour_conversion(meet[0])
            print('-',end='')
            min_hour_conversion(meet[1])
            print()
            for j in range(no_of_employees):
                if employee_details[j][0]==emp1_id or employee_details[j][0]==emp2_id:
                    employee_details[j][5].append(meet)        
    schedule=int(input("to schedule meeting enter 1 and to exit enter 0 : "))
    
    
                                            
