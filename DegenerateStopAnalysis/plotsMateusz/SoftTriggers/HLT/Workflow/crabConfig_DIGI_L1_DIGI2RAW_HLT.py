#Crab3 Configuration File

from CRABClient.UserUtilities import config
config = config()
#from WMCore.Configuration import Configuration
#config = Configuration()

menuName = 'SoftMuPlusHardJet'
menuVersion = 'V5'
PU = 'PU' # 'noPU'

mStop = "500"
mLSP = "490"

datasetHashes = {\
    '500_420':'e6899ac770b5fd2a8126a98b77f980ae',
    #'500_430':'1e61eb3cb939649820d25e9592686255',
    #'500_440':'4e3ef5c5b8fdf32b5e8fb9f058dd2ff5',
    #'500_450':'53b68c9b95dad72fe2f33903314d66f4',
    '500_460':'0e80182b879d56964403a4714c769c96',
    #'500_470':'7b3c47d810a037e5e041c9914f218b1a',
    #'500_480':'a277bfbe79d79dc678d759fada5de4a3',
    '500_490':'7cd2021cd9cd2ab1c5d0bf1788e358df',
}

outputName = 'T2tt_dM-10to80_mStop-%s_mLSP-%s_%s-%s_HLT_%s'%(mStop,mLSP,menuName,menuVersion,PU)
#config.section_('General')
config.General.requestName = outputName 
config.General.transferOutputs = True
config.General.transferLogs = True
#config.General.workArea = 'crab_projects'

#config.section_('JobType')
#config.JobType.inputFiles = ['/afs/hephy.at/data/mzarucki02/gridpacks/%s'%gridpack]
config.JobType.pyCfgParams = ['outputName='+outputName]
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SoftTriggers_10X_DIGI_L1_DIGI2RAW_HLT_%s.py'%PU # Name of the CMSSW configuration file
config.JobType.outputFiles = ['%s.root'%outputName]
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 8000
#config.JobType.generator = 'lhe'

#config.section_('Data')
config.Data.inputDataset = '/SMS-T2tt_dM-10to80_mStop-{mStop}_mLSP-{mLSP}_privGridpack_GEN-SIM/mzarucki-SMS-T2tt_dM-10to80_mStop-{mStop}_mLSP-{mLSP}_privGridpack_GEN-SIM_RAWSIMoutput-{datasetHash}/USER'.format(mStop = mStop, mLSP = mLSP, datasetHash = datasetHashes['%s_%s'%(mStop, mLSP)])
config.Data.inputDBS = 'phys03'
#config.Data.userInputFiles = [x.strip() for x in open('inputFiles/inputFiles_T2tt_dM-10to80_mStop-%s_mLSP-%s_privGridpack_GEN-SIM.txt'%(mStop,mLSP)).readlines()] #NOTE: careful that the string is not too long
config.Data.outputDatasetTag = outputName # This string is used to construct the output dataset name
#config.Data.outputPrimaryDataset = outputName # This string determines the primary dataset of the newly-produced outputs.
config.Data.splitting = 'FileBased'
config.Data.publication = False
#config.Data.totalUnits = 300 #500000
config.Data.unitsPerJob = 1 #5000 #NOTE: if FileBased splitting, # files per job
config.Data.ignoreLocality = True # Set to True to allow the jobs to run at sites regardless of where the input dataset is hosted (this parameter has effect only when Data.inputDataset is used). The parameter Site.whitelist is mandatory and Site.blacklist can also be used and it is respected. This parameter is useful to allow the jobs to run on other sites when for example a dataset is hosted only on sites which are not running CRAB jobs. 

#config.section_('Site')
config.Site.storageSite = 'T2_AT_Vienna' #Where the output files will be transmitted to
config.Site.whitelist = ['T2_AT_Vienna','T2_CH*','T2_US*','T2_UK*','T2_IT*', 'T2_FR*', 'T2_PT*']
config.Site.blacklist = ['T2_EE_Estonia']

#config.section_("Debug")
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

#if __name__ == '__main__':
#    from CRABAPI.RawCommand import crabCommand
#    crabCommand('submit', config = config)
