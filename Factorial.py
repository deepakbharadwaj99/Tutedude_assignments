# Def fun named factorial that takes a number as an argument and
# calculates its factorial using a loop or recursion.
n= int(input("Enter a number: "))
def factorial(n):
   if n==0:
       return 1
   else:
       return n*factorial(n-1)
print(factorial(n))