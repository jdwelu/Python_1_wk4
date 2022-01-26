# Creating a program that makes 2 parallel lists one customer, the other
# the price of a product they purchased, and running some simply analytics
# after returning the original data that was input.

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$ Welcome to the Cash Calulator $$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print()

# Asks the user for the number of customers changes value to integer
num_customer = int(input("Please enter the number of customers: "))
## print("The number of customers is: ", num_customer)
print()
print("Now you will be prompted to enter the customer data. ")
print()

# Define arrays needed (debated over whether to append)
name_array = ["undefined"] * num_customer
cost_array = [0] * num_customer

# Establish a loop for entering customer information
count = 0
while count < num_customer:
    print()
    ## print("The customer number is:", count)
    customer = input("Enter the customer name: ")
    ## print("Name:", customer)
    name_array[count] = customer
    
    price = float(input("Enter the price of the product: $"))
    ## print("Product cost: $", format(price, ",.2f"), sep="") 
    cost_array[count] = price
    
    count = count + 1

# Testing my array values
## print()
## print(name_array)
## print(cost_array)
print()
print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$ The Calculated Summary! $$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print()

# Now to summarize the array data
summary = 0
while summary < num_customer:
    print()
    print("Name: ", name_array[summary])
    print("Price: $", format(cost_array[summary], ",.2f"), sep="")

    summary = summary + 1

# Now to factor in the total cash, average cash, min cash, and max cash
print()
print()
print("The maximum cash spent: $", format(max(cost_array), ",.2f"), sep="")
print("The minimum cash spent: $", format(min(cost_array), ",.2f"), sep="")
print("The total cash spent: $", format(sum(cost_array), ",.2f"), sep="")
print("The average cash spent: $", format((sum(cost_array)/num_customer), ",.2f"), sep="")


