# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:18:06 2023

@author: qercA
"""

#class-->object--> variables and functions

# example from website
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""
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

bids_path = BIDSPath(subject='aliens9', session='payoff1', task='rocket1', acquisition='quicktutorial1', modality='raw', run='s20031', suffix='raw', extension='.iqdat')
print(bids_path)

#insert the file name 
input_file = input("Enter the input file path: ")
#convert to BIDS
def conversion_filename (given_filename):
    breakingdown= input_file_name.split('_')
    #convert to BIDS format
    """
    subject_label = 
    session_label = 
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
