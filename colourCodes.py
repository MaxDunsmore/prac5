"""
CP1404 Practical
Colour codes in a dictionary
"""

colour_codes = {"alice blue": "f0f8ff", "beige": "f5fdc", "black": "000000", "aquamarine": "7fffdf", "brown": "a52a2a", "Cadet Blue": "5f9ea0", "chocolate": "d2691e"}
colour = input("Please enter a colour: ").lower()
while colour != "":
    if colour in colour_codes:
        print("The colour code for {} is {}.".format(colour,colour_codes[colour]))
        colour = input("Please enter a colour: ").lower()
