'''
Question 2: Write a Python program using nested loops to find pairs of numbers from a
given list that sum up to 16. Display the pairs of numbers that satisfy this condition.
Write a Python program that accomplishes the following:
Define a list of numbers: [2, 4, 6, 8, 10].
Implement nested loops to iterate through all possible combinations of numbers from the list.
Check if the sum of each pair of numbers equals 16.
If a pair is found, display the pair as output in the format: "Pair found: <number1> +
<number2>".
If no pair is found, display the message: "No pair found."
Example Output:
Pair found: 6 + 10

Pair found: 8 + 8
Ensure that your program handles the given list of numbers and produces the correct output for
pairs that sum up to 16.

'''

def solution2(input_list, pair_sum):
  for i in input_list:
    for j in input_list:
      if (i + j) == pair_sum:
        print(f'Pair Found: {i} + {j}')
  print('No pairs found')
  
print(solution2([2,4,6,8,10], 16))