# def power(num1, num2):
#     """This raised num1 to the pwer of num2. """
#     answer = num1 ** num2
#     print(answer)

# number1 = int(input("Enter the base: "))
# number2 =int(input("Enter the exponent: "))
# print(power(number1, number2))

def getFormattedName(first, last, middle=''):
    if middle:
        fullName = f"{first} {middle} {last}"
    else:
        fullName = f"{first} {last}"
    print(fullName.title())

getFormattedName("joe", "biden")



TAX = 0.055

def printTotalAmount(billAmount=100, tipPercentage=20):
    tipDecimal = tipPercentage/100
    tipAmount = billAmount * tipDecimal
    taxAmount = billAmount * TAX
    total = billAmount + tipAmount + taxAmount
    print(total)

printTotalAmount()

printTotalAmount(50)
printTotalAmount(tipPercentage=30)



# TAX = 0.055
# billAmount = float(input("Enter your total purchase amount: "))
# tipPercentage = float(input("Enter your tip amount (as a percentage): "))
# printTotalAmount(billAmount, tipPercentage)







# 
















# tipDecimal = tipPercentage/100
# tipAmount = billAmount * tipDecimal
# taxAmount = billAmount * TAX
# total = billAmount + tipAmount + taxAmount
# print(total)



