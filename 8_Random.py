import random

print(random.random()) #0.0 => 1.0 float


#randint()
#randrange()

print("printingr random integer", random.randint(0,9))

print("printingr random integer", random.randrange(0,10,2))

#ramdom.choice
#random.sample
#random.seed(5) current time
#stdlib.h srand()
#random.shuffle() list tuple
#random.uniform(start, end) #floating point
#random.triangular

name = ['hnin', 'snow', 'nay', 'thura']
print('select element', random.choice(name))
print('select element', random.sample(name,3))

random.seed(9)
print('random number from seed()', random.random())

print('before shuffle', name)
random.shuffle(name)
print('after shuffle', name)

print('uniform ', random.uniform(10.5, 20.5))
print('uniform ', random.triangular(10.5, 20.5,5.5))