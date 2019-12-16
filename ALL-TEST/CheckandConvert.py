from __future__ import print_function
from test import MoveFile
from pull import pullChanges
from checkoutbranch import checkout
import os
import subprocess

cout = checkout()  # objecrt created for checkout class
cout.chkout()      # Can checkout to desired branch

proc = subprocess.Popen(["git rev-parse --abbrev-ref HEAD"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
get_branch=out.strip('\n')
print (get_branch)

#oving_object = MoveFile()
if get_branch=="master":
        #print("Here")
        #print ("Make sure that you have saved changes to master!"),
        #print ("If sure key in Y/N")
        #status = raw_input("Make sure that you have saved changes to master! If sure, key in Y/N:")  # This variable takes in yes or no from user
        #if status=="Y":
        #       print("We are now ready to move files to Packaging folder!")
        #
        #       moving_object = MoveFile()
        #       moving_object.move()


        #else:
        #       print ("So you haven't saved changes yet!")
        #       exit()
        print("Pulling changes first")
        pul = pullChanges()
        pul.changePull()
        print("Now packing branches to production!")
        moving_object1 = MoveFile()
        moving_object1.moveLocal()

else:
		
	print("This is not master, hence pulling changes first!")
	#status2=raw_input("Would you like to make changes!")
	pul = pullChanges()
	pul.changePull()
	print("Now packing the local branches!")
	moving_object1 = MoveFile()
	moving_object1.moveLocal()			
