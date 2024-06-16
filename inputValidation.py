def get_single_number():
    while True:
        user_input = input("Please enter a single number: ")
        try:
            # Attempt to convert the input to a float (or int if you prefer)
            number = float(user_input)
            print(f"Thank you! You entered the number: {number}")
            return number
        except ValueError:
            # If conversion fails, it means the input is not a valid number
            print("Invalid input. Please enter a valid number.")

# Call the function
get_single_number()