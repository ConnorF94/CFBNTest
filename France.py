#First change/addition to .py file
Print "Welcome to Connor's GitHub Python File."
# Input taxable income
print ("What is your taxable income?")
incomeString = input()
income = int (incomeString)
# Test againt local tax rate
if income <= 20000:
    tax = 0.02 * income
else:
    if income <= 50000:
        tax = 400 + 0.035 * (income - 20000)
    else:
        tax = 1150 + 0.045 * (income - 50000)
print ("Your income tax is: $%.2f" %tax)

