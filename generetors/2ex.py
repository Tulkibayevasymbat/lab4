#Write a program using generator to print the even numbers
#between 0 and n in comma separated form where n is input from console.


n = int(input("Enter the number n: "))
print(",".join(map(str, range(0, n + 1, 2))))

#input: 10
#output: 0,2,4,6,8,10