def binaryToDec(b): #binary will pass
    num = b
    dec = 0
    base = 1    #2^0 =1
    temp = num
    while(temp): # loop until temp is zero
        digit = temp%10
        temp = int(temp/10)
        dec += digit * base
        base = base * 2
    return dec

bnumber = 1010
print(binaryToDec(bnumber))
