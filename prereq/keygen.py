import math

from prereq.primegen import primegen

def keygen(strlist,keylist):
    
    for ordch in strlist:
        for i in range(0,1):
            ordch += 794538
            ordch *= 74457
            # ordch **= 3
            ordch -= 856478
            # ordch /= 11
            ordch += 9435647
            ordch *= 473456
            ordch ^= 13
            ordch *= 36357
            ordch += 434456
            ordch *= 2456433
            
            ordch += 37653257
            ordch %= 1234
        
        print(ordch)    
        ordch = math.floor(ordch)
        # primech = primegen(ordch)
        # ordch *= primech
        
        keylist.append(ordch)
    
    return keylist



        
