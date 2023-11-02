# Fibonacci-Problem
This Python code calculates the nth Fibonacci number using an iterative method. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.

# Code Description
The code consists of a Solution class that contains a method fib to compute the Fibonacci number for a given value of n.

The fib method takes an integer n as input and returns the nth Fibonacci number. It uses an iterative approach to compute the Fibonacci number by initializing variables for the first two numbers in the sequence (0 and 1) and iteratively generating subsequent numbers until it reaches the desired nth value.

If n is 0 or 1, the method returns 0 or 1, respectively. For n greater than 1, it employs a loop to generate the Fibonacci number by iteratively updating the values until it reaches the desired index.

# Usage
The code demonstrates the functionality of the Solution class by instantiating an object solution and calculating the Fibonacci number for specific values of n. It showcases three different n values: 3, 6, and 4.

python

solution = Solution()

# Calculate the Fibonacci number for specific 'n' values
result1 = solution.fib(3)  
result2 = solution.fib(6)  
result3 = solution.fib(4)  

print("Fibonacci number for n = 3:", result1)
print("Fibonacci number for n = 6:", result2)
print("Fibonacci number for n = 4:", result3)
The results are printed for each calculated Fibonacci number corresponding to the provided n values.

# Example Output

Fibonacci number for n = 3: 2
Fibonacci number for n = 6: 8
Fibonacci number for n = 4: 3
The code demonstrates how to use the fib method to obtain the nth Fibonacci number for different input values of n.

