# Electricity Bill Calculator

RATE = 12.90

name = input("Enter customer name: ")

if name.strip == "":
    print("Please enter your name: ")
    name = input("Enter customer name: ")

previous = float(input("Enter previous meter reading: "))

if previous < 0:
    print("Invalid")
    previous = float(input("Enter previous meter reading: "))

current = float(input("Enter current meter reading: "))

if current < previous:
    print("Invalid")
    current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
