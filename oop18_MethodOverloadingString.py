class Price:
    def payment(self, dataType, *args):   #arbitray argumeent
        if dataType == "int":
            data = 0
            count = 0
            for i in args:
                count +=1
                data = data + i
            print("Parameter type is Integer")
            print("There are {0} parameters passedd ".format(count))
            return data
        elif dataType == "str":
            data = ''
            count = 0
            for i in args:
                count +=1
                data = data + i
            print("Parameter type is STring")
            print("There are {0} parameters passedd ".format(count))
            return data


obj = Price()
print(obj.payment('int',10,5))
print(obj.payment('int',2,2,2,2,2,2))
print(obj.payment('str','aung', 'aung'))
print(obj.payment('str','i', 'am', 'hnin'))

