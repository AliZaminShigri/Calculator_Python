# Author: Zamin Ali
# Project: This is a mini project that does some calculations and conversions
# Libraries used: "math"
# Number of operations included: 18
# GUI based: No (runs on terminal only)

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed!"
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def sqrt(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    return math.factorial(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def currency_conversion(amount, rate):
    return amount * rate

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def calculator():
    print("Welcome to my Calculator!")
    print("Here you can perform multiple operations and conversions.")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Modulus (%)")
        print("7. Square Root (√)")
        print("8. Logarithm (log)")
        print("9. Factorial (!)")
        print("10. Sine (sin)")
        print("11. Cosine (cos)")
        print("12. Tangent (tan)")
        print("13. Currency Conversion")
        print("14. Celsius to Fahrenheit")
        print("15. Fahrenheit to Celsius")
        print("16. Meters to Kilometers")
        print("17. Kilometers to Miles")
        print("18. Miles to Kilometers")
        print("19. Exit")
        
        choice = input("\nEnter your choice (1-19): ")
        
        if choice == '19':
            print("Thank you for using the calculator! Goodbye.")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "^"
            elif choice == '6':
                result = modulus(num1, num2)
                operation = "%"
            print(f"\nResult[ {num1} {operation} {num2} = {result} ]")

        elif choice == '7':
            num = float(input("Enter the number: "))
            result = sqrt(num)
            print(f"\n√{num} = {result}")

        elif choice == '8':
            num = float(input("Enter the number: "))
            base = float(input("Enter the base (default is 10): ") or 10)
            result = logarithm(num, base)
            print(f"\nlog{base}({num}) = {result}")

        elif choice == '9':
            num = int(input("Enter an integer: "))
            result = factorial(num)
            print(f"\n{num}! = {result}")

        elif choice == '10':
            num = float(input("Enter the angle in degrees: "))
            result = sine(num)
            print(f"\nsin({num}°) = {result}")

        elif choice == '11':
            num = float(input("Enter the angle in degrees: "))
            result = cosine(num)
            print(f"\ncos({num}°) = {result}")

        elif choice == '12':
            num = float(input("Enter the angle in degrees: "))
            result = tangent(num)
            print(f"\ntan({num}°) = {result}")

        elif choice == '13':
            amount = float(input("Enter the amount to convert: "))
            rate = float(input("Enter the conversion rate: "))
            result = currency_conversion(amount, rate)
            print(f"\nConverted amount = {result}")

        elif choice == '14':
            celsius = float(input("Enter the temperature in Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"\n{celsius}°C = {result}°F")

        elif choice == '15':
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"\n{fahrenheit}°F = {result}°C")

        elif choice == '16':
            meters = float(input("Enter the distance in meters: "))
            result = meters_to_kilometers(meters)
            print(f"\n{meters} meters = {result} kilometers")

        elif choice == '17':
            kilometers = float(input("Enter the distance in kilometers: "))
            result = kilometers_to_miles(kilometers)
            print(f"\n{kilometers} km = {result} miles")

        elif choice == '18':
            miles = float(input("Enter the distance in miles: "))
            result = miles_to_kilometers(miles)
            print(f"\n{miles} miles = {result} km")

        else:
            print("Invalid input. Please enter a valid choice (1-19).")

# To start the calculator
calculator()
