import subprocess
import argparse
import sys
import os

class pullChanges:
        def changePull(self):
		#parser1=argparse.ArgumentParser()
		#parser1.add_argument('-p')
		#pull_parser = parser1.parse_args()
		#cmd=pull_parser.p
                #a=str(sys.argv[1])
                #cmd = "git checkout {0}".format(a)
		#print(cmd)
                proc = subprocess.Popen(["git pull"], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                status=out.strip('\n')
                print (status)
	#a=str(sys.argv[1])
	#changePull()
