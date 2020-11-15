# dog.py
class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
    
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print("Woof!")

    #Step 1: Stretch Challanges
    def roll_over(self):
        print("Rolls Over")

    def sit_down(self):
        print("Sits")

