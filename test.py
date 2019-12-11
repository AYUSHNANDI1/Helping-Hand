import shutil
import os
import tarfile
import subprocess


class MoveFile:

	def move(self):
		source = '/tmp/Practice_Ayush/majordir/GIT/Helping-Hand'
		dest1 = '/tmp/Practice_Ayush/production/scripts'
		if not os.path.isdir(dest1):
			os.mkdir(dest1, 0o755)
			print ("Directory Script made!")
			#shutil.rmtree(dest1)
		else:
			print("Deletiing old directory!")
			shutil.rmtree(dest1)
			#est1='/tmp/Practice_Ayush/production/scripts'
			os.mkdir(dest1, 0o755)
			print("Created new directory Script!")

			
		files = os.listdir(source)
                for f in files:
			if os.path.isdir(source+'/'+f):
				shutil.rmtree(dest1, True)
                                shutil.copytree(source+'/'+f,dest1,symlinks=False,ignore=None)
                        else:
                                shutil.copy(source+'/'+f,dest1)
		'''with tarfile.open("samp.tar", "w:gz") as tar:
			tar.add('/tmp/Practice_Ayush/production/', arcname=os.path('/tmp/Practice_Ayush/production/'))'''

		directory=str('/tmp/Practice_Ayush/production/scripts')
		tar = tarfile.open("/tmp/Practice_Ayush/production/Scripts.tar", "w:gz")
		#print(os.listdir(directory))
		for filename in os.listdir(directory):
			#print (filename)
			#if filename=="scripts":
				#print("Found!")
                		tar.add(filename)
				exit()
		tar.close()
