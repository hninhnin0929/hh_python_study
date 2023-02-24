from myModule import fibo, listFibo

print(globals())

fibo(10)
print("llist fibo 100")
print(listFibo(100))


# import myModule
# myModule.fibo(10)

#Rewrite Globals to be clear

def print_info(header, info):
    print("***********{0}*******".format(header))
    for key, value in info.items():
        print(key, value)
    print("**********eend of information*********")

print_info('Using Global Function', globals())
print(__name__)

if __name__ == "__main__":
    print("The name was changed to main")
else:
    print("They are not changed")

