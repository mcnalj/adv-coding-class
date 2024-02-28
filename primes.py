numbers = range(1, 1001)
total = 0
for n in numbers:
    total = total + n
# print(total)

numbers = range(1, 1001)
total = 0
for n in numbers:
    if n % 2 == 0:
        total = total + n
# print(total)

numbers = range(1, 1001)
total = 0
for n in numbers:
    if n % 2 == 1:
        total = total + n
print(total)
# def isThisPrime(n):
isPrime = True
testNums = range(2, n)
for num in testNums:
    if n % num == 0:
        isPrime = False
    print(isPrime)

    return isPrime


numbers = range(2, 101)
primes = []
for n in numbers:
    if isThisPrime(n):
        primes.append(n)
print(primes)


numbers = range(1, 7)
total = 1
for n in numbers:
    total = total * n
print(total)


print(isThisPrime(7))


