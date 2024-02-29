from decimal import Decimal
from app.calculator import Calculator
from app.calculator.operations import subtract
from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        user_input1 = Decimal(input("> Num1: "))
        user_input2 = Decimal(input("> Num2: "))
        print(Calculator.subtract(user_input1, user_input2))