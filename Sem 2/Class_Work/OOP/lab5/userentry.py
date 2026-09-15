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
                ...
            elif syschoice == 3:
                exit()