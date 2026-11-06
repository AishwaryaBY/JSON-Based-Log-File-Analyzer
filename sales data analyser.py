
sales = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Headphones": 5000,
    "Keyboard": 3000,
    "Mouse": 1500
}

print("===== SALES DATA ANALYZER =====")

print("\nProduct-wise Sales:")
for product, amount in sales.items():
    print(product, ":", amount)

total_sales = sum(sales.values())
print("\nTotal Sales:", total_sales)

average_sales = total_sales / len(sales)
print("Average Sales:", average_sales)

highest = max(sales, key=sales.get)
print("\nHighest Selling Product:", highest)
print("Sales Amount:", sales[highest])

lowest = min(sales, key=sales.get)
print("\nLowest Selling Product:", lowest)
print("Sales Amount:", sales[lowest])

print("\nSales Ranking:")
sorted_sales = sorted(
    sales.items(),
    key=lambda x: x[1],
    reverse=True
)

for product, amount in sorted_sales:
    print(product, ":", amount)

search = input("\nEnter product name to search: ")

if search in sales:
    print("Product Found!")
    print("Sales Amount:", sales[search])
else:
    print("Product Not Found!")
