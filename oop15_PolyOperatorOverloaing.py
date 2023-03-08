class People:   #id,age
    def __init__(self, id, age) -> None:
        self.id = id
        self.age = age
    def __add__(self, self1):
        data_id = self.id + self1.id 
        data_age = self.age + self1.age 
        return  data_id, data_age

p1 = People(111, 20)
p2 = People(222, 30)
p3 = People(333, 40)
total = p1+p2
dataId, dAge = total
print(total)
print(dataId, dAge)
p4 = People(dataId, dAge)
finalTotal = p4 + p3
print(finalTotal)
dataId, dAge = finalTotal
result = dataId+ dAge
print(result)