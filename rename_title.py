#!/usr/bin/env python

data = open('human.txt', 'rt')
data2 = open('output3.txt', 'w')
count = 1
for line in data:
    if line.startswith('>'):
        title = '>sequence_' + str(count) + '\n'
        data2.write(title)
        count += 1
    else:
        data2.write(line)

data.close()
data2.close()
