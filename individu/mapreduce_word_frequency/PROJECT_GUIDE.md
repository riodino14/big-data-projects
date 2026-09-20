# Project Guide — What You Should Understand

## 1. Mapper
Input:
    A line of text

Output:
    (word, 1)

Example:
    Hadoop is fast

becomes:
    hadoop    1
    is        1
    fast      1

## 2. Shuffle/Sort
The Mapper outputs are grouped by key.

Example:
    hadoop    1
    data      1
    hadoop    1

becomes conceptually:
    data      -> [1]
    hadoop    -> [1, 1]

## 3. Reducer
The Reducer sums the values for each key.

Example:
    hadoop -> [1, 1]

becomes:
    hadoop -> 2

## 4. Why this matters
This small project demonstrates the core logic behind WordCount-style MapReduce.

The local shell pipeline is:
    mapper.py | sort | reducer.py

The Hadoop concept is:
    HDFS -> Mapper -> Shuffle/Sort -> Reducer -> HDFS

## 5. Questions to answer after running
1. What does the Mapper output?
2. Why does every word initially receive the value 1?
3. What does Shuffle/Sort accomplish?
4. Why can the Reducer sum the values?
5. Which file contains the final result?
6. What would happen if the input file became much larger?
7. Which Hadoop component would be responsible for storing the large input data?
8. Which Hadoop component would manage resources in a YARN-based system?

## 6. Suggested next step
Once the local version is understood, move the same project to Hadoop/HDFS. Do not skip the local version: it makes the Hadoop execution much easier to understand.
