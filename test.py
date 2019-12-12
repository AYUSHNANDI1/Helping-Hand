import shutil
import os
import tarfile
import subprocess


class MoveFile:

	def move(self):
		source = '/tmp/Practice_Ayush/majordir/GIT/Helping-Hand'
		dest1 = '/tmp/Practice_Ayush/production/scripts'
		if not os.path.isdir(dest1):
			os.mkdir(dest1)
			print ("Directory Script made!")
			#shutil.rmtree(dest1)
		else:
			print("Deletiing old directory!")
			shutil.rmtree(dest1)
			#est1='/tmp/Practice_Ayush/production/scripts'
			os.mkdir(dest1)
			print("Created new directory Script!")

			
		files = os.listdir(source)
                for f in files:
			if os.path.isdir(source+'/'+f):
				shutil.rmtree(dest1, True)
                                shutil.copytree(source+'/'+f,dest1,symlinks=False,ignore=None)
				print("Moved tthe directories!")
                        else:
                                shutil.copy(source+'/'+f,dest1)
		print("Moved all the files sucessfully!!")

		directory=str('/tmp/Practice_Ayush/production/')
		tar = tarfile.open("/tmp/Practice_Ayush/production/scripts.tar", "w:tar")
		#print(os.listdir(directory))
		for filename in os.listdir(directory):
			#print (filename)
			if filename=="scripts":
				print("Found!: ", filename)
                		tar.add('/tmp/Practice_Ayush/production/'+filename)
				#exit()
		tar.close()
