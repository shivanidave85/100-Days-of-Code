#Subscripting
print("Hello"[-1])

#Tip Calculator
print("Welcome to the Tip")
Bill = int(input("What was the total bill ? \n"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15 ?\n "))
Split = int(input("How How many people will split the bill? \n "))

Total_amount = Bill + ((Tip / 100) * Bill)
Split_amount = round(Total_amount/ Split , 2 )

print(f"Each person should pay : ${Split_amount}")
