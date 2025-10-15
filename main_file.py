import os
def create_file(filename):
    try:
        with open (filename,'x') as f:
            print(f"Filename{filename}:Created Successfully!")
    except FileExistsError:
        print(F"Filename{filename}:already exist!")
    except Exception as E:
        print("An Error Occurred")
def view_all_files():
    file=os.listdir()
    if not file:
        print("No File Found!")
    else:
        print("Files in directory!")
        for files in file:
            print(files) 
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename}:has been deleted successfully!")
    except FileExistsError:
        print("file Not Found!")
    except Exception as e:
        print("An Error Occurred!")
def read_files(filename):
    try:
        with open("Sample.txt",'r') as f:
            content=f.read()
            print(f"ontent of '{filename}';\n{content}")
    except FileExistsError:
        print(f"{filename}doesn't exist!")    
    except Exception as e:
        print('An Error Occurred!')  
def edit_file(filename):
    try:
        with open('Sample.txt',"a" ) as f:
            content=input("Enter data to add =")
            f.write(content+"\n")
            print(f"content added to {filename} Successfully")
    except FileNotFoundError: 
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print("An Error Occurred!")
def main():
    while True:
        print('File Managenent APP')
        print('1: Create File')
        print('2: View All File')
        print('3: Delete File')
        print('4: Read File')
        print('5: Edit File')
        print('6: Exist') 
        choice =input('Enter Your Choice(1-6) = ')  
        if choice =="1":
            filename=input("Enter Your File-name to create = ")
            create_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice =="3":
            filename=input('Enter the name of the you want delete! ') 
            delete_file(filename)
        elif choice =="4":
            filename=input('Enter file name to read!= ')
            read_files(filename)
        elif choice=='5':
            filename=input("enter file name to edit!= ")
            edit_file(filename)
        elif choice=='6':
            print("Closing the App...")
        else:
            print("In-Valid Syntax")
if __name__=="__main__":    
    main()        
