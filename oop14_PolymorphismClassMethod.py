class AungAung:
    def human(self):
        print("Aung Aung is a programmer")
        print("Aung Aung is always coding")
class MgMg:
    def human(self):
        print("MgMg is a hacker")
        print("MgMg is always learning")
class KoKo:
    def human(self):
        print("KoKo is a scientist")
        print("KoKo is always testing")
class People:
    def func(self, obj):
        obj.human()
agag = AungAung()
mgmg = MgMg()
koko = KoKo()
people = People()
# people.func(agag)

myList = [agag, mgmg, koko]
for obj in myList:
    people.func(obj)