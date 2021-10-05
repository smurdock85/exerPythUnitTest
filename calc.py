# Add function 
def add(x, y):
    """Add Function"""
    return x + y

# Subtract function 
def subtract(x, y):
    """Subtract Function"""
    return x - y

# Multiply function 
def multiply(x, y):
    """Multiply Function"""
    return x * y

# Divide function 
def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

