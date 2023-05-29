"""CS 108 Lab 11.1

This module provides basic functionality for a calculator.


@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015 - replaced JUnit tests with assert tests
@date: Spring, 2020 - ported to ZyLabs

@author: Blessing Amoah (bsa5)
@date: fall, 2022

"""


class Calculator:

    def __init__(self):
        """ Initialize calculator memory to 0. """
        self.memory = 0 

    def calculate(self, operand1, operator, operand2):
        """ Perform the specified calculation. No error-checking is done for
        division by zero.
        """
        if operand1 == 'M':
            operand1 = self.memory
        if operand2 == 'M':
            operand2 = self.memory
             

        operand1 = float(operand1)
        operand2 = float(operand2)

        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        
    def set_memory(self,value):
        self.memory = value
           
            
            
            
