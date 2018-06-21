class Parent():
    def __init__(self, last_name,eye_color):
        print("parent constructor is called")
        self.last_name=last_name
        self.eye_color=eye_color
    def show_info(self):
        print('Last Name: - '+ self.last_name)
        print("Eye Color: -" + self.eye_color)


billy_cyrus = Parent("Cyrus", "Blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()
    
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child constructor is called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print('Last Name: - '+ self.last_name)
        print("Eye Color: -" + self.eye_color)
        print("Number Of Toys: " + str(self.number_of_toys))

Liu_joe = Child("Joe", "Blue",10)
print(Liu_dave.number_of_toys)
Liu_dave.show_info()
