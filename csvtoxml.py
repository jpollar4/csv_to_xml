# CSV module
import csv
from lxml import etree

# Topmost XML element
top = etree.Element('top')
# Open a file
with open('data.csv') as csvfile:
	# And use a dictionary-reader
	for d in csv.DictReader(csvfile):
		# For each mapping in the dictionary
		child = etree.SubElement(top, "UNIT")
		for (k, v) in d.items():
			# Create an XML node
			child2 = etree.SubElement(child, k)
			child2.text = v
print(etree.tostring(top, pretty_print=True))

file = open('testfile.xml','wb')
file.write(etree.tostring(top, pretty_print=True));

file.close()
