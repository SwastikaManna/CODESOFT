class Calculator:
    def __init__(self):
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "//": lambda x, y: x//y,
            "%": lambda x, y: x%y,
        }

    def calculate(self, num1, num2, operator):
        """Calculates the expression and returns the result.

        Args:
            num1: The first number in the expression.
            num2: The second number in the expression.
            operator: The mathematical operator to perform.

        Returns:
            The result of the calculation.
        """

        try:
            return self.operations[operator](num1, num2)
        except Exception as e:
            print(e)
            return None

def main():
    calculator = Calculator()
    ch=True

    while ch:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Choose an operation (+, -, *, /,//,%): ")

        result = calculator.calculate(num1, num2, operator)

        if result is not None:
            print(f"The result is: {result}")
        else:
            print("Invalid input.")
        c=input("Want to do more calculations? Y/N: ")
        if (c=='Y' or c=='y'):
            ch=True
        elif (c=='N' or c=='n'):
            ch=False
        else:
            break

if __name__ == "__main__":
    main()
