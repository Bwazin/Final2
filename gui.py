from tkinter import *
from mathLogic import *
'''
Import statement 1 imports everything from tkinter to be able to create
    the gui
Import statement 2 imports everything from mathLogic to be able to 
    use the functions within the file
'''

class GUI:
    """
    Class representing the graphical user interface of the application.
    """

    def __init__(self, window):
        """
        Initialize the GUI class.

        Parameters:
            window (Tk): The main Tkinter window.

        Attributes:
            window (Tk): The main Tkinter window.
            self.number_save1 (str): String to store the first part of the equation.
            self.number_save2 (str): String to store the second part of the equation.
            self.number_iteration (int): Tracks what part of the equation the program is on.
            self.equation_type_str (str): String to store the type of equation
                (e.g., addition, subtraction).
            self.equal_pressed (bool): Flag to indicate if the equal button has been pressed.
            self.counter (int): Counter for keeping track of events.
            self.frame_one (Frame): Frame for containing the input/output label.
            self.label_input_output (Label): Label for displaying input/output text.
            self.frame_two (Frame): Frame for containing buttons related to operations.
            self.button_percentage (Button): Button for percentage calculation.
            self.button_CE (Button): Button for clearing the current entry.
            self.button_c (Button): Button for clearing all entries.
            self.button_delete (Button): Button for deleting the last entered digit.
            self.frame_three (Frame): Frame for containing buttons related to operations.
            self.button_factorial_logic (Button): Button for power calculation
            self.button_power (Button): Button for doing power of 2 calculation
            self.button_log (Button): Button for log calculations
                space for area and perimeter calculations
            self.button_division (Button): Button for doing division calculations
            self.frame_four (Frame): Frame for containing buttons related to operations.
            self.button_7 (Button): Button for displaying the number 7
            self.button_8 (Button): Button for displaying the number 8
            self.button_9 (Button): Button for displaying the number 9
            self.button_multiplication (Button): Button for doing multiplication calculations
            self.frame_five (Frame): Frame for containing buttons related to operations.
            self.button_4 (Button): Button for displaying the number 4
            self.button_5 (Button): Button for displaying the number 5
            self.button_6 (Button): Button for displaying the number 6
            self.button_subtraction (Button): Button for doing subtraction calculations
            self.frame_six (Frame): Frame for containing buttons related to operations.
            self.button_1 (Button): Button for displaying the number 1
            self.button_2 (Button): Button for displaying the number 2
            self.button_3 (Button): Button for displaying the number 3
            self.button_addition (Button): Button for doing addition calculations
            self.frame_seven (Frame): Frame for containing buttons related to operations.
            self.button_plus_minus (Button): Button for changing the sign of the number
            self.button_0 (Button): Button for displaying the number 0
            self.button_dot (Button): Button for adding a decimal to the number
            self.button_equal (Button): Button for solving equations
            self.frame_eight (Frame): Frame for containing buttons related to operations.
            self.radio_answer (Variable): Variable that holds which radio button is pressed
            self.radio_square (Radio): Radio for displaying the options for a square
            self.radio_rectangle (Radio): Radio for displaying the options for a rectangle
            self.radio_triangle (Radio): Radio for displaying the options for a triangle
            self.radio_circle (Radio): Radio for displaying the options for a circle
            self.frame_nine (Frame): Frame for containing buttons related to operations.
            self.radio_option_1 (Radio): Radio for displaying the options
            self.radio_option_2 (Radio): Radio for displaying the options
            self.radio_answer_2 (Variable): Variable that holds which radio button is pressed
            self.frame_ten (Frame): Frame for containing buttons related to operations.
            self.label_textbox_1 (Label): Label for displaying what to inpout
            self.label_textbox_2 (Label): Label for displaying what to inpout
            self.label_textbox_3 (Label): Label for displaying what to inpout
            self.frame_eleven (Frame): Frame for containing buttons related to operations.
            self.label_results (Label): Label for displaying the results
            self.button_action (Button): Button for solving equations
            self.frame_twelve (Frame): Frame for containing buttons related to operations.
        """
        self.window = window
        self.window.configure()  # Configuring the main window
        self.number_save1 = ''  # Initializing first number storage
        self.number_save2 = ''  # Initializing second number storage
        self.number_iteration = 1  # Initializing number iteration
        self.equation_type_str = ''  # Initializing equation type string
        self.equal_pressed = False  # Initializing equal button press flag
        self.counter = 0  # Initializing counter for events

        # Creating the first frame for input/output
        self.frame_one = Frame(self.window, bg='grey', height=100)
        # Creating the label for input/output
        self.label_input_output = Label(self.frame_one, text='', bg='light grey', fg='white',
                                        font=('Arial', 24, 'bold'), anchor='e', padx=15)
        self.label_input_output.pack(fill='both', expand=True, padx=8, pady=8)  # Packing the label
        self.frame_one.pack(fill='x')  # Packing the frame

        """
        Configuration for Frame 1:
            - bg (str): Background color of the frame.
            - height (int): Height of the frame in pixels.
        """
        """
        Configuration for label_input_output (Label):
            - text (str): Text to display on the label.
            - bg (str): Background color of the label.
            - fg (str): Text color of the label.
            - font (tuple): Font settings for the label.
            - anchor (str): Alignment of the text within the label.
            - pad x (int): Horizontal padding of the label.
        """

        # Creating a frame to contain the buttons
        self.frame_two = Frame(self.window)

        # Creating the button for percentage calculation
        self.button_percentage = Button(self.frame_two, text='%', bg='orange', fg='white',
                                        font=('Arial', 24, 'bold'), width=7, command=lambda: self.percentage_logic())
        self.button_percentage.pack(side='left')  # Packing the button to the left of the frame

        # Creating the button for clearing the current entry
        self.button_CE = Button(self.frame_two, text='CE', bg='orange', fg='white',
                                font=('Arial', 24, 'bold'), width=7, command=lambda: self.ce_logic())
        self.button_CE.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        # Creating the button for clearing all entries
        self.button_c = Button(self.frame_two, text='C', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.c_logic())
        self.button_c.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        # Creating the button for deleting the last entered digit
        self.button_delete = Button(self.frame_two, text='❌', bg='orange', fg='white',
                                    font=('Arial', 24, 'bold'), width=7, command=lambda: self.delete_num())
        self.button_delete.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        # Packing the frame containing the buttons
        self.frame_two.pack(pady=1)  # Adding padding to the bottom of the frame

        self.frame_three = Frame(self.window)
        self.button_factorial = Button(self.frame_three, text='!', bg='orange', fg='white',
                                       font=('Arial', 24, 'bold'), width=7, command=lambda: self.factorial_logic())
        self.button_factorial.pack(side='left')  # Packing the button to the left of the frame

        self.button_power = Button(self.frame_three, text='x^2', bg='orange', fg='white',
                                   font=('Arial', 24, 'bold'), width=7, command=lambda: self.power_of_two())
        self.button_power.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_log = Button(self.frame_three, text='log', bg='orange', fg='white',
                                            font=('Arial', 24, 'bold'), width=7, command=lambda: self.log_logic())
        self.button_log.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_division = Button(self.frame_three, text='/', bg='orange', fg='white',
                                      font=('Arial', 24, 'bold'), width=7, command=lambda: self.equation_type('/'))
        self.button_division.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.frame_three.pack(pady=1)  # Adding padding to the bottom of the frame

        self.frame_four = Frame(self.window)
        self.button_7 = Button(self.frame_four, text='7', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('7'))
        self.button_7.pack(side='left')  # Packing the button to the left of the frame

        self.button_8 = Button(self.frame_four, text='8', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('8'))
        self.button_8.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_9 = Button(self.frame_four, text='9', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('9'))
        self.button_9.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_multiplication = Button(self.frame_four, text='*', bg='orange', fg='white',
                                            font=('Arial', 24, 'bold'), width=7,
                                            command=lambda: self.equation_type('*'))
        self.button_multiplication.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.frame_four.pack(pady=1)  # Adding padding to the bottom of the frame

        self.frame_five = Frame(self.window)
        self.button_4 = Button(self.frame_five, text='4', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('4'))
        self.button_4.pack(side='left')  # Packing the button to the left of the frame

        self.button_5 = Button(self.frame_five, text='5', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('5'))
        self.button_5.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_6 = Button(self.frame_five, text='6', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('6'))
        self.button_6.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_subtraction = Button(self.frame_five, text='-', bg='orange', fg='white',
                                         font=('Arial', 24, 'bold'), width=7, command=lambda: self.equation_type('-'))
        self.button_subtraction.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.frame_five.pack(pady=1)  # Adding padding to the bottom of the frame

        self.frame_six = Frame(self.window)
        self.button_1 = Button(self.frame_six, text='1', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('1'))
        self.button_1.pack(side='left')  # Packing the button to the left of the frame

        self.button_2 = Button(self.frame_six, text='2', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('2'))
        self.button_2.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_3 = Button(self.frame_six, text='3', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('3'))
        self.button_3.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_addition = Button(self.frame_six, text='+', bg='orange', fg='white',
                                      font=('Arial', 24, 'bold'), width=7, command=lambda: self.equation_type('+'))
        self.button_addition.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.frame_six.pack(pady=1)  # Adding padding to the bottom of the frame

        self.frame_seven = Frame(self.window)
        self.button_plus_minus = Button(self.frame_seven, text='+/-', bg='orange', fg='white',
                                        font=('Arial', 24, 'bold'), width=7, command=lambda: self.negative_plus_sign())
        self.button_plus_minus.pack(side='left')  # Packing the button to the left of the frame

        self.button_0 = Button(self.frame_seven, text='0', bg='orange', fg='white',
                               font=('Arial', 24, 'bold'), width=7, command=lambda: self.display_num('0'))
        self.button_0.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_dot = Button(self.frame_seven, text='.', bg='orange', fg='white',
                                 font=('Arial', 24, 'bold'), width=7, command=lambda: self.period())
        self.button_dot.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.button_equal = Button(self.frame_seven, text='=', bg='orange', fg='white',
                                   font=('Arial', 24, 'bold'), width=7, command=lambda: self.equal_sign())
        self.button_equal.pack(side='left', padx=2)  # Packing the button to the left of the frame with padding

        self.frame_seven.pack(pady=1)  # Adding padding to the bottom of the frame

        # Create a new frame for the radio buttons
        self.frame_eight = Frame(self.window)

        # Create an integer variable to hold the selected radio button value and set its initial value to 0
        self.radio_answer = IntVar()
        self.radio_answer.set(0)

        # Create radio buttons for different shapes and assign them to the frame
        self.radio_square = Radiobutton(self.frame_eight, text='Square',
                                        variable=self.radio_answer, value=1, command=lambda: self.hide_show_options(self.radio_answer.get()))
        self.radio_square.pack(pady=10, side='left')
        self.radio_rectangle = Radiobutton(self.frame_eight, text='Rectangle',
                                           variable=self.radio_answer, value=2, command=lambda: self.hide_show_options(self.radio_answer.get()))
        self.radio_rectangle.pack(pady=10, side='left')
        self.radio_triangle = Radiobutton(self.frame_eight, text='Triangle',
                                          variable=self.radio_answer, value=3, command=lambda: self.hide_show_options(self.radio_answer.get()))
        self.radio_triangle.pack(pady=10, side='left')
        self.radio_circle = Radiobutton(self.frame_eight, text='Circle',
                                        variable=self.radio_answer, value=4, command=lambda: self.hide_show_options(self.radio_answer.get()))
        self.radio_circle.pack(pady=10, side='left')

        # Pack the frame to display the radio buttons
        self.frame_eight.pack()

        # Create another frame for the second set of radio buttons
        self.frame_nine = Frame(self.window)

        # Create an integer variable for the second set of radio buttons and set its initial value to 0
        self.radio_answer_2 = IntVar()
        self.radio_answer_2.set(0)

        # Create radio buttons for selecting the calculation type (perimeter or area) and assign them to the frame
        self.radio_option1 = Radiobutton(self.frame_nine, text='Perimeter', variable=self.radio_answer_2, value=1, command=lambda: self.hide_show_options(self.radio_answer.get(), self.radio_answer_2.get()))
        self.radio_option1.pack(pady=10, side='left')
        self.radio_option2 = Radiobutton(self.frame_nine, text='Area', variable=self.radio_answer_2, value=2, command=lambda: self.hide_show_options(self.radio_answer.get(), self.radio_answer_2.get()))
        self.radio_option2.pack(pady=10, side='left')

        # Create a frame to contain the labels and entry boxes
        self.frame_ten = Frame(self.window)
        self.validate_numeric = (window.register(self.on_validate_numeric), '%P')

        # Label and entry for side1
        self.label_textbox_1 = Label(self.frame_ten, text='side1', bg='light grey', fg='white',
                                     font=('Arial', 20, 'bold'), padx=5)

        self.entry_box_1 = Entry(self.frame_ten, validate="key", validatecommand=self.validate_numeric, bg='light grey', fg='white',
                                 font=('Arial', 20, 'bold'), width=3)  # Adjust width if necessary

        # Label and entry for side2
        self.label_textbox_2 = Label(self.frame_ten, text='side2', bg='light grey', fg='white',
                                     font=('Arial', 20, 'bold'), padx=5)

        self.entry_box_2 = Entry(self.frame_ten, validate="key", validatecommand=self.validate_numeric, bg='light grey', fg='white',
                                 font=('Arial', 20, 'bold'), width=3)  # Adjust width if necessary

        # Label and entry for side3
        self.label_textbox_3 = Label(self.frame_ten, text='side3', bg='light grey', fg='white',
                                     font=('Arial', 20, 'bold'), padx=5)

        self.entry_box_3 = Entry(self.frame_ten, validate="key", validatecommand=self.validate_numeric, bg='light grey', fg='white',
                                 font=('Arial', 20, 'bold'), width=3)  # Adjust width if necessary

        # Create a frame to contain the result label
        self.frame_eleven = Frame(self.window)

        # Create a button to display the result
        self.button_action = Button(self.frame_eleven, text='RESULT', bg='light grey', fg='white',
                                     font=('Arial', 10, 'bold'), padx=5, command=lambda: self.solver())
        self.button_action.pack()

        # Create a frame to contain the result label
        self.frame_twelve = Frame(self.window)

        # Create a label for displaying the result
        self.label_result = Label(self.frame_twelve, text='', bg='light grey', fg='white',
                                  font=('Arial', 20, 'bold'), padx=15)  # Increased font size to 20
        self.label_result.pack()


        """
            Configuration for buttons in frames (Button):
                - text (str): Text displayed on the button.
                - bg (str): Background color of the button.
                - fg (str): Text color of the button.
                - font (tuple): Font settings for the button text.
                - width (int): Width of the button in characters.
                - command (function): Callback function to execute when the button is clicked.
        """

    def display_num(self, num):
        """
        Display the entered number on the calculator interface.

        Parameters:
            num (str): The number to be displayed.

        Description:
            - If the entered number is 0 and there are no saved numbers in the first part of the equation
              and the program is on the first iteration, do nothing.
            - If the entered number is 0 and there are no saved numbers in the second part of the equation
              and the program is on the second iteration, do nothing.
            - If the equal button is pressed and the program is on the second iteration, clear the interface
              and display the entered number as the new first part of the equation.
            - If the program is on the second iteration, add the entered number to the second part of the equation.
            - If the counter is set to 1, reset it to 0 and display the entered number as the first part of the equation.
            - Otherwise, add the entered number to the first part of the equation.

        Returns:
            None
        """
        if int(num) == 0 and len(self.number_save1) == 0 and self.number_iteration == 1:
            return
        elif int(num) == 0 and len(self.number_save2) == 0 and self.number_iteration == 2:
            return
        elif self.equal_pressed == True and self.number_iteration == 2:
            self.erase()
            self.number_save1 = num
            self.label_input_output.config(text=f'{self.number_save1}')
        elif self.number_iteration == 2:
            self.number_save2 = self.number_save2 + num
            self.label_input_output.config(text=f'{self.number_save2}')
        elif self.counter == 1:
            self.counter = 0
            self.number_save1 = num
            self.label_input_output.config(text=f'{self.number_save1}')
        else:
            self.number_save1 = self.number_save1 + num
            self.label_input_output.config(text=f'{self.number_save1}')

    def delete_num(self):
        """
        Delete the last entered digit or decimal point from the displayed number.

        Description:
            - If the program is on the second iteration and there are digits or a decimal point
              in the second part of the equation, remove the last character from it.
            - If the counter is set, clear the interface and reset the counter.
            - If the program is on the first iteration and there are digits or a decimal point
              in the first part of the equation, remove the last character from it.
            - If the equal button is pressed, clear the interface.

        Returns:
            None
        """
        # If on the second iteration and there are digits or a decimal point in the second part
        # of the equation, remove the last character
        if self.number_iteration == 2 and (self.number_save2 != '' or self.number_save2 == '.'):
            self.number_save2 = self.number_save2[:-1]
            self.label_input_output.config(text=f'{self.number_save2}')
        # If the counter is set, clear the interface and reset the counter
        elif self.counter == 1:
            self.erase()
            self.counter = 0
        # If on the first iteration and there are digits or a decimal point in the first part
        # of the equation, remove the last character
        elif self.number_iteration == 1 and (self.number_save1 != '' or self.number_save1 == '.'):
            self.number_save1 = self.number_save1[:-1]
            self.label_input_output.config(text=f'{self.number_save1}')
        # If the equal button is pressed, clear the interface
        elif self.equal_pressed == True:
            self.erase()

    def equation_type(self, type):
        """
        Set the type of equation and perform calculation if both numbers are entered.

        Parameters:
            type (str): The type of equation (e.g., '+', '-', '*', '/').

        Description:
            - Set the equation type to the specified type.
            - If the program is on the second iteration and both numbers are entered,
              perform the calculation based on the equation type and update the displayed result.
            - If the program is on the second iteration, reset the equal button press flag.
            - If only the decimal point is entered, clear the equation type.
            - If the first number is not entered, set the equation type and move to the second iteration.

        Returns:
            None
        """
        self.equation_type_str = type

        # Check if both numbers are entered for calculation
        if self.number_iteration == 2 and self.number_save2 != '' and (
                self.number_save2 != '.' or self.number_save2 != '-' or self.number_save2 != '-.'):
            # Perform calculation based on equation type
            if self.equation_type_str == '+':
                if '.' in self.number_save1 or '.' in self.number_save2:
                    self.conclusion = str(addition(float(self.number_save1), float(self.number_save2)))
                else:
                    self.conclusion = str(addition(int(self.number_save1), int(self.number_save2)))
            elif self.equation_type_str == '-':
                if '.' in self.number_save1 or '.' in self.number_save2:
                    self.conclusion = str(subtraction(float(self.number_save1), float(self.number_save2)))
                else:
                    self.conclusion = str(subtraction(int(self.number_save1), int(self.number_save2)))
            elif self.equation_type_str == '/':
                if '.' in self.number_save1 or '.' in self.number_save2:
                    self.conclusion = str(division(float(self.number_save1), float(self.number_save2)))
                else:
                    self.conclusion = str(division(int(self.number_save1), int(self.number_save2)))
                if self.conclusion == 'error':
                    self.error()
            elif self.equation_type_str == '*':
                if '.' in self.number_save1 or '.' in self.number_save2:
                    self.conclusion = str(multiplication(float(self.number_save1), float(self.number_save2)))
                else:
                    self.conclusion = str(multiplication(int(self.number_save1), int(self.number_save2)))

            # Update the first number and reset the second number
            self.number_save1 = self.conclusion
            self.number_save2 = ''
            # Display the result with rounding if necessary
            if '.' in self.number_save1:
                self.label_input_output.config(text=f'{round(float(self.number_save1), 3)}')
            else:
                self.label_input_output.config(text=f'{self.number_save1}')

        # Reset the equal button press flag
        elif self.number_iteration == 2:
            self.equal_pressed = False
        # Clear the equation type if only the decimal point is entered
        elif self.number_save1 == '.':
            self.equation_type_str = ''
        # Set the equation type and move to the second iteration
        else:
            self.equation_type_str = type
            self.number_iteration += 1

    def period(self):
        """
        Add a decimal point to the displayed number.

        Description:
            - If on the first iteration and there is no decimal point in the first number,
              add a decimal point to it and update the display.
            - If on the second iteration and there is no decimal point in the second number,
              add a decimal point to it and update the display.

        Returns:
            None
        """
        # Check if on the first iteration and there is no decimal point in the first number
        if self.number_iteration == 1 and ('.' not in self.number_save1):
            # Add a decimal point to the first number and update the display
            self.number_save1 = self.number_save1 + '.'
            self.label_input_output.config(text=f'{self.number_save1}')
        # Check if on the second iteration and there is no decimal point in the second number
        elif self.number_iteration == 2 and ('.' not in self.number_save2):
            # Add a decimal point to the second number and update the display
            self.number_save2 = self.number_save2 + '.'
            self.label_input_output.config(text=f'{self.number_save2}')

    def negative_plus_sign(self):
        """
        Handle adding or removing a negative sign from the displayed number.

        Description:
            - If on the first iteration and there is no negative sign in the first number,
              add a negative sign to it and update the display.
            - If on the first iteration and there is a negative sign in the first number,
              remove the negative sign from it and update the display.
            - If on the second iteration and the equal button is pressed,
              reset to the first iteration and recursively call the function.
            - If on the second iteration and there is no negative sign in the second number,
              add a negative sign to it and update the display.
            - If on the second iteration and there is a negative sign in the second number,
              remove the negative sign from it and update the display.

        Returns:
            None
        """
        # Check if on the first iteration and there is no negative sign in the first number
        if self.number_iteration == 1 and ('-' not in self.number_save1):
            # Add a negative sign to the first number and update the display
            self.number_save1 = '-' + self.number_save1
            self.label_input_output.config(text=f'{self.number_save1}')
        # Check if on the first iteration and there is a negative sign in the first number
        elif self.number_iteration == 1 and ('-' in self.number_save1):
            # Remove the negative sign from the first number and update the display
            self.number_save1 = self.number_save1.replace('-', '', 1)
            self.label_input_output.config(text=f'{self.number_save1}')
        # Check if on the second iteration and the equal button is pressed
        elif self.number_iteration == 2 and self.equal_pressed == True:
            # Reset to the first iteration and recursively call the function
            self.number_iteration -= 1
            self.equal_pressed = False
            self.negative_plus_sign()
        # Check if on the second iteration and there is no negative sign in the second number
        elif self.number_iteration == 2 and ('-') not in self.number_save2:
            # Add a negative sign to the second number and update the display
            self.number_save2 = '-' + self.number_save2
            self.label_input_output.config(text=f'{self.number_save2}')
        # Check if on the second iteration and there is a negative sign in the second number
        elif self.number_iteration == 2 and ('-') in self.number_save2:
            # Remove the negative sign from the second number and update the display
            self.number_save2 = self.number_save2.replace('-', '', 1)
            self.label_input_output.config(text=f'{self.number_save2}')

    def equal_sign(self):
        """
        Handle the functionality of the equal sign button.

        Description:
            - If on the second iteration, the second number is not empty, and the equal button
              is not pressed yet, call the equation_type function to perform the calculation.

        Returns:
            None
        """
        # Check if on the second iteration, the second number is not empty, and the equal button is not pressed yet
        if self.number_iteration == 2 and self.number_save2 != '' and self.equal_pressed == False and self.number_save2 != '.':
            # Set the equal_pressed flag to True
            self.equal_pressed = True
            # Call the equation_type function to perform the calculation
            self.equation_type(self.equation_type_str)

    def power_of_two(self):
        """
        Handle the functionality of raising a number to the power of two.

        Description:
            - If on the first iteration and the first number is not empty, call the power function
              to calculate the square of the number and update the display.
            - If on the second iteration and the second number is not empty, call the power function
              to calculate the square of the number and update the display.

        Returns:
            None
        """
        # Check if on the first iteration and the first number is not empty
        if self.number_iteration == 1 and self.number_save1 != '' and self.number_save1 != '.':
            # Calculate the square of the number and update the display
            if '.' in self.number_save1:
                self.number_save1 = str(power(float(self.number_save1)))
                self.label_input_output.config(text=f'{self.number_save1}')
                self.counter = 1
            else:
                self.number_save1 = str(power(int(self.number_save1)))
                self.label_input_output.config(text=f'{self.number_save1}')
                self.counter = 1
        # Check if on the second iteration and the second number is not empty
        elif self.number_iteration == 2 and self.number_save2 != '' and self.number_save2 != '.':
            # Calculate the square of the number and update the display
            if '.' in self.number_save2:
                self.number_save2 = str(power(float(self.number_save2)))
                self.label_input_output.config(text=f'{self.number_save2}')
            else:
                self.number_save2 = str(power(int(self.number_save2)))
                self.label_input_output.config(text=f'{self.number_save2}')

    def factorial_logic(self):
        """
        Handle the functionality of calculating the factorial of a number.

        Description:
            - If on the first iteration and the first number is not empty, call the factorial function
              to calculate the factorial of the number and update the display.
            - If on the second iteration and the second number is not empty, call the factorial function
              to calculate the factorial of the number and update the display.

        Returns:
            None
        """
        # Check if on the first iteration and the first number is not empty
        if self.number_iteration == 1 and self.number_save1 != '' and self.number_save1 != '.':
            # Calculate the factorial of the number and update the display
            if '.' not in self.number_save1:
                self.number_save1 = str(factorial(int(self.number_save1)))
                self.label_input_output.config(text=f'{self.number_save1}')
                self.counter = 1
        # Check if on the second iteration and the second number is not empty
        elif self.number_iteration == 2 and self.number_save2 != '' and self.number_save2 != '.':
            # Calculate the factorial of the number and update the display
            if '.' not in self.number_save2:
                self.number_save2 = str(factorial(int(self.number_save2)))
                self.label_input_output.config(text=f'{self.number_save2}')

    def percentage_logic(self):
        """
        Handle the functionality of calculating the percentage of a number.

        Description:
            - If on the first iteration and the first number is not empty, call the percentage function
              to calculate the percentage of the number and update the display.
            - If on the second iteration and the second number is not empty, call the percentage function
              to calculate the percentage of the number and update the display.

        Returns:
            None
        """
        # Check if on the first iteration and the first number is not empty
        if self.number_iteration == 1 and self.number_save1 != '' and self.number_save1 != '.':
            # Calculate the percentage of the number and update the display
            if '.' in self.number_save1:
                self.number_save1 = str(percentage(float(self.number_save1)))
                self.label_input_output.config(text=f'{self.number_save1}')
                self.counter = 1
            else:
                self.number_save1 = str(percentage(int(self.number_save1)))
                self.label_input_output.config(text=f'{self.number_save1}')
                self.counter = 1
        # Check if on the second iteration and the second number is not empty
        elif self.number_iteration == 2 and self.number_save2 != '' and self.number_save2 != '.':
            # Calculate the percentage of the number and update the display
            if '.' in self.number_save2:
                self.number_save2 = str(percentage(float(self.number_save2)))
                self.label_input_output.config(text=f'{self.number_save2}')
            else:
                self.number_save2 = str(percentage(int(self.number_save2)))
                self.label_input_output.config(text=f'{self.number_save2}')

    def c_logic(self):
        """
        Clear the current entry or the entire interface.

        Description:
            - If the program is on the first iteration, clear the current entry by resetting the first number
              and updating the display.
            - If the program is on the second iteration, clear the entire interface.

        Returns:
            None
        """
        if self.number_iteration == 1:
            # If on the first iteration, clear the current entry by resetting the first number
            # and updating the display
            self.number_save1 = ''
            self.label_input_output.config(text=f'{self.number_save1}')
        else:
            # If on the second iteration, clear the entire interface
            self.erase()

    def ce_logic(self):
        """
        Clear the current entry or the entire interface, depending on the iteration.

        Description:
            - If the program is on the first iteration, clear the entire interface.
            - If the program is on the second iteration, clear the current entry by resetting the second number
              and updating the display.

        Returns:
            None
        """
        if self.number_iteration == 1:
            # If on the first iteration, clear the entire interface
            self.erase()
        else:
            # If on the second iteration, clear the current entry by resetting the second number
            # and updating the display
            self.number_save2 = ''
            self.label_input_output.config(text=f'{self.number_save2}')

    def error(self):
        """
        Handle error condition by displaying 'error' and resetting the calculator.

        Description:
            - Calls the erase method to clear the interface and reset the calculator.
            - Displays 'error' on the input/output label.

        Returns:
            None
        """
        self.erase()  # Call erase to reset the calculator
        self.label_input_output.config(text='error')  # Display 'error' on the input/output label

    def erase(self):
        """
        Clear the interface and reset the calculator.

        Description:
            - Reset various attributes such as the equal button flag, saved numbers, number iteration, and equation type.
            - Update the input/output label to reflect the cleared state.

        Returns:
            None
        """
        self.equal_pressed = False  # Reset equal button press flag
        self.number_save1 = ''  # Reset first number storage
        self.number_save2 = ''  # Reset second number storage
        self.number_iteration = 1  # Reset number iteration
        self.equation_type_str = ''  # Reset equation type string
        self.label_input_output.config(text=f'{self.number_save1}')  # Update input/output label

    def log_logic(self):
        # Check if on the first iteration and the first number is not empty
        if self.number_iteration == 1 and self.number_save1 != '' and self.number_save1 != '.':
            # Calculate the factorial of the number and update the display
            if '.' not in self.number_save1:
                self.number_save1 = str(log(int(self.number_save1)))
                self.label_input_output.config(text=f'{self.number_save1}')
                self.counter = 1
        # Check if on the second iteration and the second number is not empty
        elif self.number_iteration == 2 and self.number_save2 != '' and self.number_save2 != '.':
            # Calculate the factorial of the number and update the display
            if '.' not in self.number_save2:
                self.number_save2 = str(log(int(self.number_save2)))
                self.label_input_output.config(text=f'{self.number_save2}')

    def on_validate_numeric(self, new_text):
        """
        Validation function to allow only numeric input.

        Parameters:
            new_text (str): The new text to be validated.

        Returns:
            bool: True if the new text contains only digits or is empty, False otherwise.
        """
        # Check if the new text contains only digits
        return new_text.isdigit() or new_text == ''

    def hide_show_options(self, value1, value2=0):
        """
        Hide or show options based on the selected values.

        Parameters:
            value1 (int): The value of the first option.
            value2 (int, optional): The value of the second option. Defaults to 0.
        """
        # Hide or show options based on selected values
        if value1 == 1 and value2 == 1:
            self.label_textbox_2.pack_forget()
            self.entry_box_2.pack_forget()
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Side')
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 1 and value2 == 2:
            self.label_textbox_2.pack_forget()
            self.entry_box_2.pack_forget()
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Side')
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 2 and value2 == 1:
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Side 1')
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_2.pack(side='left', padx=5, pady=10)
            self.label_textbox_2.config(text='Side 2')
            self.entry_box_2.pack(side='left', padx=5, pady=10)
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 2 and value2 == 2:
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Side 1')
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_2.pack(side='left', padx=5, pady=10)
            self.label_textbox_2.config(text='Side 2')
            self.entry_box_2.pack(side='left', padx=5, pady=10)
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 3 and value2 == 1:
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Side 1')
            self.label_textbox_2.pack(side='left', padx=5, pady=10)
            self.entry_box_2.pack(side='left', padx=5, pady=10)
            self.label_textbox_2.config(text='Side 2')
            self.label_textbox_3.pack(side='left', padx=5, pady=10)
            self.entry_box_3.pack(side='left', padx=5, pady=10)
            self.label_textbox_3.config(text='Side 3')
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 3 and value2 == 2:
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Base')
            self.label_textbox_2.pack(side='left', padx=5, pady=10)
            self.entry_box_2.pack(side='left', padx=5, pady=10)
            self.label_textbox_2.config(text='Height')
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 4 and value2 == 1:
            self.label_textbox_2.pack_forget()
            self.entry_box_2.pack_forget()
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Radius')
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 4 and value2 == 2:
            self.label_textbox_2.pack_forget()
            self.entry_box_2.pack_forget()
            self.label_textbox_3.pack_forget()
            self.entry_box_3.pack_forget()
            self.entry_box_1.delete(0, 'end')
            self.entry_box_2.delete(0, 'end')
            self.entry_box_3.delete(0, 'end')

            self.label_textbox_1.pack(side='left', padx=5, pady=10)
            self.entry_box_1.pack(side='left', padx=5, pady=10)
            self.label_textbox_1.config(text='Radius')
            self.frame_ten.pack()
            self.frame_eleven.pack()
        elif value1 == 1:
            self.frame_ten.pack_forget()
            self.frame_eleven.pack_forget()
            self.frame_twelve.pack_forget()

            self.radio_option1.config(text='Perimeter')
            self.radio_option2.config(text='Area')
            self.radio_answer_2.set(0)
            self.frame_nine.pack()
        elif value1 == 2:
            self.frame_ten.pack_forget()
            self.frame_eleven.pack_forget()
            self.frame_twelve.pack_forget()

            self.radio_option1.config(text='Perimeter')
            self.radio_option2.config(text='Area')
            self.radio_answer_2.set(0)
            self.frame_nine.pack()
        elif value1 == 3:
            self.frame_ten.pack_forget()
            self.frame_eleven.pack_forget()
            self.frame_twelve.pack_forget()

            self.radio_option1.config(text='Perimeter')
            self.radio_option2.config(text='Area')
            self.radio_answer_2.set(0)
            self.frame_nine.pack()
        elif value1 == 4:
            self.frame_ten.pack_forget()
            self.frame_eleven.pack_forget()
            self.frame_twelve.pack_forget()

            self.radio_option1.config(text='Circumference')
            self.radio_option2.config(text='Area')
            self.radio_answer_2.set(0)
            self.frame_nine.pack()

    def solver(self):
        """
        Solve the geometry problem based on the selected shape and calculation option.
        """
            # Determine the selected shape and calculation option, then compute and display the result
        if self.radio_answer.get() == 1 and self.radio_answer_2.get() == 1:
            self.display_result(str(perimeter_of_square(int(self.entry_box_1.get()))))
        elif self.radio_answer.get() == 1 and self.radio_answer_2.get() == 2:
            self.display_result(str(area_of_square(int(self.entry_box_1.get()))))
        elif self.radio_answer.get() == 2 and self.radio_answer_2.get() == 1:
            self.display_result(str(perimeter_of_rectangle(int(self.entry_box_1.get()), int(self.entry_box_2.get()))))
        elif self.radio_answer.get() == 2 and self.radio_answer_2.get() == 2:
            self.display_result(str(area_of_rectangle(int(self.entry_box_1.get()), int(self.entry_box_2.get()))))
        elif self.radio_answer.get() == 3 and self.radio_answer_2.get() == 1:
            self.display_result(str(perimeter_of_triangle(int(self.entry_box_3.get()), int(self.entry_box_2.get()), int(self.entry_box_3.get()))))
        elif self.radio_answer.get() == 3 and self.radio_answer_2.get() == 2:
            self.display_result(str(area_of_triangle(int(self.entry_box_1.get()), int(self.entry_box_2.get()))))
        elif self.radio_answer.get() == 4 and self.radio_answer_2.get() == 1:
            self.display_result(str(circumference_of_circle(int(self.entry_box_1.get()))))
        elif self.radio_answer.get() == 4 and self.radio_answer_2.get() == 2:
            self.display_result(str(area_of_circle(int(self.entry_box_1.get()))))

    def display_result(self, num):
        """
        Display the result in the label.

        Parameters:
          num (str): The result to be displayed.
        """
        self.label_result.configure(text=f'{num}')
        self.frame_twelve.pack(pady=5)


