import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)

for row in reader:
    if len(row) != 5:
        continue
    transaction_id, date, city, category, amount = row
    print(f"{city}\t1")
