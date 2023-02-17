def mySum(x1,y1):
    return x1+y1
def myReduce(mySum, seq):   #sequence
    first = seq[0]
    for i in seq[1:]:
        first = mySum(first,i)
    return first

list = [1,2,3,4,5,6]
print(myReduce(mySum, list))