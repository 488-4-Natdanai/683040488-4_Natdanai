# area.py
def calculate_area(length, width):
    if not isinstance(length, (int,float)):
        raise TypeError("Both value has to be number")
    
    if not isinstance(width, (int,float)):
        raise TypeError("Both value has to be number")
    
    if length < 0 or width < 0:
        raise ValueError("Both values has to be positive")
    return length * width