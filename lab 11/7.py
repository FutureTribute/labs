# Засько Б., КНИТ16-А
# Программа создания каталога NewFold на системном диске, в нем своего каталога, а в нем
# файла со анкетой и вывод анкеты на экран

import os

os.chdir('C:\\NewFold\\')
os.mkdir('Fold')
os.chdir('C:\\NewFold\\Fold\\')
with open('resume.txt', 'w') as f:
    f.write('Засько Богдан, КНИТ16-А')
with open('resume.txt', 'r') as f:
    print(f.read())
