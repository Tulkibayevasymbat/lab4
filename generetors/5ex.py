#Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

starting_number = int(input("number: "))

for number in countdown(starting_number):
    print(number)