class Solution(object):
    def fib(self, n):
     if n == 0:
        return 0
     elif n == 1:
        return 1
     else:
        a, b = 0, 1
        counter = 2
        while counter <= n:
            a, b = b, a + b
            counter += 1
        return b

solution=Solution()
# Calculate the Fibonacci number for specific 'n' values
result1 = solution.fib(3)  
result2 = solution.fib(6)  
result3 = solution.fib(4)  

print("Fibonacci number for n = 3:", result1)
print("Fibonacci number for n = 6:", result2)
print("Fibonacci number for n = 4:", result3)