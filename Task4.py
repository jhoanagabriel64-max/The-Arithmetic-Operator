age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

base_price = 12

if age <= 12:
    discount = 3
elif age >= 65:
    discount = 4
elif is_student:
    discount = 2
else:
    discount = 0

final_price = base_price - discount

print(f"Your ticket price is ${final_price}.")