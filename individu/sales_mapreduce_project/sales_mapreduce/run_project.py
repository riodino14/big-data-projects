import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "sales.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

def run_pipeline(mapper, output_name):
    p1 = subprocess.run(
        [sys.executable, str(ROOT / "mapper" / mapper)],
        stdin=open(DATA, "r", encoding="utf-8"),
        capture_output=True,
        text=True
    )
    if p1.returncode != 0:
        print(p1.stderr)
        raise SystemExit(p1.returncode)

    mapped = p1.stdout.splitlines()
    (OUT / f"{output_name}_mapped.txt").write_text(
        "\n".join(mapped) + "\n", encoding="utf-8"
    )

    shuffled = sorted(mapped)
    (OUT / f"{output_name}_shuffled.txt").write_text(
        "\n".join(shuffled) + "\n", encoding="utf-8"
    )

    p2 = subprocess.run(
        [sys.executable, str(ROOT / "reducer" / "reducer_sum.py")],
        input="\n".join(shuffled) + "\n",
        capture_output=True,
        text=True
    )
    if p2.returncode != 0:
        print(p2.stderr)
        raise SystemExit(p2.returncode)

    (OUT / f"{output_name}_result.txt").write_text(
        p2.stdout, encoding="utf-8"
    )
    return p2.stdout

print("=== SALES MAPREDUCE PROJECT ===\n")

print("[1] Total sales by city")
print(run_pipeline("mapper_city.py", "city"))

print("[2] Total sales by category")
print(run_pipeline("mapper_category.py", "category"))

print("[3] Transaction count by city")
print(run_pipeline("mapper_count.py", "count"))

print("Results have been saved in the output/ folder.")
print("\nExpected results for the 10-row dataset:")
print("City: Busan 81000, Incheon 21500, Seoul 144000")
print("Category: Electronics 150000, Food 84000, Transport 12500")
print("Count: Busan 3, Incheon 2, Seoul 5")
