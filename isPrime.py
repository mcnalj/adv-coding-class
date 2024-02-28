n = input("Enter a number: ")
isPrime = True
testNums = range(2, n)
for num in testNums:
    if n % num == 0:
        isPrime = False
print(isPrime)

