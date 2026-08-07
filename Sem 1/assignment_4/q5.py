# addressObj1 = Address("2/15", "John Ave", "Sydney", "NSW", "2512")
# addressObj2 = Address("3", "Circle St", "Mathville", "ACT", "0214")
# print(addressObj1)
# print(addressObj2)

	

# Address[number="2/15", street="John Ave", suburb="Sydney", state="NSW", code="2512"]
# Address[number="3", street="Circle St", suburb="Mathville", state="ACT", code="0214"]

# Address[number="2/15", street="John Ave", suburb="Sydney", state="NSW", code="2512"]
# Address[number="3", street="Circle St", suburb="Mathville", state="ACT", code="0214"]

# addressObj1 = Address("5", "Frog St", "Pondy", "ABC", "1111")
# addressObj2 = Address("3/7", "Emu Ave", "Blah", "XYZ", "2222")
# print(addressObj1)
# print(addressObj2)

	

# Address[number="5", street="Frog St", suburb="Pondy", state="ABC", code="1111"]
# Address[number="3/7", street="Emu Ave", suburb="Blah", state="XYZ", code="2222"]


class Address:
    def __init__(self, streetNo, streetName, city, region, postcode):
        self.streetNo = streetNo
        self.streetName = streetName
        self.city = city
        self.region  = region
        self.postcode = postcode

    def __str__(self):
         return f'Address[number="{self.streetNo}", street="{self.streetName}", suburb="{self.city}", state="{self.region}", code="{self.postcode}"]'
    

addressObj1 = Address("2/15", "John Ave", "Sydney", "NSW", "2512")
addressObj2 = Address("3", "Circle St", "Mathville", "ACT", "0214")
print(addressObj1)
print(addressObj2)
print()
addressObj1 = Address("5", "Frog St", "Pondy", "ABC", "1111")
addressObj2 = Address("3/7", "Emu Ave", "Blah", "XYZ", "2222")
print(addressObj1)
print(addressObj2)