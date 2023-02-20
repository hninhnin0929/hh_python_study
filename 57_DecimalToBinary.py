def decToBinary(n):
    binary = [0]*n  #to store binary number       # increase array size by n
    i = 0   #counter
    while(n>0):
        binary[i] = n%2
        n = int(n/2)
        i += 1
    for x in range(i-1, -1, -1):
        print(binary[x], end="")

decimalNumber = int(input("please eneter decimal number: "))
decToBinary(decimalNumber)