print("Welcome to tip calculator!")
totalBill = float(input("What was the total Bill?\n:$ "))
tip = float(input("How much tip would you like to give?\n$: "))
totalPerson = float(input("How many people to split the bill?\n: "))

billEveryPerson = round((totalBill + tip) / totalPerson , 2)

print(f"Each person should pay: $ {billEveryPerson}")

# type convert are int() float() str() bool()

