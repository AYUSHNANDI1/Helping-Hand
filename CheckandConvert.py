from __future__ import print_function
from test import MoveFile
from pull import pullChanges
import os
import subprocess
proc = subprocess.Popen(["git rev-parse --abbrev-ref HEAD"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
get_branch=out.strip('\n')
print (get_branch)

moving_object = MoveFile()

if get_branch=="master":
	#print("Here")
	#print ("Make sure that you have saved changes to master!"),
	#print ("If sure key in Y/N")
	status = raw_input("Make sure that you have saved changes to master! If sure, key in Y/N:")  # This variable takes in yes or no from user
	if status=="Y":
		print("We are now ready to move files to Packaging folder!")

		moving_object = MoveFile()
		moving_object.move()

		
	else:
		print ("So you haven't saved changes yet!")
		exit()

else:
	print("This is not master, hence pulling changes first!")
	#status2=raw_input("Would you like to make changes!")
	pul = pullChanges()
	pul.changePull()
	print("Now packing the local branches!")
	moving_object.moveLocal()			
