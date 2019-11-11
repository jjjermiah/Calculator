class Calculator:
    def __init__(self):
        self.numbers = []
        self.operations = []

    def calculate(self, calc):
        print(calc)
        answer = 0

        # BASE CASE
        if(type(calc) == int):
            return int(calc)
        elif(len(calc) == 3):
            if(calc[1]== "+"):
                return self.add(calc[0], calc[2])
            elif (calc[1] == "-"):
                return self.sub(calc[0], calc[2])
            elif (calc[1] == "*"):
                return self.mul(calc[0], calc[2])
            elif (calc[1] == "/"):
                return self.div(calc[0], calc[2])

        # Recursive Case
        else:
            if (calc.find("+") != -1):
                split = calc.split("+")
                return self.add(self.calculate(split[0]), self.calculate(split[1]))
            elif (calc.find("-") != 1):
                split = calc.split("-")
                return self.sub(self.calculate(split[0]), self.calculate(split[1]))
            elif (calc.find("*") != 1):
                split = calc.split("*")
                return self.mul(self.calculate(split[0]), self.calculate(split[1]))
            elif (calc.find("/") != 1):
                split = calc.split("/")
                return self.div(self.calculate(split[0]), self.calculate(split[1]))


    def add(self, num1, num2):
        return int(num1) + int(num2)

    def sub(self, num1, num2):
        return int(num1) - int(num2)

    def mul(self, num1, num2):
        return int(num1) * int(num2)

    def div(self, num1, num2):
        return int(num1)/int(num2)

calculation = Calculator();
print("your answer is ", calculation.calculate(input("Please give me a calculation with numbers 0-9\n")))

