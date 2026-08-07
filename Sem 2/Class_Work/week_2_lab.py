class HelloWorld:
    def greet(self):
        name = input("Enter your name: ")
        print(f"hi {name}, hello object world")

greeter = HelloWorld()
greeter.greet() 