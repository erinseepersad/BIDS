# os.listdir('directory_path') function
@GregKronberg line 24 i am unsure what condition to put
# cd?
# instructions: look at OS and create something where you can get a list of all the directories stored
import os
# navigating my directory path
directory_path= '/Users/qercA/Downloads/mount_data'
# getting a list of all the files in the directory from the previous line
allentries = os.listdir(directory_path)
# make a list of the files 
print ('List of files')
for entry in allentries:
    print(entry)
    #file_path= os.path.join(directory_path, entry)
    # check if file needs conversion based on specific conditions
    #if needs_conversion(entry):
    # try convert_file(file_path)
      #except: breakpoints -- print file name to check the file 
    #else:
    #print("Skipping file: {}".format(file_path))
# now go through the files in the directory make sure they are BIDS format- JACK
# check if file needs conversion
#REMINDER: REARRANGE CODE, THIS FIRST AFTER DIRECTORY PATH
def needs_conversion(file_name):
    #what condition?
# conversion
    #Jacks code 
    
