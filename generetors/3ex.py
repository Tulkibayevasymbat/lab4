#Define a function with a generator which can iterate the numbers,
#which are divisible by 3 and 4, between a given range 0 and n.

def qwerty(n):
    return (num for num in range(n + 1) if num % 3 == 0 and num % 4 == 0)

n = int(input("Enter the number n: "))
print(list(qwerty(n)))

#output:
#Enter the number n: 12
#[0, 12]