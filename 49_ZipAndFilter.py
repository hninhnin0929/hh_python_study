itrl1 = [1,2,3,4,5]
itrl2 = [10,20,30,40,50,60]

results = zip(itrl1, itrl2)
print(results)
for i in results:
    print(i)

alphabet = ['a','b','c','d','e','f','i','o','u','j','k']

print("Testing filter()")
def VowelFilter(alphabet):
    vowel = ['a','e','i','o','u']
    if(alphabet in vowel):
        return True
    else:
        return False


filterVowel = filter(VowelFilter, alphabet)
print(filterVowel)
for i in filterVowel:
    print(i)