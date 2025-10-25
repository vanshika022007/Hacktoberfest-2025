#!/usr/bin/env python3
"""
Test file to demonstrate the Python Linter Workflow
This file contains some intentional style issues for testing purposes.
"""

import os
import sys


def hello_world():
    """A simple function to test the linter."""
    message = "Hello, World!"
    print(message)
    return message


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def main():
    """Main function to run the test."""
    hello_world()
    result = calculate_sum(5, 10)
    print(f"The sum is: {result}")
    print("This file is used to test the Python Linter Workflow.")

if __name__ == "__main__":
    main()