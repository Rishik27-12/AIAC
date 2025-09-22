# Find squares of numbers
import time

start = time.time()
nums = [i for i in range(1,1000000)]
squares = []
for n in nums:
    squares.append(n**2)
print(len(squares))
end = time.time()
print("Execution time:", end - start)
# Refactored code using list comprehension
start = time.time()
nums = [i for i in range(1,1000000)]
squares = [n**2 for n in nums]
print(len(squares))
end = time.time()
print("Execution time:", end - start)
