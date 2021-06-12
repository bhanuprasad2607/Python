"""
Python Program for finding the radius of circle of by 4 decimal points
"""
# importing math for pi value i.e, 3.141592653589793
import math

if __name__ == "__main__":
    radius = float(input())
    area_circle = math.pi * radius**2   # Calculate the radius of circle pi*r*r
    print(f"The area of circle of {radius:.2f} is {area_circle:.4f}") # The : represents property of value i.e., 4 decimal points the result is displayed
    