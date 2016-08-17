#! /usr/bin/env python3

with open("/proc/meminfo") as fobj:
    for i in range(0,3):
        lines=fobj.readline()
        size=int(lines.split(' ')[-2])
        #print(size)
        size//=1024
        print(lines.split(' ')[0],' ',size,' Mb')
        

