from lxml import etree
from copy import deepcopy
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

tree = etree.parse('CRISPRs.xml')
root = tree.getroot()
outTree = etree.Element("CRISPRsSequences")

genomeNumbers = []
genomeCRISPRReferences = []
#Get the accession numbers of the genomes we're interested in
with open('AccessionNumbersManySequences.txt', 'r') as file:
    for line in file:
        genomeNumbers.append(line[:-1])

#find the sequence info of the genomes we are interested in
for ref in genomeNumbers:
    for seq in root.iterdescendants("Sequence"):
        reference = seq.findtext("RefSeq")
        if reference == ref:
            outTree.append(deepcopy(seq))


#Make a list that has the genome Acc. and the boundaries of the CRISPR
outTree = etree.ElementTree(outTree)
outRoot = outTree.getroot()
for seq in outRoot.iterdescendants("Sequence"):
    reference = seq.findtext('RefSeq')
    for crisp in seq.iterdescendants('CRISPR'):
        id = [reference, [crisp.findtext('BeginningPosition'), crisp.findtext('EndingPosition')]]
        genomeCRISPRReferences.append(id)

#open the FASTA file and get sequences that border the crisprs by 20kb margin
record_iterator = SeqIO.parse("Genomes.fasta", "fasta")
annotated = []
for record in record_iterator:
    id = record.id
    seq = record.seq
    for entry in genomeCRISPRReferences:
        if entry[0] == id[:-2]:
            start = int(max(int(entry[1][0]) - 20000, 0))
            end = int(int(entry[1][1]) + 20000)
            seq = seq[start:end]
            record = SeqRecord(seq, id=id)
            annotated.append(record)
#Use BioPython to create a fasta file with the new sequences
SeqIO.write(annotated, "WideMarginCRISPRs.faa", "fasta")