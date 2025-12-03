def sequence(keylist):
    
    for i in range(0,len(keylist)-1): # [39,45,85,39,45,112]
        keylist[i+1] = keylist[i+1]+keylist[i]*keylist[i]+(keylist[i])*2
    return keylist