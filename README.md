# DB2-Project1

This is a public repository containing the Source code and data used for the development 
of the assigned Database 2 Course Team Project

# Possible Subjects Domains:

Energy/Fuel Consumption

The idea is to analyse the usage of fuel and electric of autovehicles in the world, relating it to the energy production costs and determining which is the most CO2 efficient and cost efficient

Datasets:
	- Fuel Economy Data: How Efficient Are Today's Cars? | Kaggle
	- Electricity Production by Source (World) | Kaggle
	- World Energy Consumption | Kaggle
    - https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html
	- Countries URL Repo : https://eulersharp.sourceforge.net/2003/03swap/countries

# Model explanation:
The objective is to make a model that can describe the energy used and produced by each country, sub-dividing then by class of property/ 

# Implementation
The main implementation of the dataset involves around the custom class Dataset, in which we find all the attributes and method that allow us to create the RDF. 
We will start by creating the Country Nodes, using the public Namespace:
http://eulersharp.sourceforge.net/2003/03swap/countries#
For each country we will specify the attributes defined in the RDF Schema model