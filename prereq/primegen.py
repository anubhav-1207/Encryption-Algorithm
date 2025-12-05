# def isprime(num):
#     for i in range(2,num-1):
#         if num % i == 0:
#             return False
#             break    
#     else:
#         return True

# i = 0
# limit = 50
# count = 0
# while count != limit:
#     i += 1
#     if isprime(i):
#         count += 1
#         print(i)























def isprime(num):
    for i in range(2,num-1):
        if num%i == 0:
            return False
            break
        else:
            return True
        
def keygen(limit):
    count = 0
    i = 0
    
    while count != limit:
        i += 1
        if isprime(i):
            count += 1
    return i


