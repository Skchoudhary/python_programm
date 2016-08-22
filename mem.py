#! /usr/bin/env python3

with open ('/proc/meminfo') as f:
    for l in range (0,3):
        mem=f.readline()
        size=mem.split(' ')[-2]
        size=int(size)//1024
        print('{:14}{:10} '.format(mem.split(' ')[0],size),' MB')


        
