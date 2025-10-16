weight = float(input("Enter weight (lbs): "))
destination = input("Enter destination (domestic/international): ")
membership = input("Enter membership (standard/premium): ")

base_cost = 10

if weight > 20:
    base_cost += 5

if destination == "international" and membership != "premium":
    base_cost *= 2

if membership == "premium":
    final_cost = base_cost * 0.8
else:
    final_cost = base_cost

print(f"Final Shipping Cost: ${final_cost:.2f}")
if weight > 20:
    print(f"Details: Base $10 + Overweight $5")
if destination == "international" and membership != "premium":
    print(f"International fee applied")
if membership == "premium":
    print(f"Premium 20% discount applied")