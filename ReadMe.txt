#Extracting CRISPR Array Sequence data from a database web server
#Part 0: A brief description of the intention behind this project
The purpose behind this project is to develop a Hidden Markov Model to predict the presense of CRISPR arrays in bacterial genomes.
The HMM is being developed as a learning project for an undergraduate level directed study, and is not meant to perform better than existing CRISPR array detection tools.
To develop the model, I first need to create relevant data, which involves finding data of known CRISPR arrays and creating training sets of feature vectors and corresponding label vectors.

##Part 1: Downloading XML data from CRISPRdb (CRISPRArrayScraper.py)
####Dependancies:
* Python 3.x
* Selenium webdriver
* Google Chrome

CRISPRdb is an online database which hosts thousands of bacterial and Archael genomes which have been scanned for CRISPR arrays using academically published tools.
CRISPRdb hosts genomes without CRISPRs, with confirmed CRISPRs, and with "questionable structures". For the purpose of my project, I want to work only with bacterial DNA with confirmed CRISPRs. While CRISPRdb offers several utilities to download their data, I wanted to ensure that I was getting the data which met my critetia.
Using Selenium webdriver, I selected all of the table entries from the data base that had CRISPRs but did not have questionable structures. This allowed me to download the file CRISPRs.XML, which stores information about the CRISPR arrays as XML objects.

#Part 2: Extracting Accession numbers and Querying RefSec
###Dependancies:
* Python 3.x
* lxml

XMLAccessionExtractor.py is a script which uses the lxml package to parse the large xml file we obtained from part 1. The script extracts sequence objects from the XML file which contain 1 or more CRISPRs and creates a new XML file comprised of only those sequences. Taxa information is not important for the end of this project and was therefore excluded. The script then exctracts the RefSeq accession numbers of every genome sequence saved in the new XML file, writing them to a text file which is compatible for Batch Search from NCBI.
