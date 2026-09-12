import time
from datetime import date, datetime

class note:
    def __init__(self, noteId, tag, memo):
        self.noteId = noteId
        self.tag = tag
        self.memo = memo

        self.date = datetime.now()
        self.author = ''

    def displayNote(self):
        print(f"""Id: {self.noteId}
tag: {self.tag}
memo: {self.memo}
Date created: {self.date}
Author: {self.author}""")

    def updAttr(self, attr, val):
            if not hasattr(self, attr):
                return False
            setattr(self, attr, val)
            return True
    
class notebook:
    def __init__(self):
        self.notes = []

    def addNote(self, note: note):
        if note.noteId == None:
            print("cannot be empty ")
            return False
        success = self.searchById(note.noteId)
        if success is not None:
            print("Note already exists")
            return False
        
        self.notes.append(note)
        print(f"Note {note.noteId} created")
        note.displayNote()
        return True

    def searchById(self, noteId: int):
        for note in self.notes:
            if note.noteId == noteId :
                return note
        return None

    def editNote(self, noteId: int, updates: dict):
        note = self.searchById(noteId)
        if note is None:
            print("That note does not exist")
            return False
        for attr, val in updates.items():
            success = note.updAttr(attr, val)
            if success == False:
                print("Could not edit attributes")
            else:
                print("Attributes updated: \n")
                note.displayNote()

    def deleteNote(self, noteId):
        note = self.searchById(noteId)
        if note == None:
            print("that note does not exist ")
            return False
        else:
            note.displayNote()
            choice = input(f"Are you sure you want to delete Note {note.id}").lower()
            if choice == 'y':
                self.notes.remove(note)
                print("It has been deleted")
                return True
            else:
                print("Exiting...")
                time.sleep(3)
                return False
      
    def noteIdSort(self):
        idSorted = sorted(self.notes, key=lambda note: note.noteId)
        print(idSorted)
        return idSorted 

    def noteDateSort(self):
        dateSorted = sorted(self.notes, key=lambda note: note.date)
        print(dateSorted)
        return dateSorted




    
    


