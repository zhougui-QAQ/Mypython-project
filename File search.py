import shutil
import os
path = 'xxx'#你的目录
files = os.listdir(path)
for f in files:
    if 'xx'in f and f.endswith('.py'):#文件名和后缀
        print('yes ' +   f)
        shutil.copy('xx', 'xxx')#复制 目录文件到xxx
