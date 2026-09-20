# Mini Project: Word Frequency Analysis Using MapReduce

## Objective
Learn the basic MapReduce workflow:
Input -> Map -> Shuffle/Sort -> Reduce -> Output

## Requirements
- Python 3.x
- Command Prompt / PowerShell / Terminal
- Hadoop is NOT required for Part 1. This project first simulates MapReduce locally.

## Files
- input/data.txt : sample dataset
- mapper.py : Mapper
- reducer.py : Reducer
- run_windows.bat : one-click Windows pipeline
- run_linux_mac.sh : pipeline for Linux/macOS
- top5.py : optional analysis for Top 5 words
- output/ : place for generated results

## Step 1 — Test the Mapper
Windows:
    python mapper.py < input/data.txt

Linux/macOS:
    python3 mapper.py < input/data.txt

Expected behavior:
Each word becomes:
    word    1

## Step 2 — Test Shuffle/Sort
Windows:
    python mapper.py < input/data.txt | sort

Linux/macOS:
    python3 mapper.py < input/data.txt | sort

The `sort` command is used here to simulate the grouping/sorting stage that conceptually happens before Reduce.

## Step 3 — Run the Full Pipeline
Windows:
    run_windows.bat

Linux/macOS:
    bash run_linux_mac.sh

Or manually:

Windows:
    python mapper.py < input/data.txt | sort | python reducer.py > output/result.txt

Linux/macOS:
    python3 mapper.py < input/data.txt | sort | python3 reducer.py > output/result.txt

## Step 4 — View the result
Open:
    output/result.txt

## Step 5 — Optional Top 5 Analysis
After generating output/result.txt:

    python top5.py

This displays the five most frequent words.

## Important Learning Point
The local project simulates the MapReduce logic. It does not yet run on a Hadoop cluster.

Conceptually:
    HDFS -> Map -> Shuffle/Sort -> Reduce -> HDFS

After this works, the same idea can be moved to Hadoop/HDFS.
