# Write a Python program that reads an integer n from the user.

# Print the square of every number from 0 to n-1, with each square on a new line.

# Example

# Input

# 5

# Output

# 0
# 1
# 4
# 9
# 16

# Solution
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)

