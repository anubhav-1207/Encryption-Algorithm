import math

# from prereq.primegen import primegen

def keygen(strlist,keylist):
    
    for ordch in strlist:
        for i in range(0,1):
            ordch += 984376
            ordch *= 7445
            ordch -= 231414
            ordch **= 1
            ordch -= 2341
            ordch *= 126
            ordch += 28375
            ordch -= 23
            ordch *= 12
            ordch ^= 34
            ordch += 752
            ordch += 234234
            ordch += 7372
            ordch *= 143
            ordch %= 12346
        
        ordch = math.floor(ordch)
        # primech = primegen(ordch)
        # ordch *= primech
        
        keylist.append(ordch)
        
    print(f'{keylist}: KEYLIST')
    return keylist
