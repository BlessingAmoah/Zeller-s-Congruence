"""CS 108 Lab 11.2

This module implements a basic calculator GUI.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020 - ported to ZyLabs
@date: Spring, 2021 - ported to GuiZero

@author: Blessing Amoah (ba5)
@date: Fall, 2022
"""

from guizero import App, Box, Text, TextBox, ButtonGroup, PushButton
from calculator import Calculator


class CalculatorApp:

    def __init__(self, app):
        """Build the Calculator interface."""

        # Configure the application GUI.
        app.title = 'Calculator'
        app.width = 300
        app.height = 200
        app.font = 'Helvetica'
        app.text_size = 12

        # Instantiate a single calculator object for repeated use.
        self.calculator = Calculator()

        # Add the operand-input widgets.
        box = Box(app, layout='grid')
        Text(box, text="Input 1:", grid=[0, 0], align='right')
        self.input1_entry = TextBox(box, width=6, grid=[1, 0], align='left')
        Text(box, text="Input 2:", grid=[0, 1], align='right')
        self.input2_entry = TextBox(box, width=6, grid=[1, 1], align='left')
        self.operator_choice = ButtonGroup(box, ('+','-','*','/'),grid = [0,2,2,1], horizontal=True)
        PushButton(box, text= 'Calculate', grid =[0,3], command = self.do_calculation)
        self.result_text= Text(box, grid=[1,3], text='', align= 'right')
        PushButton(box, text ='Memory', grid = [0,4], command = self.do_memory)
        self.memory_text= Text(box, grid=[1,4], text='', align= 'right')
        
        
    def do_calculation(self):
        result = self.calculator.calculate(self.input1_entry.value,
                                   self.operator_choice.value,
                                   self.input2_entry.value)
        
        self.result_text.value = result
        
    def do_memory(self):
        result = self.calculator.calculate(self.input1_entry.value,
                                   self.operator_choice.value,
                                   self.input2_entry.value)
        self.calculator.set_memory(result)
        self.memory_text.value = result
     
    
        
        

        



app = App()
CalculatorApp(app)
app.display()
