class Babu:
    def __init__(self, name):  # Correct constructor
        self.name = name

    def display_info(self):
        print(f"Babu name: {self.name}")


class Suba(Babu):
    def __init__(self, name, habits):  # Correct constructor
        super().__init__(name)  # Call constructor of the base class
        self.habits = habits

    def display_info(self):
        print(f"Suba name: {self.name}, Habits: {self.habits}")


class Sanjay(Suba):
    def __init__(self, name, habits, age):  # Correct constructor
        super().__init__(name, habits)  # Call constructor of the Suba class
        self.age = age

    def display_info(self):
        print(f"Sanjay name: {self.name}, Habits: {self.habits}, Age: {self.age}")


# Creating an instance of Sanjay
sanjay_1 = Sanjay(name="Sanjay", habits="Reading", age=25)
sanjay_1.display_info()

