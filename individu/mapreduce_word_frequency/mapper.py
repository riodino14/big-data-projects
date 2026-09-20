import sys

for line in sys.stdin:
    words = line.strip().lower().split()

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word:
            print(f"{word}\t1")