# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:18:06 2023

@author: qercA
"""

#class-->object--> variables and functions
"""
# example from website
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

filename template
key1-value1_key2-value2_suffix.extension

bids_path = BIDSPath(subject='test', session='two', task='mytask',
                     suffix='events', extension='.tsv')
print(bids_path)
"""

#converting to filename 
#sub-aliens9_ses-payoff1_task-rocket1_acq-quicktutorial1_mod-raw_run-s20031.iqdat
from mne_bids import BIDSPath #website 
import os
import datetime
import pandas as pd 

bids_path = BIDSPath(subject='aliens9', session='payoff1', task='rocket1', acquisition='quicktutorial1', modality='raw', run='s20031', suffix='raw', extension='.iqdat')
print(bids_path)

#grabbing the file from the directory

def get_file_from_directory(directory_path, file_name):
    if not os.path.isdir(directory_path):
        print("Error: The provided path is not a directory.")
        return None

    #list of files in the directory 
    file_list = os.listdir(directory_path)

    # Search for the desired file in the list
    for file in file_list:
        if file == file_name:
            return os.path.join(directory_path, file)

    # If the file is not found, return None
    return None
#??????
directory_path = "/path/to/your/directory"
file_name = "your_file.txt"

#full file path
file_path = get_file_from_directory(directory_path, file_name)

# Check if the file was found and print the result
if file_path:
    print("File found at:", file_path)
else:
    print("File not found in the directory.")

#convert to BIDS
def conversion_filename (given_filename):
    breakingdown= input_file_name.split('_')
    #convert to BIDS format
    """
    subject_label = narc iD
    session_label = the date 
    task_label =
    acquisition_label = 
    modality_label = 
    run_index = 
    suffix = 
    extension = 
    """
    subject_label = breakingdown[0][4:] 
    session_label = breakingdown[1][4:]  
    task_label = breakingdown[2][5:] 
    acquisition_label = breakingdown[3][4:]  
    modality_label = breakingdown[4][4:]  
    run_index = breakingdown[5][4:]  
    suffix, extension = breakingdown[6].split('.')
    bids_filename = f"sub-{subject_label}_ses-{session_label}_task-{task_label}_acq-{acquisition_label}_mod-{modality_label}_run-{run_index}_{suffix}.{extension}"
    
    return bids_filename
input_file_name = os.path.basename(input_file)

bids_file_name = converion_filename(given_filename)#input filename to bids

#upload as a normal folder
new_file= open(input_file, "x")

print("BIDS File Name:", bids_file_name)
