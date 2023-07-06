#! /opt/anaconda3/bin/python

import os
import pandas as pd
from random import randrange
import subprocess
import sys

# For each DEG observed for ASCs, randomly generate region within 500kb upstream of TSS and 100kb downstream of gene body

# EDIT FOR THIS VERSION: ensure the random regions do NOT overlap DARs

### 1.0 For each DEG: ###
# 	if # DARs > 0, get number of DARs. Randomly generate that number of 500 bp bins within defined gene region.
#	if # DARs = 0, randomly generate 13 500 bp bins within defined gene region.

# Count No. DARs per DEG:
master_list_file = "/Users/maggiebrown/Dropbox (GaTech)/For_Erin/DARs_vs_DEGs/ASCs/Master_Overlap_DARs.txt"
master_list_handler = open(master_list_file)
master_list = master_list_handler.readlines()[1:]

dars_count = {} # {gene : count}
chr_dict = {} # {chr : [region]}
for line in master_list:
	gene = line.split()[0]
	chromo = line.split()[2][:2]
	region = line.split()[2][3:]
	print(chromo, region)
	if gene not in dars_count.keys():
		dars_count[gene] = 1
	elif gene in dars_count.keys():
		new_count = dars_count[gene] + 1
		dars_count[gene] = new_count
"""
# Get random region for each DEG
gene_list_file = "/Users/maggiebrown/Dropbox (GaTech)/For_Erin/DARs_vs_DEGs/ASCs/ASCs_vs_Non-ASCs_DEGs_Anno.bed"
gene_list_handler = open(gene_list_file)
gene_list = gene_list_handler.readlines()[1:]

# generate output file

outputname = "Random_Regions.txt"
f = open(outputname,"w+")
header = str("DEG" + "\t" + "Region" + "\n")
f.write(header)

genes_regions_dict = {} # {gene : [region1, region2, ...]} 
for line in gene_list:
	gene = line.split()[12]
	if gene not in genes_regions_dict.keys():
		chromo = line.split()[2]
		strand = line.split()[3]

		# determine number of regions
		if gene in dars_count.keys():
			count = dars_count[gene]
		else:
			count = 13 # avg number DARs per gene

		# account for translational direction
		region_list = []
		i = 0
		while i < count:
			start = int(line.split()[4])
			end = int(line.split()[5])

			if start > end: # opp strand
				DEGs_start = int(line.split()[4])+500000
				DEGs_end = int(line.split()[5])-100000
				print("-", gene, count, DEGs_start, DEGs_end)
				# randomly choose 500 bp region within DEG region:
				rand_start = randrange(DEGs_end, (DEGs_start-500))
				rand_end = rand_start + 500
			elif start < end: # pos strand
				DEGs_start = int(line.split()[4])-500000
				DEGs_end = int(line.split()[5])+100000
				print("+", gene, count, DEGs_start, DEGs_end)
				# randomly choose 500 bp region within DEG region:
				rand_start = randrange(DEGs_start, (DEGs_end-500))
				rand_end = rand_start + 500

			"""
			"""
			if strand == "-":
				DEGs_start = int(line.split()[4])+500000
				DEGs_end = int(line.split()[5])-100000
				print("-", gene, count, DEGs_start, DEGs_end)
				# randomly choose 500 bp region within DEG region:
				rand_start = randrange(DEGs_end, (DEGs_start-500))
				rand_end = rand_start + 500

			elif strand == "+":
				DEGs_start = int(line.split()[4])-500000
				DEGs_end = int(line.split()[5])+100000
				print("+", gene, count, DEGs_start, DEGs_end)
				# randomly choose 500 bp region within DEG region:
				rand_start = randrange(DEGs_start, (DEGs_end-500))
				rand_end = rand_start + 500
			"""
			"""

			new_region = str(chromo + ":" + str(rand_start) + "-" + str(rand_end))

			newline = str(gene + "\t" + new_region + "\n")
			f.write(newline)
			region_list.append(new_region)
			i += 1
	else:
		pass

	genes_regions_dict[gene] = region_list
"""

