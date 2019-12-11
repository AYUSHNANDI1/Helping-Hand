from __future__ import print_function
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
	print ("Make sure that you have saved changes to master!"),
	print ("If sure key in Y/N")
	status = raw_input("Enter status")  # This variable takes in yes or no from user
	if status=="Y":
	
		
	else:
		print ("So you haven't saved changes yet!")
		exit()


