import shutil
import os
import tarfile
import subprocess


class MoveFile:

	def move(self):
		source = '/tmp/Practice_Ayush/majordir/GIT/Helping-Hand'
		dest1 = '/tmp/Practice_Ayush/production/scripts'
		if os.path.isdir(dest1):
			os.rmdir(dest1)

			files = os.listdir(source)
                        for f in files:
                                if os.path.isdir(source+'/'+f):
                                #print(f)
                                        shutil.rmtree(dest1, True)
                                        shutil.copytree(source+'/'+f,dest1,symlinks=False,ignore=None)
                                else:
                                        shutil.copy(source+'/'+f,dest1)

		else:

			files = os.listdir(source)
			for f in files:
				if os.path.isdir(source+'/'+f):
				#print(f)
					shutil.rmtree(dest1, True)
					shutil.copytree(source+'/'+f,dest1,symlinks=False,ignore=None)
				else:
					shutil.copy(source+'/'+f,dest1)

		tar = tarfile.open("scripts.tar", "w:tar")
		for filename in os.listdir(dest1):
			if filename=="scripts":
                		tar.add(filename)

		tar.close()
