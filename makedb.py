from person import Person, Manager
bob = Person('Bob Smith') # Создание объектов для сохранения
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for object in (bob,sue,tom):
    db[object.name] = object
db.close()

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])

tom = db['Tom Jones']
tom.giveRaise(0.1)
db['Tom Jones'] = tom
db.close()
