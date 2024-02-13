# coding: utf-8
#this will be my receipt for the coffee and muffin shop.
print("************************************") #asterisks
num_coffees = int(input("Number of coffees bought?")) #asking how many coffees bought.
num_muffins = int(input("Number of muffins bought?")) #asking how many muffins bought.
num_teas = int(input("Number of teas bought?")) #asking how many teas bought.
print("************************************")
print() #blank space
print("************************************")
print("My Coffee and Muffin Receipt")
cost_of_coffees = num_coffees * 5.00 
print(num_coffees, "Coffee at $5 each: $ %.2f" %(cost_of_coffees))
cost_of_muffins = num_muffins * 4.00
print(num_muffins, "Muffins at $4 each: $ %.2f" %(cost_of_muffins))
cost_of_teas = num_teas * 3.00
print(num_teas, "Teas at $3 each: $ %.2f" %(cost_of_teas))
total_cost = cost_of_coffees + cost_of_muffins + cost_of_teas
tax = total_cost * 0.06
total_cost = total_cost + tax
print("6% tax: $", (tax))
print("-----")
print("total: $ %.2f" %(total_cost + tax))
print("************************************")
print()
print("Thank you for stopping by! Have a great day.")
#I am having trouble with the tax part, not sure if the tax is correct.


