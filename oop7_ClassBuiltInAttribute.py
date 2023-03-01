#class built in attribute
# __dict__အချက်လက်အားလုံးကိို ပြန်ပြပေးတယ်
# __doc__ classတစ်ခုရဲ့ မှတ်ချက်
# __name__ to access class's name
# __module__
#__bases__ ဒီ classမှာ ဘယ်basesတွေရှိသလဲ , classတခုကနေန ခွဲသွားတဲ့ base classes
class MyClass:
    variable = "programming"
    def active():
        print(f'hello from {MyClass.variable}')  #f=formatted
print(MyClass.__dict__)
