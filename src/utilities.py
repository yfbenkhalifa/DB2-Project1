import csv
import pandas
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD
class Utilities:
    
    def __init__(self):
        pass
    
    @staticmethod
    def creteDataframe(file):
        format = file.split('.')[-1]
        if format == 'csv':
            return pandas.DataFrame(pandas.read_csv(file, header = 0))
        elif format == 'xlsx':
            return pandas.read_excel(file, engine="openpyxl")
        else:
            return None
            
    @staticmethod
    def bindNamespaces(graph, namespaces):
        for elem in namespaces:
            graph.bind(elem, namespaces[elem])
            
    @staticmethod
    def createNodes(graph, dataframe, column, nodeType, namespace, columnIndex = -1):
        for index, row in dataframe.iterrows():
            uri = URIRef(namespace[row[column]])
            graph.add((uri, RDF.type, nodeType))
    @staticmethod
    def addAttributes(graph, dataframe, column, namespace, columnIndex = -1):
        for index, row in dataframe.iterrows():
            uri = URIRef(namespace[row[column]])
            for col in dataframe.columns:
                if col != column:
                    graph.add((uri, URIRef(namespace[col]), Literal(row[col])))
            
    @staticmethod
    def loadDatasets(dataDir, datasets):
        dataframes = []
        for dataset in datasets:
            for datasrouce in datasets:
                csvFile = dataDir + datasrouce[0]
                df = Utilities.creteDataframe(csvFile)
                if df is None:
                    print('Error: File not found or not valid')
                else:
                    dataframes.__add__([df, datasrouce[1]])
        return dataframes