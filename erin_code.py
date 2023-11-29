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

    # how flexible does our code have to be for differnet environments, can we assume that these people have the directories
    #on their computers or would I need to code something to make a new directroy-- assume they have a folder of raw data 
    
  # raw to converted, if file doesnt exist, if you dont have permission   
import shutil
import os

source_path = '/path/to/source/file.txt'
destination_path = '/path/to/destination/'

try:
    # Move the file from the source directory to the destination directory
    shutil.move(source_path, destination_path)
    print(f"File moved successfully from {source_path} to {destination_path}")
except FileNotFoundError:
    print("Source file not found.")
except PermissionError:
    print("Permission error. Check if you have the necessary permissions.")
except Exception as e:
    print(f"An error occurred: {e}")

# is jacks code check conversion internally or do I have to do that before it passes in
# only accept files that need bids conversion-- yes, if its already converted then it would just keeo it the same 
#mount datda_> unzipping the folder

#run jacks code first, see if errors, try to fix them, how well does it work?
#add comments to jack code 
