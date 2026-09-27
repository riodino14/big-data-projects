# Sales Data Analysis Using MapReduce Simulation

## Project objective
This project demonstrates the MapReduce programming model using Python without requiring Hadoop, HDFS, WSL, or a virtual machine.

## Workflow
Input Data -> Mapper -> Shuffle & Sort -> Reducer -> Output

## Analyses
1. Total sales by city
2. Total sales by category
3. Transaction count by city

## Quick start
Requirements:
- Python 3.x

From the project root:

```powershell
python3.14 run_project.py
```

If `python3.14` is not recognized, use:

```powershell
python run_project.py
```

The results will be saved in the `output` folder.

## Run individual stages

Mapper:
```powershell
Get-Content data\sales.csv | python3.14 mapper\mapper_city.py
```

Shuffle:
```powershell
Get-Content data\sales.csv | python3.14 mapper\mapper_city.py | Sort-Object
```

Reducer:
```powershell
Get-Content output\city_shuffled.txt | python3.14 reducer\reducer_sum.py
```

## Local baseline
```powershell
python3.14 local\local_analysis.py
```

## Larger dataset
Generate 10,000 transactions:
```powershell
python3.14 generate_data.py
```

The generated file is:
`data/sales_10000.csv`

## Important limitation
This is a Python simulation of the MapReduce programming model. It does not execute on a real Hadoop cluster and therefore does not demonstrate HDFS, YARN, or distributed multi-node execution.

## Expected result for the 10-row dataset

### Total sales by city
- Busan: 81,000
- Incheon: 21,500
- Seoul: 144,000

### Total sales by category
- Electronics: 150,000
- Food: 84,000
- Transport: 12,500

### Transaction count by city
- Busan: 3
- Incheon: 2
- Seoul: 5
