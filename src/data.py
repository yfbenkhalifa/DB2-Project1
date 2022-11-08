import rdflib
import os
from utilities import Utilities as utils
from rdflib import Graph, Literal, RDF, URIRef, Namespace

class Dataset:
    dataframes = {}
    graph = rdflib.Graph()
    namespaces = {}
    
    def __init__(self):
        self.initGraph()
    
    def initGraph(self):
        self.graph = rdflib.Graph()
        utils.bindNamespaces(self.graph, self.namespaces)
    
    def initGraph(self, namespaces=None, dataFrames=None):
        if namespaces is not None:
            self.namespaces = namespaces
        if dataFrames is not None:
            self.dataframes = dataFrames
        self.graph = rdflib.Graph()
        utils.bindNamespaces(self.graph, self.namespaces)
        
    def addNameSpace(self, prefix, namespace):
        self.namespaces[prefix] = namespace
        
    def bindNamespaces(self):
        for elem in self.namespaces:
            self.graph.bind(elem, self.namespaces[elem])
        
    def addDataset(self, filePath, name=''):
        df = utils.creteDataframe(filePath)
        if df is None:
            print('Error: File not found or not valid')
        else:
            if self.dataframes.get(name) is None:
                self.dataframes[name] = df
            else: 
                self.dataframes[name].append(df)
            print('Added ' + filePath + ' to dataset') 
            
    def addDatasets(self, files):
        for file in files:
            self.addDataset(file)
            
    def creteCountryNodes(self):
        for index, entry in self.dataframes.get('Countries').iterrows():
            uri = rdflib.URIRef(self.namespaces['country'][entry['FIFA']])
            # Create Node
            self.graph.add((uri, RDF.type, self.namespaces.get('country').Country))
            # Adding name attribute
            self.graph.add((uri, self.namespaces.get('country').name, rdflib.Literal(entry['official_name_en'])))
            
    