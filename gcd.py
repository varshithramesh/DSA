# -*- coding: utf-8 -*-
"""GCD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jz8cyjec38DGDvAuO-zBgdcXaXgf58G8
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Example usage:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))

