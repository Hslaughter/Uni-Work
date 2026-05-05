# addressObj1 = Address("2/15", "John Ave", "Sydney", "NSW", "2512")
# addressObj2 = Address("3", "Circle St", "Mathville", "ACT", "0214")
# addressObj1.printAddress()
# addressObj2.printAddress()

	

# 2/15 John Ave, Sydney, NSW 2512
# 3 Circle St, Mathville, ACT 0214

# 2/15 John Ave, Sydney, NSW 2512
# 3 Circle St, Mathville, ACT 0214

# addressObj1 = Address("5", "Frog St", "Pondy", "ABC", "1111")
# addressObj2 = Address("3/7", "Emu Ave", "Blah", "XYZ", "2222")
# addressObj1.printAddress()
# addressObj2.printAddress()

# 5 Frog St, Pondy, ABC 1111
# 3/7 Emu Ave, Blah, XYZ 2222

class Address:
    def __init__(self, streetNo, streetName, city, region, postcode):
        self.streetNo = streetNo
        self.streetName = streetName
        self.city = city
        self.region  = region
        self.postcode = postcode

    def printAddress(self):
        print(f"{self.streetNo} {self.streetName}, {self.city}, {self.region} {self.postcode}")

addressObj1 = Address("2/15", "John Ave", "Sydney", "NSW", "2512")
addressObj2 = Address("3", "Circle St", "Mathville", "ACT", "0214")
addressObj1.printAddress()
addressObj2.printAddress()
print()
addressObj1 = Address("5", "Frog St", "Pondy", "ABC", "1111")
addressObj2 = Address("3/7", "Emu Ave", "Blah", "XYZ", "2222")
addressObj1.printAddress()
addressObj2.printAddress()

