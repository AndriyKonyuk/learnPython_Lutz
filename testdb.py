import shelve

db = shelve.open('persondb')
for i in db:
    print(db[i])