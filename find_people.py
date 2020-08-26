#coding:utf-8
import os
import glob

path = 'data'
files = glob.glob(os.path.join(path, '*', '*.wav'))
print(files)

names = []
for file in files:
    items = file.split('\\')
    name = items[-2]
    if name not in names:
        names.append(name)

print(names)