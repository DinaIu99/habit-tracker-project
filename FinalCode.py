# Libraries
from datetime import date
import datetime

# The menu will display the main menu options and will call the respective functions of that selected 
# option by the user. however, if the user selects an invalid option error will be displayed.
# the menu function remains running till the 'QUIT' option is not selected by the user
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
        except:
            print("Invalid Input, Try Again")
        
            
# this function is another menu to select the option between daily weekly and monthly
# we get to select the type of habit we want to create and finally pass the type as a parameter to 
# other function that creates that type           
def create_habit_menu():
    print("Select an Option:\n \n1.Daily")
    print("2.Weekly")
    print("3.Monthly")
    try:
        x=int(input("Enter Your Choice... "))
        if x==1:
            create_habit('Daily')
        elif x==2:
            create_habit('Weekly')
        elif x==3:
            create_habit('Monthly')
        else:
            print("Invalid Input Returning Back...\n")
    except:
        print("Invalid Input Returning Back...\n")

# This is a helping function of create_habit that is merely for the purpose of correct and accurate data 
# it also uses user input and checks for current date and finally returns the accurate and valid date back to the creatE_habit for data
# creation
def date_entry():
    while(1):
        y0=''
        y1=0
        y2=0
        y3=0
        while(1):
            try: 
                y1=int(input("Please enter the year: "))
                if y1>1000:
                    break
                print("Invalid Input, Try Again")
            except:
                print("Invalid Input, Try Again")
        while(1):
            try:
                y2=int(input("Please enter the month: "))
                if y2<=12:
                    break
                print("Invalid Input, Try Again")
            except:
                print("Invalid Input, Try Again")
        while(1):
            try:
                y3=int(input("Please enter the day: "))
                if y3<=31:
                    break
                print("Invalid Input, Try Again")
            except:
                print("Invalid Input, Try Again")
        today=date.today()
        d4 = today.strftime("%Y-%m-%d")
        d4=d4.split('-')
        if int(d4[0])<y1:
            break
        elif int(d4[0])==y1 and int(d4[1])<y2:
            break
        elif int(d4[0])==y1 and int(d4[1])==y2 and int(d4[2])<=y3:
            break
        else:
            print("Date cannot be earlier than todays date... please enter again")
    y0=str(y1)+'-'+str(y2)+'-'+str(y3)
    return y0

# takes type as a parameter and asks user to fill the other required information and finally saves it in the 
# file by using file handling. it also displays the confirmation notification and also displays error if no such 
# type exists
def create_habit(types):
    f=open('tasks.txt','a')
    if types=='Daily':
        x=input("Please enter the name of the task: ")
        print("Please enter starting date: ")
        y=date_entry()
        print("Please enter ending date: ")
        z=date_entry()
        w=int(input("Please enter Daily Period: "))
        li=x+" "+"Daily"+" "+y+" "+z+" "+str(0)+' '+str(w)+"\n"
        f.write(li)
        print("Task Created Successfully")
    if types=='Weekly':
        x=input("Please enter the name of the task: ")
        print("Please enter starting date: ")
        y=date_entry()
        print("Please enter ending date: ")
        z=date_entry()
        w=int(input("Please enter Weekly Period: "))
        li=x+" "+"Weekly"+" "+y+" "+z+" "+str(0)+' '+str(w)+"\n"
        f.write(li)
        print("Task Created Successfully")
    if types=='Monthly':
        x=input("Please enter the name of the task: ")
        print("Please enter starting date: ")
        y=date_entry()
        print("Please enter ending date: ")
        z=date_entry()
        w=int(input("Please enter Monthly Period: "))
        li=x+" "+"Monthly"+" "+y+" "+z+" "+str(0)+' '+str(w)+"\n"
        f.write(li)
        print("Task Created Successfully")

# this functions helps in viewing the habits that the user has previously created and in a simple manner for user to 
# understand it also displays all the related data to that habit and whether it is checked or un checked      
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

# Modify habit povides user options to modify various functionalities or check or uncheck a task
# when the user makes their choice, this function calls the mark_habit function and passes its selection as a parameter to 
# it             
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

# this function is used to open the file and then search for the name of the habit the user wants to edit and finally
# changes the habits data according to the user requirment provided to it as a parameter 
# at the end saves the updated data in the file again for viewing and further uses
def mark_habit(x):
    y=[]
    found=0
    f=open("tasks.txt",'r')
    i=input("Enter the name of the habit to Modify: ")
    while True:
        o=f.readline()
        if o=='':
            f2=open("tasks.txt",'w')
            for j in y:
                f2.write(j)
            if found==0:
                print("No such habit with this name found...")
            else:
                print("Modification completed")
            return
        o=o.split(' ')
        if o[0]==i:
            found=1
            if x=='Check':
                o[4]=int(o[4])+1
                o[4]=str(o[4])
            elif x=='Uncheck':
                o[4]=str(0)
            else:
                o[0]=x
        li=o[0]+" "+o[1]+" "+o[2]+" "+o[3]+" "+o[4]+' '+o[5]
        y.append(li)

# this function asks user for the name of the habit and then deletes that data as whole from the file         
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
         
 # this function is used to analyze the habits and define if they are due or days remaining to their due 
# from the current date timestamp it also displays other important functionalities that
# helps in defining and analying the habits to the user      
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
    
# menu is called to run the code    
menu()




