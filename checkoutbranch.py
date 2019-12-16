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
                proc = subprocess.Popen(["git checkout"+' '+cmd], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                status=out.strip('\n')
                print (status)
        #a=str(sys.argv[1])
        #changePull()

