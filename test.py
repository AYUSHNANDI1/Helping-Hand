'''import subprocess

proc = subprocess.Popen(["git rev-parse --abbrev-ref HEAD"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
k=out.strip('\n')
print (k)'''

import shutil
import os

source = '/tmp/Practice_Ayush/majordir/GIT/Helping-Hand'
dest1 = '/tmp/Practice_Ayush/production/scripts'


files = os.listdir(source)

for f in files:
        shutil.move(source+f, dest1)
