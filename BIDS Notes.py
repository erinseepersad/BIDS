# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:53:04 2023

@author: qercA
"""

# conda install -c conda-forge pybids ( i used this in the terminal to download)
#  conda install conda=23.5.2 ( i used to update )
# https://bids-standard.github.io/pybids/layout/index.html this is the link i used to take notes for BIDS

#LOADING BIDS DataSet
bids.layout.BIDSLayout class
from os.path import join
from bids import BIDSLayout
from bids.tests import get_test_data_path
layout = BIDSLayout(join(get_test_data_path(), 'synthetic'))
# this is a containor for all of the files stored in the project directory. 
#it allows us to identify the BIDS present in the files path.
#since its in a container it helps us execute queries across the file tree
# meaning, it allows you to get specific or groups of files based on certain standards

#to exclude folders from indexing:
BIDSLayout(bids_dir, ignore=[re.compile(r"(sub-(?!25)\d*/)")])
# this ignores all subjects except "25"

#QUERYING DATASETS (questioning its validity)
#get a list of subjects in a dataset:
layout.get_subjects()
#list of all available sessions:
layout.get_sessions()
#list of tasks
layout.get_task()

#Extracting metadata(set of data that describes and gives information about other data)
# if we want event (task timing) information for a given fMRI scan, we can use:
f = layout.get(task='nback', run=1, extension='nii.gz')[0].filename
layout.get_events(f)

#you can also extract metadata from the json files associated with a scan file:
f = layout.get(task='nback', run=1, extension='nii.gz')[0].filename
layout.get_metadata(f)

#OVERVIEW OF THE ANALYSIS MODULE 
# the bids models specification is an extension to the BIDS standard for describing and organzining 
#general linear models 

#sample code from the website. 
#this assumes that we have a root folder containing a BIDS-compliant project as well as a BIDS models JSON specification
from bids.modeling import BIDSStatsModelsGraph
# Initialize the BIDSStatsModelsGraph
analysis = BIDSStatsModelsGraph('/bidsproject', 'model1.json')
# Setup constructs all the design matrices
analysis.setup()
# Sample query: retrieve first-level design matrix for one run
dm = analysis[0].get_design_matrix(subject='01', run=1, task='taskA')
# Sample query: retrieve session-level contrast matrix
cm = analysis[1].get_contrasts(subject='01', session='retest')


#INITIALIZING REPORTS
bids.reports.BIDSReport class #requires bids.BidsLayout object as an arguent
from os.path import join
from bids import BIDSLayout
from bids.reports import BIDSReport
from bids.tests import get_test_data_path
layout = BIDSLayout(join(get_test_data_path(), 'synthetic'))
report = BIDSReport(layout)

#generating reports you use the generate method( an action that an object is able to perform) it returns a collections.Counter of reports
#sample code from website
counter = report.generate()
main_report = counter.most_common()[0][0]
print(main_report)
r"""
For session 01:
    MR data were acquired using a UNKNOWN-Tesla MANUFACTURER MODEL MRI scanner.
    Ten runs of N-Back UNKNOWN-echo fMRI data were collected (64 slices; repetition time, TR=2500ms;
echo time, TE=UNKNOWNms; flip angle, FA=UNKNOWN<deg>; field of view, FOV=128x128mm;
matrix size=64x64; voxel size=2x2x2mm). Each run was 2:40 minutes in length, during
which 64 functional volumes were acquired.
    Five runs of Rest UNKNOWN-echo fMRI data were collected (64 slices; repetition time, TR=2500ms;
echo time, TE=UNKNOWNms; flip angle, FA=UNKNOWN<deg>; field of view, FOV=128x128mm;
matrix size=64x64; voxel size=2x2x2mm). Each run was 2:40 minutes in length, during
which 64 functional volumes were acquired.

For session 02:
    MR data were acquired using a UNKNOWN-Tesla MANUFACTURER MODEL MRI scanner.
    Ten runs of N-Back UNKNOWN-echo fMRI data were collected (64 slices; repetition time, TR=2500ms;
echo time, TE=UNKNOWNms; flip angle, FA=UNKNOWN<deg>; field of view, FOV=128x128mm;
matrix size=64x64; voxel size=2x2x2mm). Each run was 2:40 minutes in length, during
which 64 functional volumes were acquired.
    Five runs of Rest UNKNOWN-echo fMRI data were collected (64 slices; repetition time, TR=2500ms;
echo time, TE=UNKNOWNms; flip angle, FA=UNKNOWN<deg>; field of view, FOV=128x128mm;
matrix size=64x64; voxel size=2x2x2mm). Each run was 2:40 minutes in length, during
which 64 functional volumes were acquired.

Dicoms were converted to NIfTI-1 format. This section was (in part) generated
automatically using pybids (0.5)."""

#generating reports on subsets of data
# using generate allows for keyword restrictions. for example to generate a report only for nback task data in session 01:
ounter = report.generate(session='01', task='nback')
main_report = counter.most_common()[0][0]
print(main_report)
r"""
For session 01:
  MR data were acquired using a UNKNOWN-Tesla MANUFACTURER MODEL MRI scanner.
  Ten runs of N-Back fMRI data were collected (64 slices; repetition time,
TR=2500ms; echo time, TE=UNKNOWNms; flip angle, FA=UNKNOWN<deg>; field of
view, FOV=128x128mm; matrix size=64x64; voxel size=2x2x2mm). Each run was
2:40 minutes in length, during which 64 functional volumes were acquired.

Dicoms were converted to NIfTI-1 format. This section was (in part)
generated automatically using pybids (0.5)."""