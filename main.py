#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

filename = 'BIOGRID-GENE-34444-3.1.84.tab2.txt';

protein1 = 7
protein2 = 8
interaction = 11

for line in open(filename).readlines():
	if line[0] != "#":
		fields = line.split('\t')
		if fields[interaction].find('Genetic') < 0:
			print fields[interaction]+"\t\t"+fields[protein1]+"\t"+fields[protein2]
