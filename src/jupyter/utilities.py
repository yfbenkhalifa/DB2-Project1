import csv
import pandas

def creteDataframe(csvFile):
    with open(csvFile, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return pandas.DataFrame(data)

def bindNamespaces(graph, prefixes, namespaces):
    for prefix, namespace in namespaces.items():
        graph.bind(prefix, namespace)

def createNodes(graph, dataframe, column, nodeType, namespace):
    for index, row in dataframe.iterrows():
        graph.add()