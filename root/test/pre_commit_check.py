"""This File created to Learn the pre-commit check"""
from __future__ import annotations


class Calculator:
    """Calculator Class"""

    def __init__(self):
        """Init of Calculator Class"""
        print("Executed the Init of the class A")

    def fun(self):
        """This method is to print the name of class"""
        print("Class A")

    def sum(self, a: int, b: int):
        """
        This method returns the Sum.

        Args:
            a: First Number
            b: Second Number

        Returns:
            int: sum result
        """
        return a + b
