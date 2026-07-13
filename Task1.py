# Problem 1: Weird or Not Weird
# Problem Statement

# Write a Python program that takes one integer as input.

# Based on the value of the number, print either "Weird" or "Not Weird" by following these rules:

# If the number is odd, print "Weird".
# If the number is even and is between 2 and 5 (inclusive), print "Not Weird".
# If the number is even and is between 6 and 20 (inclusive), print "Weird".
# If the number is even and is greater than 20, print "Not Weird".



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
if n%2==0 and 2<= n <=5:
    print("Not Weird")    
elif n%2==0 and 6<= n <=20:
    print("Weird")    
elif n%2==0 and n > 20:
    print("Not Weird")    
   