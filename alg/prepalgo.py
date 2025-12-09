import math
from prereq.primegen import primegen

def diffusion (seqlist,site,sitel,primechl):
    for char in site:
        char = ord(char)
        sitel.append(char)
        
    for ordch in sitel:
        for i in range(1):
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
        
        ordch = math.floor(ordch) #gives the ascii secured characters of site
        primech = primegen(ordch)
        ordch *= primech # primech is the ordch-th prime number
        primechl.append(ordch) # primechl is the list containing ordch*primech
    print(primechl)
    return primechl

