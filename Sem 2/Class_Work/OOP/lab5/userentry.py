from notebook import *
from StaffSys import *

nb = notebook()
sys = System()

while True:
    try:
        syschoice = int(input(f"Please Enter from the following:\n1.Notebook System\n2.Staff System\n3.Exit\n"))
    except ValueError:
        print("That is not a valid input")
    while True:
            if syschoice == 1:
                try:    
                    choice = int(input(f"Welcome to the Notebook System, Please choose an option!\n1. Add Note\n2. Search Note\n3. Edit Note\n4. Delete Note\n5. Exit\n"))

                    if choice == 1:
                        tag = input("Please enter a tag: ").strip()
                        memo = input("Please enter a memo: ").strip()
                        author = input("Please enter an author (Press enter to leave blank): ").strip()

                        newNote = note(nb.getId(), tag, memo, author)
                        nb.addNote(newNote)
                    elif choice == 2:
                        search = int(input("Please enter the Id of the note you would like to look for: "))
                        success = nb.searchById(search)
                        if success == None:
                            print("No such note exists")
                        else:
                            success.displayNote()
                    elif choice == 3:
                        search = int(input("Please enter the Id of the note you would like to edit: "))
                        success = nb.searchById(search)
                        if success == None:
                            print("No such note exists")
                        else:
                            print("Note found:\n")
                            success.displayNote()
                            attr = input("Which attribute would you like to edit?: ").strip()
                            if attr == 'noteId':
                                print("noteId cannot be edited")
                            else:   
                                val = input("What would you like to change the value to?: ").strip()
                                updates = {attr: val}
                                nb.editNote(success.noteId, updates)
                    elif choice == 4:
                        try:
                            target = int(input("Please enter the Id of the note you would like to delete: "))
                            if target > nb.getId() or target < 0:
                                print("Please enter a valid input")
                        except ValueError:
                            print("Please enter a valid input")
                        else:
                            success = nb.searchById(target)
                            if success == None:
                                print("No such note exists..")
                            success.displayNote()
                            nb.deleteNote(success.noteId)
                    elif choice == 5:
                        break
                except ValueError:
                    print("That is not a valid input")
        
            elif syschoice == 2:
                try:
                    choice = int(input("Welcome to the Staff System, Please select from the following:\n1. Add Staff\n2. Search Staff\n3. Edit Staff\n4. Delete Staff\n5. Exit\n"))
                    if choice == 1:
                        print("Please Enter some information about the staff member you are going to add: ")
                        name = input("Name: ")
                        dob = input("Dob: ")
                        address = input("Address: ")
                        mobNum = input("Mobile Number: ")
                        role = input("What role is the staff member? Professional/Academic/Manager (Enter P/A/M): ").lower().strip()
                        if role == 'p':
                            pos = input("What is the staff members professional position?: ")
                            workDays = input("What days are they available to work?: ")
                            p1 = Professional(sys.getId(), name, dob, address, mobNum, pos, workDays)
                            p1.displayProfile()
                            sys.addStaff(p1)
                        elif role == 'a':
                            aca = input("What is their academic position?: ")
                            teach = input("What is their teaching area?: ")
                            research = input("What is their research area?: ")
                            a1 = Academic(sys.getId(), name, dob, address, mobNum, aca, teach, research)
                            a1.displayProfile()
                            sys.addStaff(a1)
                        elif role == "m":
                            dep = input("What is their department?: ")
                            m1 = Manager(sys.getId(), name, dob, address, mobNum, dep)
                            m1.displayProfile()
                            sys.addStaff(m1)
                    elif choice == 2:
                        target = input("Enter the staff ID you would like to search for: ")
                        x = sys.searchStaff(target)
                        if x == None:
                            print("Does not exist.")
                        x.displayProfile()
                    elif choice == 3:
                        search = int(input("Please enter the Id of the note you would like to edit: "))
                        success = sys.searchById(search)
                        if success == None:
                            print("No such Staff Member exists")
                        success.displayProfile()
                        attr = input("Which attribute would you like to edit?: ")
                        val = input("What is the new value you would like to assign to this attribute?")
                        updates = {attr: val}
                        sys.editStaff(target, updates)
                    elif choice == 4:
                        target = input("Enter the staff ID you would like to delete: ")
                        x = sys.searchStaff(target)
                        sys.delStaff(x.staffId)
                    elif choice == 5:
                        break   
                except ValueError:
                    print("Please enter a valid input")
            elif syschoice == 3:
                exit()