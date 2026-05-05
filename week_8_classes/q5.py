# Test 	Result

# song1 = Song("Baby Shark", "Pinkfong", 2016, "Kids/Educational")
# song1.display_info()

	

# Title: Baby Shark
# Creator: Pinkfong
# Year: 2016
# Genre: Kids/Educational

class Song:
    def __init__(self, title, creator, year, genre):
        self.title = title
        self.creator = creator
        self.year= year
        self.genre = genre
        
    def display_info(self):
        print(f"""Title: {self.title}
Creator: {self.creator}
Year: {self.year}
Genre: {self.genre}""")