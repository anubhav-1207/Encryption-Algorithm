def algorithm(primechl,keylist,finalPassword):
    primechl.extend(keylist)
    determinedPassword = primechl
    # print(primechl)
    # print(keylist)
    print(determinedPassword)
    for i in range(0,len(determinedPassword)-1):
        determinedPassword[i] += determinedPassword[i+1]
        determinedPassword[i] += determinedPassword[i+1]

    for elem in determinedPassword:
        elem = (elem%90)+33
        elem = chr(elem)
        finalPassword += elem
    

    print(finalPassword)
    