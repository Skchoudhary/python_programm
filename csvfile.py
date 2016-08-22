#! /usr/bin/env python3
with open('us-500.csv') as f:
    row=[]
    for line in f:
        row.append(line.replace('\n','').replace('"','').split(','))

    row.sort(key=lambda x: x[0],reverse=True)
    for fld in row:
        for val in fld:
            print('{:15}'.format(val),end=' ' )
        print('\n')
        print('='*10)
