def decToHexa(n): #decimal pass
    hexaDecimal = ['0']*10

    i = 0
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10): #eg 1
            hexaDecimal[i] = chr(temp +48) #character 49=1 (ssee in ascii table)
            i += 1
        else:
            hexaDecimal[i] = chr(temp + 55)
            i = i + 1
        n = int(n/16)

    x = i-1
    while(x >= 0):
        print(hexaDecimal[x], end="")
        x = x - 1

n = 12345
decToHexa(n)