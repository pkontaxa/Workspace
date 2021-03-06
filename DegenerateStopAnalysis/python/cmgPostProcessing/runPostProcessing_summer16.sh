#!/bin/sh

# shell script to run runPostProcessing_v2.py  
# Steps:
#    Prerequisite:
#      set-up the production release (e.g. via manageRelease.sh from script directory)
#      in the base repository (where the release was checked out)
#        ln -s CMSSW_8_0_11/src/Workspace/DegenerateStopAnalysis/python/cmgPostProcessing/runPostProcessing.sh .
#    Run steps:   
#       From the base repository, where the link was done:
#       nohup krenew -t -K 10 -- bash -c "./runPostProcessing.sh $1 [$2 [$3] [$4] [$5]]" & ; disown
#
#       $1 compulsory; 
#          set sample as defined in runPostProcessing.py
#       $2 must be set to 'MC' for MC samples, and to 'DATA' for data
#          take cmgTuples=${CMG_TUPLES} as defined below in the if block
#       $3 if set to "skimPreselect", run skimPreselect, otherwise do not run skimPreselect
#          set it to "" if there is another non-empty parameter after it
#       $4 if set to "skimLepton", run skimLepton, otherwise do not run skimLepton
#          set it to "" if there is another non-empty parameter after it
#       $5 optional;
#          if 'TEST', add to "_TEST" to CMG_POST_PROCESSING_TAG, e.g. "80X_postProcessing_v2_TEST"
#          with 'TEST', it also add '--verbose'
#
# 
# The parameters to be used are available in 
#   ${CMSSW_BASE}/src/Workspace/DegenerateStopAnalysis/python/cmgPostProcessing/cmgPostProcessing_parser.py
#   ${CMSSW_BASE}/src/Workspace/DegenerateStopAnalysis/python/cmgPostProcessing/runPostProcessing.py
# adapt them below to the desired values. If not set here, the default parameters will be used

# activate debugging
#set -vx

# release and architecture, 
CMSSW_RELEASE="CMSSW_8_0_20"
SCRAM_ARCH_VAL="slc6_amd64_gcc530"
CMSSW_ACTION="RO"

# set parameters 

# cli parameters
SAMPLE_SET=$1

# hard-coded parameters - modify them according to desired full set
RUNMODE="BATCH"
CMG_PROCESSING_TAG="8025_mAODv2_v7"
CMG_POST_PROCESSING_TAG="80X_postProcessing_v1"
PARAMETER_SET="analysisHephy_13TeV_2016_v2_3"
CHUNK_SPLITTING="50"
#CHUNK_SPLITTING=""
VERBOSE="--verbose"
#VERBOSE="" 

# semi-hard-coded parameters
if [[ ${2} == "DATA" ]]; then 
    CMG_TUPLES="Data2016_v7"
    BTAG_WEIGHTS=""
    BATCH_TAG="Data"
else
    CMG_TUPLES="RunIISummer16MiniAODv2_v7"
    BTAG_WEIGHTS="--processBTagWeights"
    BATCH_TAG="MC"
fi

if [[ ${3} == "skimPreselect" ]]; then 
    SKIM_PRESELECT="--skimPreselect"
else
    SKIM_PRESELECT=""
fi

if [[ ${4} == "skimLepton" ]]; then 
    #SKIM_LEPTON="--skimLepton=oneLep20"
    #SKIM_LEPTON="--skimLepton=oneLepGood20"
    CHUNK_SPLITTING="10"
    #SKIM_LEPTON="--skimLepton=oneLepGood_HT800"
    SKIM_LEPTON="--skimLepton=oneElGood50_ISR100_MET40_MT30"
elif [[ ${4} == "LT120" ]]; then
    CHUNK_SPLITTING="10"
    SKIM_LEPTON="--skimLepton=LT120"
else
    SKIM_LEPTON=""
fi

if [[ ${5} == "TEST" ]]; then 
    CMG_POST_PROCESSING_TAG=$CMG_POST_PROCESSING_TAG"_TEST"
    VERBOSE="--verbose"
fi

if [[ ${CHUNK_SPLITTING} ]]; then
    SPLIT_CHUNKS="--splitChunks "$CHUNK_SPLITTING
else
    SPLIT_CHUNKS=""
fi

if [[ ${RUNMODE} == "BATCH" ]]; then
    echo "Creating batch script (to run set RUNMODE to RUN).."
    BATCHSCRIPTNAME="batchScript-"$CMG_PROCESSING_TAG"-"$CMG_POST_PROCESSING_TAG"-"$BATCH_TAG 
    RUNOPT="--batchScript  --batchScriptName "$BATCHSCRIPTNAME
    
elif [[ ${RUNMODE} == "RUN" ]]; then
    RUNOPT="--run"
fi


# the rest of the parameters are the default parameters from cmgPostProcessing_parser.py

if [[ ${CMSSW_ACTION} == "CB" || ${CMSSW_ACTION} == "R" ]]; then

    export SCRAM_ARCH=${SCRAM_ARCH_VAL}

    scram project CMSSW ${CMSSW_RELEASE}
    cd ${CMSSW_RELEASE}/src
    eval `scram runtime -sh`
fi

if [[ ${CMSSW_ACTION} == "RO" || ${CMSSW_ACTION} == "R" ]]; then
    
    cd ${CMSSW_BASE}/src/Workspace/DegenerateStopAnalysis/python/cmgPostProcessing
            
    python runPostProcessing_summer16.py \
        --logLevel=INFO \
        --sampleSet=${SAMPLE_SET} \
        --cmgTuples=${CMG_TUPLES} \
        --parameterSet=${PARAMETER_SET} \
        --cmgProcessingTag=${CMG_PROCESSING_TAG} \
        --cmgPostProcessingTag=${CMG_POST_PROCESSING_TAG} \
        --processEventVetoFilters \
        ${SKIM_PRESELECT} \
        ${SKIM_LEPTON} \
        ${BTAG_WEIGHTS} \
        ${SPLIT_CHUNKS} \
        ${RUNOPT} \
        ${VERBOSE}
fi

# deactivate debugging
#set +vx

exit 0
