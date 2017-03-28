# CmsOpenData

source /cvmfs/cms.cern.ch/cmsset_default.sh

export SCRAM_ARCH=slc5_amd64_gcc434

cmsrel CMSSW_4_2_8

# Create the tree

Inside your CMSSW version 5_3_32 directory, change the directives in datafiles and execute the exeCreateTree.py file with python exeCreateTtree.py 
