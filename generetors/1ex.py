#Create a generator that generates the squares of numbers up to some number N.

def squares_generator(N):
    return (i ** 2 for i in range(N))

N = int(input("Enter the number N: "))
squares_gen = squares_generator(N)

for square in squares_gen:
    print(square)

#output:
#Enter the number N: 6
#0
#1
#4
#9
#16
#25