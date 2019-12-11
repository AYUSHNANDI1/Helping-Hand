import tarfile
import os
import subprocess
direct= subprocess.check_output(['pwd'])
direct=direct.rstrip()
directory=str(direct)
print(os.listdir(directory))

tar = tarfile.open("sample.tar", "w:tar")
for filename in os.listdir(directory):
	if filename=="majordir":
		tar.add(filename)

tar.close()
	
