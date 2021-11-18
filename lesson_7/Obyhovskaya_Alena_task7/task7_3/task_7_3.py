import os
import shutil


# читаем файл и создаем папки  и файлы с нужной структурой
with open('paths_task3.txt', 'r') as f:
    for line in f.read().splitlines():
        print(line)
        if line.find('.') == -1:
            if not os.path.exists(line):
                os.mkdir(line)
        elif not os.path.isfile(line):
            fl = open(line, "a")

root_dir = 'my_project'
dct_dir = 'my_project/templates'
for dir_path, dir_names, file_names in os.walk(root_dir):
    if dir_path.split('\\')[-1] == 'templates':
        for name in dir_names:
            scr = os.path.join(dir_path, name)
            dct = os.path.join(dct_dir, name)
            if not os.path.exists(dct):
                shutil.copytree(scr, dct)