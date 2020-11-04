#!/usr/bin/env python3
input_data = open('outaa1.txt', 'rt')
output_data = open('write_aa1.txt', 'w')

status = 0  # initialized
seq_name = 'null'

seq_set1 = set()
seq_set2 = set()

for lines in input_data:
    if lines.startswith('aligned protein name'):
        status = 1  # sequences located
        seq_name = lines
        continue

    if lines.startswith('fitting score'):
        status = 2 # sequence section located
        fitting_score = lines
        continue

    if lines.startswith('aligned sequence'):
        status = 3
        fy = 'null1'
        r = 'null2'
        h = 'null3'
        continue

    if status == 3:
        aa_list = lines.split()
        if aa_list != []:
            if aa_list[0] == '20' and (aa_list[2] == 'F' or aa_list[2] == 'Y'):
                fy = seq_name
            if aa_list[0] == '22' and (aa_list[2] == 'R'):
                r = seq_name
            if aa_list[0] == '23' and (aa_list[2] == 'H'):
                h = seq_name
        if fy == r and fy == h:
            seq_set1.add(seq_name)
            
for names in seq_set1:
    output_data.write(names)

input_data.close()
output_data.close()
