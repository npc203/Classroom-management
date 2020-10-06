import os,json
#Helper functions
def fetch():
    #Creating user database
    if os.path.isfile("./users.json"):
        with open("./users.json",'r') as f:
            data = json.load(f)
    else:
        with open('./users.json','w') as f:
            data = {}
    return data

def login():
    data = fetch()
    print("Enter Login credentials:")
    name = input("username:")
    password = input("password:")
    for i in data:
        if name == i:
            if password != data[i]["password"]:
                print("\nInvalid Password\n")
                return
            return data[i]
    else:
        print("User not found, Please register")

def register():
    data = fetch()
    print("Enter details:")
    name = input("username:")
    if data:
        if name in [i[0] for i in data]:
            print("User Already exists!")
            return
    password = input("password:")
    
    while True:
        role = input("Enter Teacher or Student (T/S):")
        if role not in ("T","S"):
            print("Invalid input, Try again")
        else:
            break
    data[name] ={"name":name,"password":password,"role":role}
    if role == "S":
        data[name]["class"] = input("Enter your Class:")
        data[name]["section"] = input("Enter your section:")
        data[name]["roll_no"] = input("Enter your Roll No:")
        data[name]["exam"] = input("Enter The Examination:")
        data[name]["marks"]={}
       
    with open('./users.json','w') as f:
        json.dump(data,f)

    return data[name]
