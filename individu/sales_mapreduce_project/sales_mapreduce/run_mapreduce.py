import csv
from collections import defaultdict

def map_city(input_file):
    mapped = []
    with open(input_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            mapped.append((row["city"], row["amount"]))
    return mapped

def shuffle(mapped_data):
    return sorted(mapped_data, key=lambda x: x[0])

def reduce_sum(sorted_data):
    result = defaultdict(float)
    for key, value in sorted_data:
        result[key] += float(value)
    return result

input_file = "data/sales_10000.csv"

mapped = map_city(input_file)

print("=== MAP OUTPUT (first 10) ===")
for item in mapped[:10]:
    print(item)

shuffled = shuffle(mapped)

print("\n=== SHUFFLE OUTPUT (first 10) ===")
for item in shuffled[:10]:
    print(item)

result = reduce_sum(shuffled)

print("\n=== REDUCE OUTPUT ===")
for key in sorted(result):
    print(f"{key}\t{result[key]:.0f}")
