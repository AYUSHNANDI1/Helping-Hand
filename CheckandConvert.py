from __future__ import print_function
from test import MoveFile
import os
import subprocess
#branch=raw_input("Enter branch_name:")

#Filename=raw_input("Enter file names:")


#get_branch= os.system('git rev-parse --abbrev-ref HEAD')
#getpwat=os.system('pwd')

#get_new_branch= (str(get_branch).rstrip('\n0'))

#print ("Yes")
proc = subprocess.Popen(["git rev-parse --abbrev-ref HEAD"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
get_branch=out.strip('\n')
print (get_branch)

if get_branch=="master":
	print("Here")
	#print ("Make sure that you have saved changes to master!"),
	#print ("If sure key in Y/N")
	status = raw_input("Make sure that you have saved changes to master! If sure, key in Y/N")  # This variable takes in yes or no from user
	if status=="Y":
		print("We are now ready to move files to Packaging folder!")

		moving_object = MoveFile()
		moving_object.move()

		
	else:
		print ("So you haven't saved changes yet!")
		exit()

else:
	print("Please update the changes to master if required!")
	status2=raw_input("Would you like to make changes!")
	if status2=="Y":
		print("Done!")
	else:
		

