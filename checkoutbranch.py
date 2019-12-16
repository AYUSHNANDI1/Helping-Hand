import subprocess
import argparse
import sys
import os

class checkout:
        def chkout(self):

                parser1=argparse.ArgumentParser()
                parser1.add_argument('-co')
                pull_parser = parser1.parse_args()
                cmd=pull_parser.co
                #a=str(sys.argv[1])
                #cmd = "git checkout {0}".format(a)
                #rint(cmd)
                proc = subprocess.Popen(["git add -A"], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                status=out.strip('\n')
                proc2 = subprocess.Popen(["git commit -m 'NewCommit'"], stdout=subprocess.PIPE, shell=True)
                (out2, err2) = proc2.communicate()
                status2=out.strip('\n')
                print ("ADDED AND COMMITED")
                print(status2)
                proc3 = subprocess.Popen(["git checkout"+' '+cmd], stdout=subprocess.PIPE, shell=True)
                (out3, err3) = proc3.communicate()
                status3=out.strip('\n')
                print (status3)
        #a=str(sys.argv[1])
        #changePull()

