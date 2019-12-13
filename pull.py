import subprocess
import argparse
import sys
import os

class pullChanges:
	def changePull(self):
		a=str(sys.argv[1])
		cmd = "git pull {0}".format(a)
		proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		status=out.strip('\n')
		print (status)



