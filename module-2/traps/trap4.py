# trap4.py -- predict both lines, then run it.
count = 0
names = ['Earth']


def bump():
    global count
    count = count + 1


def add_mars():
    names.append('Mars')


bump()
bump()
add_mars()
print(count)
print(names)
