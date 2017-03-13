# class FirsClass:
#     def setData(self, value):
#         self.data = value
#     def display(self):
#         print(self.data)
#
# class SecondClass(FirsClass):
#     def display(self):
#         print("Current value = %s" % self.data)
#
# class ThirdClass(SecondClass):
#     def __init__(self, value):
#         self.data = value
#     def __add__(self, other):
#         return ThirdClass(self.data + other)
#     def __str__(self):
#         return '[ThirdClass: %s]' % self.data
#     def mul(self, other):
#         self.data *= other
#
# test = FirsClass()
# test2 = SecondClass()
# test.setData(199)
# test2.setData(1996)
# a = ThirdClass('abc')

class rec: pass


rec = {}
rec['name'] = 'Bob'
rec['surname'] = 'Marley'
rec['job'] = 'Trainer/writer'
print(rec['name'])