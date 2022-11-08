from utilities import Utilities as utils
from data import Dataset
import pandas as pd
from rdflib import Namespace
# rdflib knows about some namespaces, like FOAF
from rdflib.namespace import FOAF, XSD
dataDir = 'data/'
# define dataasets
europe_dataset = dataDir + 'EnergyConsumption/EC_Europe.csv'
dfEurope = utils.creteDataframe(europe_dataset)
naDataset = dataDir + 'EnergyConsumption/EC_NA.csv'
countryCodes = dataDir + 'country_codes.csv'
dfNa = utils.creteDataframe(naDataset)



if __name__=="__main__":
    # Declare Dataset object
    rdf = Dataset()
    # Load country codes
    countryCodes = dataDir + 'country-codes.csv'
    dfCountryCodes = rdf.addDataset(countryCodes, name='Countries')
    print(rdf.dataframes.get('Countries'))
    # Add namespace for country codes
    rdf.addNameSpace("country", Namespace("http://www.semanticweb.org/ontologies/2021/0/country#"))
    rdf.addNameSpace("foaf", FOAF)
    rdf.addNameSpace("xsd", XSD)
    # Bind new namespace to graph
    rdf.bindNamespaces()
    # Create nodes for country codes
    rdf.creteCountryNodes()
    # Print graph
    rdf.graph.print()