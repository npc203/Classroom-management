import os,xlwt,time
import datetime,json
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
            if data["role"] == 'T': #Logged as teacher
                print(f"Sucessfully Logged in as Teacher\n")
                while True:
                    print(" 1 View All student Details\n") 
                    print(" 2 View Failures\n")
                    print(" 3 Get class average\n")
                    print(" 4 View my details\n")
                    print(" 5 Enter marks for student\n")
                    print(" 6 Exit")

                    choice = int(input("->"))
                    with open("./users.json",'r') as f:
                        all_data = json.load(f)
                    if choice == 1:
                        wb = xlwt.Workbook()
                        count=1
                        sheet1 = wb.add_sheet("Marks")
                        sheet1.write(0,0,"Name")
                        sheet1.write(0,1,"Maths")
                        sheet1.write(0,2,"Physics")
                        sheet1.write(0,3,"Chemistry")
                        sheet1.write(0,4,"Computer Science")
                        sheet1.write(0,5,"English")
                        for i in all_data:
                            print(i)
                            if all_data[i]["role"]=='S':
                                i=all_data[i] #lazy to refactor
                                sheet1.write(count,0,i["name"])
                                sheet1.write(count,1,i["marks"]["mat"])
                                sheet1.write(count,2,i["marks"]["phy"])
                                sheet1.write(count,3,i["marks"]["chem"])
                                sheet1.write(count,4,i["marks"]["comp"])
                                sheet1.write(count,5,i["marks"]["eng"])
                                
                        wb.save("Student MarkSheet - "+str(time.time()).split(".")[0]+".xls")
                        print("Sucessfully extracted into an Excel File\n")
                    elif choice == 2:
                        count=1
                        for user in all_data:
                            if all_data[user]["role"]=='S':
                               user = all_data[user] #lazy to refactor
                               for sub in user["marks"]:
                                   if int(user["marks"][sub])<40:
                                       print("Name:",i["name"])
                                       count+=1
                                       break
                        print("Total number of failures:",count)
                    elif choice == 3:
                        count = 0
                        result = 0 
                        for user in all_data:
                            if all_data[user]["role"] == 'S':
                                result += sum(map(int,all_data[user]["marks"].values))/5
                                count+=1
                        print("\nTotal number of students:",count)
                        print("Class average percentage: {:.2f}%".format(result/count))

                    elif choice == 4:
                        print("-----------------------------------\n")
                        print("Username:",data["name"])
                        print("Password:",data["password"])
                        print("-----------------------------------\n")
                    
                    elif choice == 5:
                        name = input("Enter the name of the student:")
                        if name in all_data:
                            stud=all_data[name]
                            stud["marks"]["mat"]=input("Enter the Maths marks:")
                            stud["marks"]["chem"]=input("Enter the Chemistry marks:")
                            stud["marks"]["phy"]=input("Enter the Physics marks:")
                            stud["marks"]["eng"]=input("Enter the English marks:")
                            stud["marks"]["comp"]=input("Enter the Comp Sci marks:")
                            all_data[name]["marks"]=stud["marks"]
                            with open("./users.json",'w') as f:
                                json.dump(all_data,f)
                            print("Successfully Updated student's mark")
                        else:
                            print("Invalid Student Name!")
                    
                    else:
                        exit()
                    
                    input("Press enter to try again")
 
            elif data["role"] == 'S': #Logged as Student
                print(f"Sucessfully Logged in as Student\n")
                while True:
                    print(" 1 View my Details")
                    print(" 2 Get my marks")
                    print(" 3 Get my average")
                    print(" 4 Exit")
                    choice = int(input("->"))
                    if choice == 1:
                        print("-----------------------------------\n")
                        print("Name:",data["name"])
                        print("Roll No:",data["roll_no"])
                        print("Class   :",data["class"])
                        print("Section  :",data["section"])
                        print("-----------------------------------\n")
                    elif choice == 2:
                        if len(data["marks"])>0:
                            print(f"My Marks in {data['exam']}:\n")
                            print("Mathematics:",data["mat"])
                            print("Physics    :",data["phy"])
                            print("Chemistry  :",data["chem"])
                            print("English    :",data["eng"])
                            print("Comp Sci   :",data["comp"])
                        else:
                            print("Teacher hasn't updated your marks\n")
                    elif choice == 3:
                        if data["marks"]:
                            print("My average :",sum(map(int,data["marks"].values()))/len(data["marks"]))
                        else:
                            print("Teacher hasn't updated your marks\n")
                    else:
                        exit()
                    
                    input("\nPress enter to try again\n")
        else:
            pass

    except KeyError:
        print("Invalid Choice!!")
        exit()
        







