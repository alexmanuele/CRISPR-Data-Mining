from lxml import etree
from copy import deepcopy

tree = etree.parse('CRISPRs.xml')
root = tree.getroot()
outTree = etree.Element("ValidSequences")

#puts all sequences with a CRISPR to a new element tree
for seq in root.iterdescendants("Sequence"):
    crisprCount = int(seq.findtext("CRISPRs/CRISPRCount"))
    if crisprCount > 0:
        outTree.append(deepcopy(seq))

#write the valid sequences to an xml file
outTree = etree.ElementTree(outTree)
outTree.write("ExtractedSequences.xml", pretty_print=True)

#Extract the accession numbers
accessionNumbers = []
outRoot = outTree.getroot()
for acc in outRoot.iterdescendants("Sequence"):
    accessionNumbers.append(acc.findtext('RefSeq'))

#Write the accession numbers to  a textfile
with open('AccessionNumbers.txt', 'w') as file:
    for i in accessionNumbers:
        file.write(i + "\n")
