import os
import shutil
import tarfile
import subprocess
import argparse
class allfunction:
        def pull(self):
                proc = subprocess.Popen(["git pull"], stdout=subprocess.PIPE, shell=True)
                (out,err) = proc.communicate()
                status = out.strip('\n')
                print(status)
        def checkout(self):
                self.pull()
                parser1=argparse.ArgumentParser()
                parser1.add_argument('-co')
                pull_parser = parser1.parse_args()
                cmd=pull_parser.co
                #a=str(sys.argv[1])
                #cmd = "git checkout {0}".format(a)
                #rint(cmd)
                #roc = subprocess.Popen(["git add -A"], stdout=subprocess.PIPE, shell=True)
                #out, err) = proc.communicate()
                #tatus=out.strip('\n')
                #roc2 = subprocess.Popen(["git commit -m 'NewCommit'"], stdout=subprocess.PIPE, shell=True)
                #out2, err2) = proc2.communicate()
                #tatus2=out.strip('\n')
                #rint ("ADDED AND COMMITED")
                #rint(status2)
                proc3 = subprocess.Popen(["git checkout"+' '+cmd], stdout=subprocess.PIPE, shell=True)
                (out3, err3) = proc3.communicate()
                status3=out3.strip('\n')
                print (status3)

        def convertTar(self):
                self.checkout()
                self.pull()
                print("Converting to tar")
                source = '/tmp/Practice_Ayush/majordir/GIT/Helping-Hand'
                dest1 = '/tmp/Practice_Ayush/scripts'
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
                                #shutil.rmtree(dest1, True)
                                #shutil.copytree(source+'/'+f,dest1,symlinks=False,ignore=None)
                                print("Did not move any git file!")
                        else:
                                shutil.copy(f,dest1)
                print("Moved all the files sucessfully!!")
                '''Compare here whether master branch or else..'''
                proc = subprocess.Popen(["git rev-parse --abbrev-ref HEAD"], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
		print("This is"+out+"branch")
                if (out.strip('\n') )== "master":
			print("Heyyyyy I havee commeee to MASTERRRRRRR!")
                        directory=str(dest1)
                        tar = tarfile.open("/tmp/Practice_Ayush/scripts.tar", "w:tar")
                        #print(os.listdir(directory))
                        for filename in os.listdir(directory):
                                #print (filename)
                                #if filename=="scripts":
                                #print("Found!: ", filename)
                                tar.add(filename)
                                        #exit()
                        tar.close()
                else:
                        directory=str(dest1)
                        tar = tarfile.open("/tmp/Practice_Ayush/DEV.tar", "w:tar")
                        #print(os.listdir(directory))
                        for filename in os.listdir(directory):
                                #print (filename)
                                #if filename=="scripts":
                                #print("Found!: ", filename)
                                tar.add(filename)
                                        #exit()
                        tar.close()
