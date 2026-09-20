from pathlib import Path

result_file = Path("output/result.txt")

if not result_file.exists():
    print("output/result.txt was not found.")
    print("Run the MapReduce pipeline first.")
    raise SystemExit(1)

results = []

with result_file.open("r", encoding="utf-8") as file:
    for line in file:
        word, count = line.strip().split("\t")
        results.append((word, int(count)))

results.sort(key=lambda item: (-item[1], item[0]))

print("Top 5 Most Frequent Words")
print("--------------------------")

for rank, (word, count) in enumerate(results[:5], start=1):
    print(f"{rank}. {word} -> {count}")
