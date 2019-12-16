import tarfile
import os
import subprocess
#direct= subprocess.check_output(['pwd'])
#direct=direct.rstrip()
#directory=str(direct)
k=(os.listdir('/tmp/Practice_Ayush/production/'))
print(k)
tar = tarfile.open("sample.tar", "w:tar")
#print(os.listdir('/tmp/Practice_Ayush/production/'))
for filename in k:
        #if filename == "new":
	print(filename)
        tar.add(filename)
tar.close()	
