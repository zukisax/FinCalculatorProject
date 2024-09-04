import math
########################################################################################
#The program allows the user to calculate their interest on an investment
# or calculate the amount that should be repaid on a bond (home loan) each month.
########################################################################################

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a loan \n ")

# Create and store the financial product chosen into variable "fin_product"
# and apply casting on the input as a string in lowercase
fin_product = str(input("Enter either 'investment' or 'bond' from the menu above: \n "))
fin_product = fin_product.lower()

# Calculate the total investment with return and monthly bond repayment
# The following if-elif-else stucture executes all the calculations
if fin_product == "investment":
    # Create variables and store inputs for the investment calculations
    deposit = float(input("Enter the amount of money for deposit: "))
    interest_rate = float(input("Enter only the number of the interest rate: "))
    # Convert to percentage the interest rate
    ir = interest_rate/100
    duration = float(input("Enter the number of years the funds are being invested: "))

    # Create variable and store input for either simple or compound interest as a string in lowecase 
    interest = str(input("Enter either 'simple' or 'compound' for interest to be earned on investment: "))
    interest = interest.lower()

    # Calculate the total invesment with either simple or compund interest
    # The nested if-elif-else stucture executes the investment calculations
    if interest == "simple":
        simple_interest = deposit*(1 + ir*duration)
        print(f"The total investment amount with {interest} interest is R{round(simple_interest,2)}")

    elif interest == "compound":
        compound_interest = deposit*math.pow((1 + ir),duration)
        print(f"The total investment amount with {interest} interest is R{round(compound_interest,2)}")

    else:
        print(f"The {interest} input is invalid. Please check your spelling!")

# Calculate the monthly bond repayment
elif fin_product == "bond":
    # Create variables and store inputs for the bond repayment calculation
    p_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter only the number of the monthly interest rate: "))
    # Convert to percentage and calibrate the interest rate for monthly payments
    ir = (interest_rate/100)/12
    num_months = int(input("Enter number of months for bond repayment: "))

    bond_repayment = (ir*p_value)/(1 -(1 + ir)**(-1*num_months))
    print(f"The monthly {fin_product} repayment is R{round(bond_repayment,2)} ")

# Output for an invalid input
else:
    print(f"Error: {fin_product} is an invalid input. Please check your spelling!")

########################################################################################
# Ouput for example with 20 years and 8% interest
# Enter the amount of money for deposit: 1000.00
# Enter only the number of the interest rate: 8.00
# Enter the number of years the funds are being invested: 20
# The total investment amount with simple interest is R2600.00
# The total investment amount with compound interest is R4660.96
########################################################################################

