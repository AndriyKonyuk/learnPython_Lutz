def countLines(name):
    global f
    f = open(name)
    dov = len(f.readlines())
    return dov
def countChars(name):
    f.seek(0)
    count = +len(f.read())
    return count
def test(name):
    return print('lines in file: '+str(countLines(name))+'\n'+'chars in file: '+ str(countChars(name)))
if __name__ == '__main__':
    test('mymod.py')

print('thi is end for module')
