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
import pyperclip
import getpass


def generate_expression():
    while True:
        # Randomly generate single-digit numbers
        a, b, c, d = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)

        # Pair operations: multiplication with subtraction, and division with addition
        if b > a:
            a, b = b, a  # Ensure subtraction is valid
        if d == 0:
            d = random.randint(1, 9)  # Avoid division by zero
        if c % d != 0:
            continue  # Ensure division has no remainder

        # Create an expression using all operations
        expression = f'({a} * {b}) - ({c} / {d}) + {random.randint(1, 9)}'
        try:
            result = eval(expression)
            result = round(abs(result))  # Get absolute value if negative
            # Ensure the result is a two-digit number
            if 10 <= result < 100:
                return f'{expression} = {result}'
        except ZeroDivisionError:
            continue


def main():
    results = []
    for _ in range(3):
        expression = generate_expression()
        print(expression.split('=')[0].strip())
        results.append(expression.split('=')[1].strip())

    passphrase = os.getenv('SHELDON')
    user_input = getpass.getpass("Enter the passphrase to view the results: ")
    if user_input == passphrase:
        pyperclip.copy('\n'.join(results))
        print("Results have been copied to the clipboard.")


if __name__ == "__main__":
    main()
