TAX_INFO = [
    (20000, 0, 0.02),
    (30000, 200, 0.035),
    (40000, 550, 0.07),
    (80000, 3350, 0.115),
    (120000, 7950, 0.15),
    (160000, 13950, 0.18),
    (200000, 21150, 0.19),
    (240000, 28750, 0.195),
    (280000, 36550, 0.2),
    (320000, 44550, 0.22)
]

# Put your code below
######################
def calculate_tax(chargeable_income):
    total_tax = 0
    for item in TAX_INFO: 
        base_income = item[0]
        base_tax = item[1]
        additional_tax_rate = item[2]
        if chargeable_income > base_income: 
            total_tax = base_tax + (chargeable_income - base_income) * additional_tax_rate
    return total_tax


# Test Cases to test your code
##############################

tax = calculate_tax(15000)
print("Expected: 0.0")
print("Actual  : " + str(tax))
print()
    
tax = calculate_tax(35000)
print("Expected: 375.0")
print("Actual  : " + str(tax))
print()
    
tax = calculate_tax(100000)
print("Expected: 5650.0")
print("Actual  : " + str(tax))
print()

tax = calculate_tax(350000)
print("Expected: 51150.0")
print("Actual  : " + str(tax))
print()

