"""
Reflection
1. Lists in Python are dynamically sized and can store mixed data types natively, which is much more 
flexible than fixed arrays in other languages. Being able to modify them in place using methods like 
append() and sort() makes data manipulation very intuitive.
2. When tracking daily teller transaction volumes and cash drawers during my time at Achieva credit union,
 compiling manual totals across multiple sheets was tedious. Using a Python list with sum() and len() 
 could have instantly automated the daily calculations and error checking.
"""
#Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2

middle_index = len(inventory) // 2
print(inventory[0])
print(inventory[-1])
print(inventory[middle_index])

#Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Exercise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#Exercise 5

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught,", e)
    print("Tuples are immutable, which is useful for protecting fixed coordinates from accidental modification.")
    print(coords)

#Exercise 6

sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {max(sales)} | Worst: {min(sales)}")

#Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)

#Exercise 8

sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_avg = sum(high_sales) / high_count

print(f"{high_sales} | Count: {high_count} | Avg: ~{high_avg:.2f}")