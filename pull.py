import subprocess
import argparse
import sys
import os
#parser = argparse.ArgumentParser()
#parser.add_argument(type=str)
#args = parser.parse_args()

#branch=raw_input("Enter branch_name:")

#Filename=raw_input("Enter file names:")

a=str(sys.argv[1])
#print(a)

#get_branch= os.system('git rev-parse --abbrev-ref HEAD')
#getpwat=os.system('pwd')

#get_new_branch= (str(get_branch).rstrip('\n0'))
cmd = "git pull {0}".format(a)
print (cmd)
#print ("Hello")
#print ("Yes")
#os.system("cmd")
#proc = subprocess.Popen(["cmd"], stdout=subprocess.PIPE, shell=True)
proc = subprocess.Popen(["git pull"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
status=out.strip('\n')
print (status)



