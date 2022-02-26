#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:45:12 2020

@author: CCloveHH
"""

import re
import pandas as pd

adj_with_de = 'pynlpir/adj_with_de.csv'
adj_no_de = 'pynlpir/adj_no_de.csv'

lines = []
# convert the file into a list
with open('pynlpir/tag/Learner_segment_tag_pynlpir.txt') as file_roommate:
    for line in file_roommate:
        line = line.strip('\n')
        line = re.sub("'",'',line)
        lines.append(line)
    file_roommate.close()
final = []
# convert each line into a list
for line in lines:
    line = line[1:-1]     
    line1 = line.split('),')
    new_list = []
    # get the info of word and pos by bracket
    for i in range(len(line1)):
        if i == len(line1) - 1:
            a = line1[i].replace(' ','')
        else:
            line1[i]+=')'
            a = line1[i].replace(' ','')           
        a = a[1:-1]
        a = a.split(',')
        a = tuple(a)
        new_list.append(a)
    final.append(new_list)
# get the combination of adj and noun
new_with_de = []
new_no_de = []
for line in final:
    for x in line:
        try:
            if x[1] == "adjective":
                y = line.index(x) + 1
                if line.index(x) < len(line)-2:
                    if line[y][0] == '的' and line[y+1][1] == 'noun':
                        with_de = x[0] + '的' + line[y+1][0]
                        new_with_de.append(with_de)
                if line.index(x) < len(line)-1:
                    if line[y][0] != '的' and line[y][1] == 'noun':
                        no_de = x[0] + line[y][0]
                        new_no_de.append(no_de)
        except:
            continue

with open('adj_with_de.csv', 'w') as file_adj_de:
    for line in new_with_de:
        file_adj_de.write(line)
        file_adj_de.write('\n')
        
with open('adj_no_de.csv', 'w') as file_adj_no_de:
    for line in new_no_de:
        file_adj_no_de.write(line)
        file_adj_no_de.write('\n')


        




