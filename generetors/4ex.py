#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
#Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    return (i ** 2 for i in range(a, b + 1))

a = int(input("begin (a): "))
b = int(input("end (b): "))

for square in squares(a, b):
    print(square)