from abc import *

class System:
    def __init__(self):
        self.staffMems = []

    def searchStaff(self, staffId):
        for staff in self.staffMems:
            if staffId == staff.staffId:
                return staff
        return None

    def addStaff(self, staff: Staff):
        check = self.searchStaff(staff.staffId)
        if check == None:
            self.staffMems.append(staff)
            return True
        else:
            print("Staff Member exists already")
            return False

    def delStaff(self, staffId):
        target = self.searchStaff(staffId)
        if target == None:
            print(f"Staff with Id: {staffId} does not exist")
            return False
        else:
            choice = input(f"Are you sure you want to delete {target.name} from the list?").lower()
            if choice == "y":
                self.staffMems.remove(target)
                print("Deleted")
                return True

    def editStaff(self, staffId, updates : dict):
        target = self.searchStaff(staffId)
        if target == None:
            print(f"Staff with Id: {staffId} does not exist")
            return False
        for attr, val in updates.items():
            success = target.updAttr(attr, val)
            if success:
                print("Successfully Updated")
            else:
                return False
        return True

class Staff(ABC):
    def __init__(self, staffId):
        self.staffId = staffId

    @abstractmethod
    def displayProfile(self):
        print(f"Staff Id: {self.staffId} ")
        print(f"Name: {self.name} ")
        print(f"Date of birth: {self.dob} ")
        print(f"Address: {self.address} ")
        print(f"Mobile Phone Number: {self.mobNum} ")
        
class People:
    def __init__(self, name, dob, address, mobNum):
        self.name = name
        self.dob = dob
        self.address = address
        self.mobNum = mobNum

    def updAttr(self, attr, val):
        if not hasattr(self, attr):
            return False
        setattr(self, attr, val)
        return True

class Professional(Staff, People):
    def __init__(self, staffId, name, dob, address, mobNum, profPosition, workDays):
        Staff.__init__(self, staffId)
        People.__init__(self, name, dob, address, mobNum)
        self.profPosition = profPosition
        self.workDays = workDays

    def displayProfile(self):
        super().displayProfile()
        print(f"Professional Position: {self.profPosition} ")
        print(f"Workdays: {self.workDays}")

class Academic(Staff, People):
    def __init__(self, staffId, name, dob, address, mobNum, acaPosition, teachArea, researchArea):
        Staff.__init__(self, staffId)
        People.__init__(self, name, dob, address, mobNum)
        self.acaPostion = acaPosition
        self.teachArea = teachArea
        self.researchArea = researchArea

    def displayProfile(self):
        super().displayProfile()
        print(f"Academic Position: {self.acaPostion} ")
        print(f"Teaching Area: {self.teachArea} ")
        print(f"Research Area: {self.researchArea} ")

class Manager(Staff, People):
    def __init__(self, staffId, name, dob, address, mobNum, department):
        Staff.__init__(self, staffId)
        People.__init__(self, name, dob, address, mobNum)
        self.department = department

    def displayProfile(self):
        super().displayProfile()
        print(f"Department: {self.department}")

class Address:
    def __init__(self, streetNo, streetName, city, state, postcode, country):
        self.streetNo = streetNo
        self.streetName = streetName
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country