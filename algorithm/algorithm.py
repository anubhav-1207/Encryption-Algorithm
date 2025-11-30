import random as random 

def encrypt(Data):
    password = ""
    for i in Data:
        ordinal_i = (ord(i))
        shift = random.randint(0,25)
        char = ordinal_i + shift
        charac_char = chr(char)
        password += charac_char
    print(password)
        

encrypt('Turtle')