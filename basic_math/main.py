"""
MIT License

Copyright (c) 2024 Dennis A. Torres <d70rr3s@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random
import os


def generate_expression():
    operations = ['+', '-', '*', '/']
    while True:
        # Randomly generate numbers
        a, b, c, d = random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)

        # Randomly select operations
        op1, op2, op3 = random.choice(operations), random.choice(operations), random.choice(operations)

        # Create an expression using random operations
        expression = f'({a} {op1} {b}) {op2} ({c} {op3} {d})'
        try:
            result = eval(expression)
            if isinstance(result, float):
                result = round(result)
            result = abs(result)  # Get absolute value if negative
            # Ensure the result is a two-digit number
            if 10 <= result < 100:
                return f'{expression} = {result}'
        except ZeroDivisionError:
            # Skip expressions that result in division by zero
            continue


def main():
    passphrase = os.getenv('SHELDON')
    user_input = input("Enter the passphrase to view the results: ")
    if user_input == passphrase:
        # Generate and print three expressions with results
        for _ in range(3):
            expression = generate_expression()
            print(expression)
    else:
        # Generate and print three expressions without results
        for _ in range(3):
            expression = generate_expression()
            print(expression.split('=')[0].strip())


if __name__ == "__main__":
    main()
