import os
#Helper functions
def fetch():
    #Creating user database
    if os.path.isfile("./users.csv"):
        with open("./users.csv",'r') as f:
            data = f.readlines()
    else:
        with open('./users.csv','w') as f:
            data = None
    return data
def login():
    data = fetch()
    data = [i.split(",") for i in data]
    print("Enter Login credentials:")
    name = input("username:")
    password = input("password:")
    for i in range(len(data)):
        if name == data[i][0] :
            if password != data[i][1]:
                print("\nInvalid Password\n")
                return
            if data[i][2] == 'S':
                #print(i)
                data[i][3] = int(data[i][3])
                data[i][4] = int(data[i][4])
                data[i][5] = int(data[i][5]) 
            return data[i]
    else:
        print("User not found, Please register")
        return

def register():
    data = fetch()
    print("Enter details:")
    name = input("username:")
    password = input("password:")
    if data:
        if name in [i[0] for i in data]:
            print("User Already exists!")
            return
    
    while True:
        role = input("Enter Teacher or Student (T/S):")
        if role not in ("T","S"):
            print("Invalid input, Try again")
        else:
            break
    data = [name,password,role]
    if role == "S":
        print("\nENTER YOUR MARKS:\n")
        mat = int(input("Enter your math marks:"))
        phy = int(input("Enter your physics marks:"))
        che = int(input("Enter your chemistry marks:"))
        data.append(mat)
        data.append(phy)
        data.append(che)
    with open('./users.csv','a') as f:
        temp = [str(i) for i in data]
        f.write(','.join(temp)+'\n')
    return data
