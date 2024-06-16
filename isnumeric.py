def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Test cases
print(is_numeric(123))  # True
print(is_numeric("-123"))  # True
print(is_numeric("123.456"))  # True
print(is_numeric("1e10"))  # True (scientific notation)
print(is_numeric("abc"))  # False