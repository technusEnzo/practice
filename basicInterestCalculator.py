# Add libraries
import numpy as np

class interestCalculator:
    # Define properties
    def __init__(self, Contribution, interestRate, Years):
        self.Contribution = Contribution;
        self.interestRate = interestRate;
        self.Years = Years;
    
    # Simple interest calculator
    def simpleInterestCalculator(self):
        check_numeric_properties(self);
        Amount = self.Contribution * self.interestRate/100 * self.Years + self.Contribution;
        print("\nSimple Interest Calculator:")
        print(Amount)

    # Compound interest calculator
    def compoundInterestCalculator(self):
        check_numeric_properties(self);
        compoundInterestAmount = self.Contribution*( (1+(self.interestRate/100))** self.Years)
        print("\nCompound Interest Calculator:")
        print(compoundInterestAmount)
     
# Check numeric properties - ChatGPT code
def check_numeric_properties(self):
    numeric_types = (int, float, complex)
    for attr, value in self.__dict__.items():
        if isinstance(value, numeric_types):
            print(f"Attribute '{attr}' with value '{value}' is numeric.")
        else:
            print(f"Attribute '{attr}' with value '{value}' is not numeric. Please enter in a numeric value")

# Create an instance of the class
Contribution = input("Enter in a value for the contribution amount:")
interestRate = input("Enter in a value for the interest rate:")
Years = input("Enter in a value for the number of years:")
myInterestCalcChoice = interestCalculator(float(Contribution), float(interestRate), float(Years));
inputTypeofCalc = input("Would you like to perform a simple interest or a compound interest calculation?")

if inputTypeofCalc == 'simple interest':
    myInterestCalcChoice.simpleInterestCalculator()
    
elif inputTypeofCalc == 'compound interest':
        myInterestCalcChoice.compoundInterestCalculator()