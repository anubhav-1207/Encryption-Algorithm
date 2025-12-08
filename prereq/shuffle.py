import prereq
from prereq.primegen import primegen

def sequence(keylist):
    
    for i in range(0,len(keylist)-1):
        keylist[i] = keylist[i+1]+keylist[i]*keylist[i]+(keylist[i])*2
    return keylist

def seqmix(keylist):
    for elem in keylist:
        elem *= primegen(elem)