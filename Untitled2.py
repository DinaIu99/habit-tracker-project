#!/usr/bin/env python
# coding: utf-8

# In[72]:


import datetime

def menu():
    while True:
        print("Select an Option:\n \n1.Create Habit")
        print("2.View Habit")    
        print("3.Modify Habit")    
        print("4.Analyze Habit")    
        print("5.Delete Habit")
        print("6.Exit")
        try:
            x=int(input("Enter Your Choice... "))
        except:
            print("Invalid Input, Try Again")
        if x==1:
            create_habit_menu()
        elif x==2:
            view_habit()
        elif x==3:
            modify_habit()
        elif x==4:
            analyze_habit()
        elif x==5:
            delete_habit()
        elif x==6:
            print('Quiting...')
            break
        else:
            print("Invalid Input, Try Again\n")
            
            
def create_habit_menu():
    print("Select an Option:\n \n1.Daily")
    print("2.Weekly")
    print("3.Monthly")
    try:
        x=int(input("Enter Your Choice... "))
    except:
        print("Invalid Input, Try Again")
    if x==1:
        create_habit('Daily')
    elif x==2:
        create_habit('Weekly')
    elif x==3:
        create_habit('Monthly')
        
        
def create_habit(types):
    f=open('tasks.txt','a')
    if types=='Daily':
        x=input("Please enter the name of the task: ")
        y=input("Please enter starting date in YYYY-MM-DD format: ")
        z=input("Please enter ending date in YYYY-MM-DD format: ")
        w=input("Please enter Daily Period: ")
        li=x+" "+"Daily"+" "+y+" "+z+" "+str(0)+' '+w+"\n"
        f.write(li)
        print("Task Created Successfully")
    if types=='Weekly':
        x=input("Please enter the name of the task: ")
        y=input("Please enter starting date in YYYY-MM-DD format: ")
        z=input("Please enter ending date in YYYY-MM-DD format: ")
        w=input("Please enter Weekly Period: ")
        li=x+" "+"Weekly"+" "+y+" "+z+" "+str(0)+' '+w+"\n"
        f.write(li)
    if types=='Monthly':
        x=input("Please enter the name of the task: ")
        y=input("Please enter starting date in YYYY-MM-DD format: ")
        z=input("Please enter ending date in YYYY-MM-DD format: ")
        w=input("Please enter Monthly Period: ")
        li=x+" "+"Monthly"+" "+y+" "+z+" "+str(0)+' '+w+"\n"
        f.write(li)

        
def view_habit():
    f=open("tasks.txt",'r')
    while True:
        x=f.readline()
        if x=='':
            break
        else:
            x=x.split(' ')
            print("\n")
            print("Habit Name:",x[0])
            print("Habit Type:",x[1])
            print("Starting Date:",x[2])
            print("Ending Date:",x[3])
            if int(x[4])>0:
                print("Status: Task Checked with",x[4]," Streak")
            else:
                print("Status: Task Unchecked")
                x[5]=x[5].split('\n')
            print("Period: ",x[5][0])
            print("\n")
            
def modify_habit():
    y=[]
    f=open("tasks.txt",'r')
    print("Select an Option to Modify:\n \n1.Check Task")
    print("2.Uncheck Task")    
    print("3.Modify Habit Name")
    try:
        sel=int(input("Your Choice... "))
    except:
        print("Invalid Choice, Returning to Main Menu\n")
        return
    if sel==1:
        mark_habit('Check')
    elif sel==2:
        mark_habit('Uncheck')
    elif sel==3:
        l=input("Enter New Habit Name:  ")
        mark_habit(l)
    else:
        print("Invalid Choice, Returning to Main Menu\n")
        return
    while True:
        x=f.readline()
        if x=='':
            break
        y.append(x)
        
def mark_habit(x):
    y=[]
    f=open("tasks.txt",'r')
    i=input("Enter the name of the habit to Modify: ")
    while True:
        o=f.readline()
        if o=='':
            f2=open("tasks.txt",'w')
            for j in y:
                f2.write(j)         
            print("Modification Complete!")
            return
        o=o.split(' ')
        if o[0]==i:
            if x=='Check':
                o[4]=int(o[4])+1
                o[4]=str(o[4])
            elif x=='Uncheck':
                o[4]=str(0)
            else:
                o[0]=x
        li=o[0]+" "+o[1]+" "+o[2]+" "+o[3]+" "+o[4]+' '+o[5]
        y.append(li)
        
        
def delete_habit():
    y=[]
    f=open("tasks.txt",'r')
    i=input("Enter the name of the habit to Delete: ")
    while True:
        o=f.readline()
        if o=='':
            f2=open("tasks.txt",'w')
            for j in y:
                f2.write(j)         
            print("Deletion Complete!")
            return
        o=o.split(' ')
        if o[0]!=i:
            li=o[0]+" "+o[1]+" "+o[2]+" "+o[3]+" "+o[4]+' '+o[5]
            y.append(li)
         
        
def analyze_habit():
    today = date.today()
    today=today.strftime("%y-%m-%d")
    print("\n\n")
    print("Today's Date is: ",today)
    f=open("tasks.txt",'r')
    while True:
        x=f.readline()
        if x=='':
            break
        else:
            x=x.split(' ')
            print("\n")
            print("Habit Name:",x[0])
            print("Habit Type:",x[1])
            if int(x[4])>0:
                print("Status: Task Checked with",x[4]," Streak")
            else:
                print("Status: Task Unchecked")
            xx=datetime.datetime.strptime(today,"%y-%m-%d")
            yy=datetime.datetime.strptime(x[3],"%Y-%m-%d")
            d=yy-xx
            if int(d.days)>0:
                print("Ending in: ",d.days,' day(s)')
            else:
                print("Was due ",abs(d.days)," day(s) ago")
            x[5]=x[5].split('\n')
    print("\n\n")
    
    
menu()


# In[ ]:




