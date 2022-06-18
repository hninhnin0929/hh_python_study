#CSPRNG
#Cryptographically strong Psedo_Random Generator
#random
#secrets 3.6

import secrets

print('Printing integer number using secrets module')

secureGenerator = secrets.SystemRandom()
number_list = [1,2,3,6,7,10,14,50,88]
randomNumber = secureGenerator.choice(number_list)
print('Secure random Number is', randomNumber)

print(secrets.token_hex()) #1 byte change to two hex digits

#URL -safe test string

passwordresetLink = "https://winhtut.com/crazycoder/reset="
passwordresetLink += secrets.token_urlsafe(4)
print('Generating secure URL', passwordresetLink)


