# Contact book application
list1 = []
# 1) Create a contact name number email

def Menu():
    print("""1 for viewing list
          2 for adding an item in list
          3 finding an item and returning the index
          4 update/change the value
          5 deleting the value
          0 for exit
        """)
    ch = int(input("Enter your choice : "))
    return ch


# 3) Find update and Delete a contact

#finding contact:
def find_contact(name):
    for item in list1:
        if item[0] == name :
            return "found" , item
        else:
            return "Not Found"
        
# For updation of contact:
def update_credentials(from_name , to_name):
    for i in list1:
        if i[0] == from_name :
            i[0] = to_name
            print("Opperation Successful!!  ")

#for deletion:
def delete_credentials(name):
    for i in list1:
        if i[0] == name:
            x = list1.pop(i)
    


#Driver code
choice = Menu()
if choice == 1:
        print("Required list is : \n " , list1)
        Menu()


elif choice == 2:
    name = input("Enter your name : ")
    number = input("Enter your Mobile Number : ")
    email = input("Enter your Email Id : ")
    list1.append([name , number , email])
    print("Required Entery is done.")
    Menu()


elif choice == 3:
    itp1 = input("Enter the name to be searched : ")
    if find_contact(itp1)[0] == "Found":
        print(f"{find_contact(itp1)[0]} at index {find_contact(itp1)[1]}")
        Menu()
    else:
        print("Entry not found :(  ")
        Menu()

elif choice == 4:
    from_name = input("Enter the name to be updated : ")
    to_name = input("Enter the final name : ")

    update_credentials(from_name , to_name)
    Menu()

elif choice == 5:
    del_temp = input("Enter the name to be deleted.")
    delete_credentials(del_temp)
    Menu()
    
