# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os

name_project = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(name_project):
    os.mkdir(name_project)
os.chdir(name_project)
[os.mkdir(folder) for folder in folders if not os.path.exists(folder)]

with open('starter.txt', 'w', encoding='utf-8') as f:
    f.writelines([name_project, '\n'])
    [f.writelines([os.path.join(name_project, folder), '\n']) for folder in folders]

