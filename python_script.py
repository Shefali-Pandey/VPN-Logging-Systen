#################### import libraries #######################################################

import pandas as pd
import numpy as np
import gzip
import glob

#################### Extract ################################################################

filenames = (glob.glob('LOG-2018-05-28-*.TXT.gz'))  ## link all files ##

for i in filenames:												 ## unzip all files to one ##
  inF = gzip.GzipFile(i, 'rb')			
  s = inF.read()
  inF.close()
  outF = file("LOG.TXT", 'wb')
  outF.write(s)
  outF.close()
  #print(s)

#################### Functions ##############################################################

def between(value, a, b):
    pos_a = value.find(a)								  ## Find and validate before-part ##
    if pos_a == -1: return ""
    pos_b = value.find(b, pos_a + 1)					   ## Find and validate after part ##
    if pos_b == -1: return ""
    adjusted_pos_a = pos_a + len(a)									 ## Return middle part ##
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

def Remove(duplicate):								  ## Function to remove duplicate data ##
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#############################################################################################

## extract data names ##
lines = []
names = []
with open('LOG.TXT') as in_file:
    for line in in_file:        ## Store each line in a string variable "line" ##
       lines.append(line) 
    for i in lines:
    	names.append(between(i, "\\", "/"))
    	#print(between(i, "\\", "/"))
names = filter(None, names)
names = Remove(names)
print(names)

#################### Eport CSV ##############################################################

with open('output.csv', 'w') as out_file:					 ## write names to output.csv ##
	for name in names:
		out_file.write(name + '\n')

#############################################################################################