import sys

current_key = None
current_total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    key, value = line.split("\t", 1)
    value = float(value)

    if key == current_key:
        current_total += value
    else:
        if current_key is not None:
            print(f"{current_key}\t{current_total:.0f}")
        current_key = key
        current_total = value

if current_key is not None:
    print(f"{current_key}\t{current_total:.0f}")
