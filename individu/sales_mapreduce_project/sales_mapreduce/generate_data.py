import csv
import random
from datetime import date, timedelta

random.seed(42)

cities = ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon"]
categories = ["Food", "Transport", "Electronics", "Clothing", "Entertainment"]
start_date = date(2026, 9, 1)

with open("data/sales_10000.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "date", "city", "category", "amount"])

    for i in range(1, 10001):
        transaction_date = start_date + timedelta(days=random.randint(0, 29))
        city = random.choice(cities)
        category = random.choice(categories)
        amount = random.randint(5000, 200000)

        writer.writerow([
            f"T{i:05d}",
            transaction_date,
            city,
            category,
            amount
        ])
