from datetime import datetime;

time = datetime.utcnow();   #currenttime
print(time);


def myFun(msg, *, dt=datetime.utcnow()):
    print("{0}:{1}".format(dt,msg));

# myFun("text message2")

def myFun1(msg, *, dt=None): #dt is null
    if not dt:
        dt = datetime.utcnow()
        print("{0}:{1}".format(dt,msg));

myFun("text message3")
