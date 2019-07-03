# -*- encoding:utf-8 -*-

class Person():

    name = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


p1 = Person()
p1.set_name("XiaoMing")
print(p1.get_name())

p2 = Person()
p2.set_name("XiaoHong")
print(p2.get_name())

print(p1.get_name())