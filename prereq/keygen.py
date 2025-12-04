import math

def keygen(strlist,keylist):
    
    for ordch in strlist:
        for i in range(0,4000):
            ordch += 7945387683
            ordch *= 7457
            ordch **= 3
            ordch -= 85678
            ordch /= 11
            ordch += 9435647
            ordch *= 47356
            ordch = ((ordch + 175)**3 + 7754)**2 -1757
            ordch *= 3657
            ordch += 4343534647
            ordch = 4453**2 - 7456**2 - 354568 + 4564*ordch
            ordch *= 245632
            ordch /= 445
            ordch += 37653257
            ordch %= 122
            
        
        ordch = math.floor(ordch)
        
        keylist.append(ordch)
    
    return keylist



        
