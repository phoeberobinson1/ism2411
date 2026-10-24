"""
Self-Assessment Questions
1. The first bug I spotted was the missing colon at the end of the for loop 
header syntax. I identified it directly from Python's traceback and syntax error 
highlight when trying to run the script. This shows that my debugging instincts 
are strong when catching immediate surface-level coding errors flagged.
2. The "apply_discount" function calculuates the discounted price based on the tier. 
It accepts a numerical price and a tier string. It evaluates the tier and applies 
the corresponding discount percentage to the price. A collague could use this without
reading the body of the function by understanding the function name and parameters. 
3. AI (Gemini) was used to help clarify debugging steps and reinforced scope rules. 
"""
#Exercise 1

def calculate_tax(price,rate):
   return price * rate

tax_1 = calculate_tax(100,0.07)
tax_2 = calculate_tax(250,0.08)

print(f"Tax on $100 at 7%: ${tax_1:.2f}")
print(f"Tax on $250 at 8%: ${tax_2:.2f}")
print(f"Tax on $350 at 5%: ${calculate_tax(350,0.05):.2f}")

#Exercise 2

def apply_discount(price,tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.1
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    return price * (1 - discount)

original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price}, | Tier: {tier}, | Total: ${total:.2f}")

#Exercise 5

sales = [120, 80, 250, 175, 90]

# Changed 'total = sale' to 'total += sale' so values accumulate instead of overwriting
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Added missing colon ':' at the end of the for loop header syntax
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Changed 'i <= len(sales)' to 'i < len(sales)' to avoid IndexError
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#Exercise 6

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # Output: 100
print(double_it()) # Output: 1998
print(x)           # Output: 100

# Variable defined outside functions live in the global scope. 
# Local variables can have the same name as global variables, 
# but they are different variables. When 'x = 999' is assigned 
# inside 'double_it()', Python creates a separate local variable 
# named 'x' within the function's scope. Modifying or assigning a 
# variable locally does not alter the global variable 'x' outside 
# the function.