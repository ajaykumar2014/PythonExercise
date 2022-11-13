from com.exam import *


class A:
    att = ['a']
    print(att)


a = A();
print(a)
print(type(a.att))
print(A.__dict__)
print(A.__doc__)
print(module1.say())
print(module2.say())
print(module1.Utils.test(987989))
print(module1.Utils.test1())
print(module1.Utils.test2())
print(emailservice.BaseEmailService.sendEmail('', 'hello  this is testing email.'))
