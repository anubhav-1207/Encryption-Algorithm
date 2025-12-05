import math

def algorithm(seqlist,site,sitel):
    for char in site:
        char = ord(char)
        sitel.append(char)
        
    for ordch in sitel:
        for i in range(91824):
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
            ordch >>= 8253
            ordch += 752
            ordch += 234234
            ordch += 7372
            ordch *= 143
            
            
            ordch %= 1234
        
        ordch = math.floor(ordch)
        print(ordch)


            
            


        