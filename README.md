# cis129_lab03_coffeeShop.py
Mod 3 Lab

# Elias Wilber
# CIS129
# 09/24/2023
# Mod 3 Lab

coffee = 6.00 # Turning coffee and muffin into variables.
muffin = 4.00

amtCoffee = int(input("How many coffees would you like to order?: ")) # Asking the user for input on. (How much of each did they buy?)
amtMuffin = int(input("How many muffins would you like to order?: "))

print() #These are blank spaces to read the code easier when its executed.
print("************************") # Stars to fill up space.
print()
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(amtCoffee)
print("Number of muffins bought?")
print(amtMuffin)
print()
print("************************")
print()
print("************************")
print()
print("My Coffee and Muffin Shop Receipt")



print(amtCoffee, " coffee at $5 each: $ ", (amtCoffee * 5.00)) # Taking the amount of coffees  bought and multiplying that by $5.00.

print(amtMuffin, " muffin at $4 each: $ ", (amtMuffin * 4.00)) # Similar situation on the bottom but it's $4.00.

total = amtCoffee + amtMuffin # Total before tax, adding both the prices of each and giving it to the variable total.

totalTaxed = total * (6/100) # totalTaxed is the 6% tax on the price of the total.
print("6% tax at: $", (totalTaxed))
print()
print("-------")
print()

actTotal = total + totalTaxed
print("Total: $", actTotal) # In these last two lines, I added total and the tax of total to make a new variblae named actTotal. I then printed that for the full price.
