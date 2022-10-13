import csv
import pandas

def csvToDataFrame(csvFile):
    with open(csvFile, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return pandas.DataFrame(data)