#!/bin/bash

mkdir -p output

echo "=========================================="
echo "MapReduce Word Frequency - Linux/macOS"
echo "=========================================="

echo "[1/3] Running Mapper..."
python3 mapper.py < input/data.txt > output/map_output.txt || exit 1

echo "[2/3] Running Shuffle/Sort..."
sort output/map_output.txt > output/sorted_output.txt || exit 1

echo "[3/3] Running Reducer..."
python3 reducer.py < output/sorted_output.txt > output/result.txt || exit 1

echo
echo "DONE!"
echo "Result saved to output/result.txt"
echo
cat output/result.txt
