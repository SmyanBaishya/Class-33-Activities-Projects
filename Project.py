class IntegerToRoman:

    def __init__(self):

        # Mapping of integer values to Roman numeral symbols

        self.value_map = [

            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),

            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),

            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')

        ]

    

    def int_to_roman(self, num):

        roman_numeral = ''

        for value, symbol in self.value_map:

            while num >= value:

                roman_numeral += symbol

                num -= value

        return roman_numeral



# Example usage:

converter = IntegerToRoman()



# Get user input and convert it to an integer

user_input = input("Enter a positive integer to convert to Roman numeral: ")



# Check if input is a positive integer

if user_input.isdigit() and int(user_input) > 0:

    num = int(user_input)

    print("Roman numeral:", converter.int_to_roman(num))

else:

    print("Please enter a valid positive integer.")