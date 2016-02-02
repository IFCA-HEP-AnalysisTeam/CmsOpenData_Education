# Name: execute.py
#
# CMS Open Data
#
# Description: 
#
# Returns: 

import ROOT
from createTTree import createTTree
import time

start_time = time.time()

# CMS data:

data_files = [
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_1.root',
	'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_2.root',
 #       'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_3.root',
  #      'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_4.root'
]

maxEv = 100000 #number of processed events. maxEvents = -1 runs over all of them


t=createTTree(data_files)
tree=t.process(maxEv)

print("--- %s seconds ---" % (time.time() - start_time))


