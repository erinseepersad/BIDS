#os.listdir('directory_path') function
@GregKronberg
# cd?
# instructions: look at OS and create something where you can get a list of all the directories stored
import os
# my directory path
directory_path= '/Users/qercA/Downloads/mount_data'
# getting a list of all the files in the directory from the previous line
allentries = os.listdir(directory_path)
# make a list of the files 
print ('List of files')
for entry in allentries:
    print(entry)
