'''
Question 4: Write a Python function that calculates the sum of numbers from a given
string in the format "{6, 2, 15}". The function should extract the individual numbers,
convert them to integers, and return their sum.

Implement a Python function that accomplishes the following:
Accept a string as input, representing a list of numbers in the format "{6, 2, 15}".
Extract the individual numbers from the string, ignoring the braces and any whitespace.
Convert each extracted number to an integer.
Calculate the sum of the numbers.
Return the sum as the output.
Example:
If the input string is "{6, 2, 15}", the function should extract the numbers 6, 2, and 15, calculate
their sum (6 + 2 + 15 = 23), and return 23 as the output.

Ensure that your function correctly handles the given input format, converts the numbers to
integers, and accurately calculates and returns their sum.

'''

def solution4():

  input_str = input('Enter the input string in the format {6,2, 15}')

  try:
    if ('{' in input_str or '}' in input_str) and ' ' in input_str:
      input_str_clean = input_str.replace("{","").replace("}","").split(',')

    else:
      print("Enter valid input")

    final_input = [int(num) for num in input_str_clean]
    return sum(final_input)

  except Exception as error:
    print(error)
    
solution4()