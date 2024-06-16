class Car:
    # Define properties
    def __init__(self, Colour, engineSize, Make):
        self.Colour = Colour
        self.engineSize = engineSize;
        self.Make = Make;
    
    # Create a function that displays the result
    def myFunc(self):
        print("\nHello, my car is of a colour " + self.Colour + " and it is a " + self.engineSize + " engine bitches!")

# Create an instance of the class
myCarChoice = Car("Dolphin Grey", "2.0L", "Audi")

# Call the function
myCarChoice.myFunc()


