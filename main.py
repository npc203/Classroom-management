import os
import datetime
from login import login,register
#name,pass,role,mat,phy,che
while True:
    print(" WELCOME TO Classroom\n----------------------------------------------------------\n") 
    print(" 1 Login\n") 
    print(" 2 Register\n")
    print(" 3 Exit\n") 

    try:
        choice = int(input("->"))
        options = {1:login,2:register,3:exit}
        data = options[choice]()
        if data:
            print(f"\nLogged in Time:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #print(data)
            if data[2] == 'T\n' or data[2] == 'T': #Logged as teacher
                print(f"Sucessfully Logged in as Teacher\n")
                while True:
                    print(" 1 View All student Details\n") 
                    print(" 2 View Failures\n")
                    print(" 3 Get class average\n")
                    print(" 4 View my details\n")
                    print(" 5 Exit")

                    choice = int(input("->"))
                    with open("./users.csv",'r') as f:
                            all_data = f.readlines()
                            all_data = [i.split(',') for i in all_data]
                    if choice == 1:
                        for i in all_data:
                            if i[2]=='S':
                                print("-----------------------------------\n")
                                print("Name:",i[0])
                                print("Marks:")
                                print("Mathematics:",i[3])
                                print("Physics    :",i[4])
                                print("Chemistry  :",i[5])
                    elif choice == 2:
                        for i in all_data:
                            if i[2]=='S':
                                if sum([int(i) for i in i[3:6]])/3 < 50:
                                    print("-----------------------------------\n")
                                    print("Name:",i[0])
                                    print("Marks:")
                                    print("Mathematics:",i[3])
                                    print("Physics    :",i[4])
                                    print("Chemistry  :",i[5])
                    elif choice == 3:
                        count = 0
                        result = 0 
                        for i in all_data:
                            if i[2] == 'S':
                                result += sum([int(i) for i in i[3:6]])/3
                                count+=1
                        print("\nTotal number of students:",count)
                        print("Class average percentage: {:.2f}%".format(result/count))

                    elif choice == 4:
                        print("-----------------------------------\n")
                        print("Username:",i[0])
                        print("Password:",i[1])
                        print("-----------------------------------\n")
                    
                    else:
                        exit()
                    
                    input("Press enter to try again")
 
            elif data[2] == 'S\n' or data[2] == 'S': #Logged as Student
                print(f"Sucessfully Logged in as Student\n")
                while True:
                    print(" 1 View my Details")
                    print(" 2 Get my average")
                    print(" 3 Exit")
                    choice = int(input("->"))
                    if choice == 1:
                        print("-----------------------------------\n")
                        print("Name:",data[0])
                        print("My Marks:\n")
                        print("Mathematics:",data[3])
                        print("Physics    :",data[4])
                        print("Chemistry  :",data[5])
                        print("-----------------------------------\n")
                    elif choice == 2:
                        print("My average :",sum(data[3:6])/3)
                    else:
                        exit()
                    
                    input("\nPress enter to try again\n")
        else:
            pass

    except KeyError:
        print("Invalid Choice")
        exit()
        







