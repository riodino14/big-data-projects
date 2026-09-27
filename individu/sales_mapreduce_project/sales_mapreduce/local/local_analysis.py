import csv
from collections import defaultdict

sales_by_city = defaultdict(int)
sales_by_category = defaultdict(int)
count_by_city = defaultdict(int)

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]
        category = row["category"]
        amount = int(row["amount"])

        sales_by_city[city] += amount
        sales_by_category[category] += amount
        count_by_city[city] += 1

print("=== TOTAL SALES BY CITY ===")
for city in sorted(sales_by_city):
    print(f"{city}\t{sales_by_city[city]}")

print("\n=== TOTAL SALES BY CATEGORY ===")
for category in sorted(sales_by_category):
    print(f"{category}\t{sales_by_category[category]}")

print("\n=== TRANSACTION COUNT BY CITY ===")
for city in sorted(count_by_city):
    print(f"{city}\t{count_by_city[city]}")
