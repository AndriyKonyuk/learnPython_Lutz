from classtools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = round(self.pay * (1 + float(percent)), 2)

    # def __str__(self):
    #     return '[%s: %s, %s, %s]' % (self.__class__.__name__, self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
# class Manager():
#     def __init__(self, name, pay):
#         self.person = Person(name, 'mgr', pay)
#
#     def giveRaise(self, percent, bonus=.1):
#         self.person.giveRaise(percent + bonus)
#
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)
#
#     def __str__(self):
#         return str(self.person)
#
#
# class Department:
#     def __init__(self, *args):
#         self.members = list(args)
#
#     def addMember(self, person):
#         self.members.append(person)
#
#     def giveRaises(self, percent):
#         for person in self.members:
#             person.giveRaise(percent)
#
#     def showAll(self):
#         for person in self.members:
#             print(person)


if __name__ == '__main__':
    bob = Person('Bob Marley')
    sue = Person('Sue Garner', 'dev', 1000)
    tom = Manager('Tom Raider', 1000)
    # print(tom.person)
    # for ob in (bob, sue):
    #     ob.giveRaise(.1)
    #     print(ob)
    # print(dir(bob))