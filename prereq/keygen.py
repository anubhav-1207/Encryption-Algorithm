import math

def keygen(strlist):
    for ordch in strlist:
        for i in range(0,40):
            ordch += 7945387683
            ordch *= 7457
            ordch**3
            ordch -= 8567857
            ordch /= 11
            ordch += 9435647
            ordch *= 47356
            ordch = ((ordch + 175)**3 + 7754)**2 -1757
            ordch *= 365744
            ordch += 4343534647
            ordch = 4453**2 - 7456**2 - 354568 + 4564*ordch
            ordch %= 9504
            ordch *= 245632
            ordch /= 445
            ordch += 37653257
            ordch %= 950
        
            ordch = math.floor(ordch)
        
    print(ordch)



        
