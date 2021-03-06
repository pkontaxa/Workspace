path     = "/afs/hephy.at/data/easilar01/Moriond2017/cmgTuples/MC/"

bkg_samples = [
  'DYJetsToLL_M50_HT100to200',\
  'DYJetsToLL_M50_HT100to200_ext',\
  'DYJetsToLL_M50_HT200to400',\
  'DYJetsToLL_M50_HT200to400_ext',\
  'DYJetsToLL_M50_HT400to600',\
  'DYJetsToLL_M50_HT400to600_ext',\
  'DYJetsToLL_M50_HT600toInf',\
  'DYJetsToLL_M50_HT600toInf_ext',\
  'QCD_HT1000to1500',\
  'QCD_HT1500to2000',\
  'QCD_HT2000toInf',\
  'QCD_HT300to500',\
  'QCD_HT500to700',\
  'QCD_HT700to1000',\
  'ST_s_channel_4f_leptonDecays',\
  'ST_tW_antitop_5f_NoFullyHadronicDecays',\
  'ST_tW_top_5f_NoFullyHadronicDecays',\
  'ST_t_channel_antitop_4f_leptonDecays',\
  'ST_t_channel_top_4f_leptonDecays',\
  'TTJets_DiLepton',\
  'TTJets_LO_HT1200to2500_ext',\
  'TTJets_LO_HT2500toInf',\
  'TTJets_LO_HT600to800_ext',\
  'TTJets_LO_HT800to1200_ext',\
  'TTJets_SingleLeptonFromT',\
  'TTJets_SingleLeptonFromTbar',\
  'TTWToLNu',\
  'TTWToQQ',\
  'TTZToLLNuNu',\
  'TTZToQQ',\
  'WJetsToLNu_HT100to200',\
  'WJetsToLNu_HT100to200_ext',\
  'WJetsToLNu_HT1200to2500',\
  'WJetsToLNu_HT1200to2500_ext',\
  'WJetsToLNu_HT200to400',\
  'WJetsToLNu_HT200to400_ext',\
  'WJetsToLNu_HT2500toInf',\
  'WJetsToLNu_HT2500toInf_ext',\
  'WJetsToLNu_HT400to600',\
  'WJetsToLNu_HT400to600_ext',\
  'WJetsToLNu_HT600to800',\
  'WJetsToLNu_HT800to1200',\
  'WJetsToLNu_HT800to1200_ext',\
  'WWTo2L2Nu',\
  'WWToLNuQQ',\
  'WWToLNuQQ_ext',\
  'WZTo1L1Nu2Q',\
  'WZTo1L3Nu',\
  'WZTo2L2Q',\
  'ZZTo2L2Nu',\
  'ZZTo2Q2Nu',\
          ]

for bkg in bkg_samples:
  exec(bkg+'={"name":bkg,"chunkString":bkg,"dir":path,"dbsName":"","skimAnalyzerDir":"skimAnalyzerCount/",\
              "rootFileLocation":"treeProducerSusySingleLepton/tree.root",\
              "treeName":"tree","isData":False\
              }')

create_run_file = True
if create_run_file :
  for bkg in bkg_samples:
    print 'python cmgPostProcessing.py --overwrite --skim="HT350" --calcbtagweights  --samples='+bkg

SMS_T5qqqqVV_TuneCUETP8M1 ={\
"name" : "SMS_T5qqqqVV_TuneCUETP8M1",
"chunkString":"SMS_T5qqqqVV_TuneCUETP8M1",
"dir": "/afs/hephy.at/data/easilar01/Moriond2017/cmgTuples/signals/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount",
"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
"treeName":"tree",
'isData':False
}

SMS_T1tttt_TuneCUETP8M1 ={\
"name" : "SMS_T1tttt_TuneCUETP8M1",
"chunkString":"SMS_T1tttt_TuneCUETP8M1",
"dir": "/afs/hephy.at/data/easilar01/Moriond2017/cmgTuples/signals/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount",
"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
"treeName":"tree",
'isData':False
}

