


# mkdir -> To creat new folder/directory
# rmdir -> To remove any folder/directory




# import os
# os.mkdir("Hello")
# os.rmdir("Hello")


"""
FILES
x -> This mode will only creat the file and 
if already exists we will get an error back
w -> Agar file exsist nahi kar rahi hai so this mode will create.
 one 
and insert the content inside the file. 
a -> 
r

"""



# MODE 1: x -> Just to creat the file 
# open("Garba.txt","x")


# Mode 2 : w -> If there is any content inside the file so 
# the new one will replace the old one
# file = open ("Garba.txt" , "w")
# file.write(" Khelo garba khub khelo ")


# Mode 3: a -> add the text at the last.
# file = open ("Garba.txt" , "a")
# file.write("\n This massage is newly added")



# Mode 4: r -> Read the content inside of the file
# file = open("Garba.txt","r")
# print(file.read())



# with open("Sample.txt","w") as file:
#     file.write("This is new file")

# CRUD - CREATE, READ, UPDATE, DELETE

# os.remove("Garba.txt")



from pathlib import Path
import os

def creat_folder():
    name = input("Tell your folder name:- ")
    p = Path (name)

    if p.exists():
        print("This folder name already exist please try again ")
        creat_folder()
    else:
        p.mkdir()
        print("folder created sucessfully ")


def read_folder():
    p = Path("")
    names = list(p.rglob("*"))

    for i in range (len(names)):
        print(f"{i+1} : {names[i]}")


def update_folder():
    read_folder()
    name = input("which folder you want to update:- ")
    old_p = Path(name) 

    if old_p.exists():
        new_name = input("Tell new folder name:- ")
        new_p =Path(new_name)
        old_p.rename(new_name)     


def remove_folder ():
    name_for_remove = input("Which folder you want to remove:- ")
    p = Path(name_for_remove)
    if p.exists():
            p.rmdir()
            print("Folder removed sucessfully ")        
    else:
        print("folder didn't found ")

#                         ----------> For Making File <----------        
        
def creat_file():
    name = input("Tell your file name with extension")
    p = Path(name)
    if p.exists():
        print("file already exists please try again ")
        creat_file()
    else:
        with open(p,"w") as file:
            data = input("Enter what you want to write : ")
            file.write(data)
            print("Sucessfully created ")

def read_file():
    name = input("Tell your file name with extention ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as file:
            data = file.read()
            print("/n/n/n Your file data is /n/n/n")
            print(data)                    

def update_file():
    names = read_folder
    for i in names:
        i = str(i)
        p = Path(i)
        if p.is_file():
            print(i)

    name = input("which file you want to update :- ")
    p = Path(name)

    if p.exists() and p.is_file():
        print("press 1 to change the file name ")
        print("press 2 to overwrite the file ")
        print("press 3 to append something in your file ")

        check = int(input("Tell your output :- "))

        if check == 1:
            new_name = input("Tell the new name :- ")
            new_p = Path(new_name)
            p.rename(new_p)

        elif check == 2:
            with open(p,'w') as file:
                data = input("what do you want to overwrite:- ")
                file.write(data)
                print("overwritten successfully ")

        elif check == 3:
            with open(p,'a') as file:
                data = input("what do you want to append:- ")
                file.write(" "+ data)
                print("appended successfully ")
            

    else:
        print("no such file exists please try again ")
        update_file()           




def deleting_file():
    name = input("Tell your file name with extention ")
    p = Path(name)

    if p.exists() and p.is_file():
        os.remove(p)
        print("File deleted successfully ")
    else:
        print("No such file exist please try again ")
        deleting_file()        


print("Press 1 for Creating a new folder: ")
print("Press 2 for Reading any folder: ")
print("Press 3 for Updating any folder: ")
print("Press 4 for Deleting any folder: ")
print("Press 5 for Creating a new file: ")
print("Press 6 for Reading any file: ")
print("Press 7 for Updating any file: ")
print("Press 8 for Deleting any file: ")

#   Responce for file 

res = int(input("tell your responce:- "))
if res == 1:
    creat_folder()


if res == 2:
    read_folder()


if res == 3:
    update_folder


if res == 4:
    remove_folder()

#        File

if res == 5:
    creat_file()


if res == 6:
    read_file()


if res == 7:
    update_file()



if res == 8:
    deleting_file()
