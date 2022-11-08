import os

dirpath = os.getcwd()

with open('file_a.txt', mode='w+') as new:
    new.write('It\'s name')
    new.seek(0)
    print(new.read())
