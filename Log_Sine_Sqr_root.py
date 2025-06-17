## calculation of square root of a number
a= int(input("Enter a number: "))
import math as m

sqrt_val=m.sqrt(a) ## squaring here

if a>0:
    log_value=m.log(a)
else:
    log_value="Unidentified (Logarithm of non- positive numbers)"
sine_value= m.sin(a) ## Sine

print("Square root: ",sqrt_val)
print("Logarithm: ",log_value)
print("Sine: ",sine_value)



