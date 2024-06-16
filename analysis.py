class interestCalculator:
    # Define properties
    def __init__(self, Contribution, interestRate, Years):
        self.Contribution = Contribution;
        self.interestRate = interestRate;
        self.Years = Years;

    def simpleInterestCalculator(self):
        Amount = self.Contribution * self.interestRate/100 * self.Years + self.Contribution;
        print("\nSimple Interest Calculator:")
        print(round(Amount))

    def compoundInterestCalculator(self):
        compoundInterestAmount = self.Contribution*( (1+(self.interestRate/100))** self.Years)
        print("Compound Interest Calculator:")
        print(round(compoundInterestAmount))


# Create an instance of the class
myInterestCalcChoice = interestCalculator(20000, 10.5, 20);

# Call the function
myInterestCalcChoice.compoundInterestCalculator()

myInterestCalcChoice.simpleInterestCalculator()
