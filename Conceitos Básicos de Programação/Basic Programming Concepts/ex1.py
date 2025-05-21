"""
Create a program that asks to the user for two numbers, sum them and show the result
"""
def summation(number1,number2):

    s = number1 + number2
    return s

def main():

    try:
        number1 = int(input(f"Type a number: "))
        number2 = int(input(f"Type another number: "))

        print(f"\n{number1} + {number2} = {summation(number1,number2)}")
    
    except ValueError:
        print(f"\nThe input must be an integer.")

if __name__ == "__main__":
    main()