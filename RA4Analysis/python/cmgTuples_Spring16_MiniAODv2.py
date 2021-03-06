#pathDaniel  = "/data/dspitzbart//cmgTuples/RunIISpring16MiniAODv2/" 
pathDaniel  = "/afs/hephy.at/data/dspitzbart01/cmgTuples/RunIISpring16MiniAODv2/"
#pathEce     = "/afs/hephy.at/data/easilar01/cmgTuples/RunIISpring16MiniAODv2/"
#pathEce2    = "/data/easilar/cmgTuples/RunIISpring16MiniAODv2/"
pathEce     = "/afs/hephy.at/data/easilar01/Ra40b/cmgTuples/RunIISpring16MiniAODv2_v1/"
path = pathEce

TTJets_SingleLeptonFromT_full = {\
"name" : "TTJets_SingleLeptonFromT_full",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}

TTJets_SingleLeptonFromTbar_full = {\
"name" : "TTJets_SingleLeptonFromTbar_full",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName" : "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}

TTJets_DiLepton_full = {\
"name" : "TTJets_DiLepton",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName" : "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}

#TTJets_NLO = {\
#"name" : "TTJets_NLO",
#"chunkString":"cmgTuples_MC25ns_1l_13062016_TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v2",
#"dir": pathDaniel+"cmgTuples_MC25ns_1l_13062016_TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v2/",
#"dbsName" : "/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM",
#"skimAnalyzerDir":"",
#"rootFileLocation":"tree.root",
#"treeName":"tree",
#'isData':False,
##'postProcessingCut':"lheHTIncoming<600",
#}

TTJets_LO={\
"name" : "TTJets_LO",
"chunkString":"cmgTuples_MC25ns_1l_August_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}


TTJets_LO_HT600to800_25ns={\
"name" : "TTJets_LO_HT600to800",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName" : "/TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}

TTJets_LO_HT800to1200_25ns={\
"name" : "TTJets_LO_HT800to1200",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName" : "/TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}

TTJets_LO_HT1200to2500_25ns={\
"name" : "TTJets_LO_HT1200to2500",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName" : "/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False,
}

TTJets_LO_HT2500toInf_25ns={\
"name" : "TTJets_LO_HT2500toInf",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}


#DYJetsToLL_M_50_amcatnloFXFX_25ns={\
#"name" : "DYJetsToLL_M_50_amcatnloFXFX_25ns",
#"chunkString":"cmgTuples_MC25ns_1l_08062016_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns",
#"dir": pathDaniel+"cmgTuples_MC25ns_1l_08062016_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns/",
#'dbsName':'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
#"skimAnalyzerDir":"",
#"rootFileLocation":"tree.root",
#"treeName":"tree",
#'isData':False
#}
#
#DYJetsToLL_M_50_madgraphMLM_25ns={\
#"name" : "DYJetsToLL_M50_madgraphMLM",
#"chunkString":"cmgTuples_MC25ns_1l_08062016_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv1-PUFlat0to50_80X_mcRun2_asymptotic_2016_v3-v1_MC25ns",
#"dir": pathDaniel+"cmgTuples_MC25ns_1l_08062016_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv1-PUFlat0to50_80X_mcRun2_asymptotic_2016_v3-v1_MC25ns/",
#'dbsName':'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUFlat0to50_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM',
#"skimAnalyzerDir":"",
#"rootFileLocation":"tree.root",
#"treeName":"tree",
#'isData':False
#}

DYJetsToLL_M_50_HT_100to200_25ns={\
"name" : "DYJetsToLL_M_50_HT_100to200",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

DYJetsToLL_M_50_HT_200to400_25ns={\
"name" : "DYJetsToLL_M_50_HT_200to400",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

DYJetsToLL_M_50_HT_400to600_25ns={\
"name" : "DYJetsToLL_M_50_HT_400to600",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

DYJetsToLL_M_50_HT_600toInf_25ns={\
"name" : "DYJetsToLL_M_50_HT_600toInf",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}


WJetsToLNu_HT100to200={\
"name" : "WJetsToLNu_HT100to200",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WJetsToLNu_HT200to400={\
"name" : "WJetsToLNu_HT200to400",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WJetsToLNu_HT400to600={\
"name" : "WJetsToLNu_HT400to600",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}


WJetsToLNu_HT600to800={\
"name" : "WJetsToLNu_HT600to800",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WJetsToLNu_HT800to1200={\
"name" : "WJetsToLNu_HT800to1200",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WJetsToLNu_HT1200to2500={\
"name" : "WJetsToLNu_HT1200to2500",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WJetsToLNu_HT2500toInf={\
"name" : "WJetsToLNu_HT2500toInf",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
'dbsName':'/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

#WJetsToLNu={\
#"name" : "WJetsToLNu",
#"chunkString":"cmgTuples_MC25ns_1l_08062016_WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns",
#"dir": pathDaniel+"cmgTuples_MC25ns_1l_08062016_WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns/",
#'dbsName':'',
#"skimAnalyzerDir":"",
#"rootFileLocation":"tree.root",
#"treeName":"tree",
#'isData':False
#}


QCD_HT300to500_25ns={
"name" : "QCD_HT300to500",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName":"",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

QCD_HT500to700_25ns={
"name" : "QCD_HT500to700",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName":"",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

QCD_HT700to1000_25ns={
"name" : "QCD_HT700to1000",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName":"",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

QCD_HT1000to1500_25ns={
"name" : "QCD_HT1000to1500",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName":"",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

QCD_HT1500to2000_25ns={
"name" : "QCD_HT1500to2000",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName":"",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

QCD_HT2000toInf_25ns={
"name" : "QCD_HT2000toInf",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1_MC25ns_v1/",
"dbsName":"",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}


TTWJetsToLNu = {\
"name" : "TTWToLNu",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

TTWJetsToQQ = {\
"name" : "TTWToQQ",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

TTZToLLNuNu = {\
"name" : "TTZToLLNuNu",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

TTZToQQ = {\
"name" : "TTZToQQ",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/" ,
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

#TBar_tWch ={\
#"name" : "TBar_tWch",
#"chunkString":"TBar_tWch",
#"dir":  path ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}

#TBar_tWch_DS ={\
#"name" : "TBar_tWch_DS",
#"chunkString":"TBar_tWch_DS",
#"dir":  path ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}


#TToLeptons_sch ={\
#"name" : "TToLeptons_sch",
#"chunkString":"TToLeptons_sch",
#"dir":  path ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}

#TToLeptons_tch ={\
#"name" : "TToLeptons_tch_amcatnlo_full",
#"chunkString":"TToLeptons_tch_amcatnlo_full",
#"dir":  path ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}

ST_schannel_4f_leptonDecays = {\
"name":"ST_schannel_4f_leptonDecays",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ST_tchannel_4f_leptonDecays ={\
"name" : "ST_tchannel_4f_leptonDecays",
"chunkString":"cmgTuples_MC25ns_1l_September_ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1_MC25ns_v1",
"dir":  pathDaniel+"cmgTuples_MC25ns_1l_September_ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1_MC25ns_v1/" ,
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ST_tchannel_antitop_4f_leptonDecays ={\
"name" : "ST_tchannel_antitop_4f_leptonDecays_powheg",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/" ,
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ST_tchannel_top_4f_leptonDecays ={\
"name" : "ST_tchannel_top_4f_leptonDecays_powheg",
"chunkString":"cmgTuples_MC25ns_1l_August_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathDaniel+"cmgTuples_MC25ns_1l_August_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/" ,
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}


#TToLeptons_tch_amcatnlo_ext = {\
#"name" : "TToLeptons_tch_amcatnlo_ext",
#"chunkString":"TToLeptons_tch_amcatnlo_ext",
#"dir":  path ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}

ST_tW_antitop_5f_inclusiveDecays ={\
"name" : "ST_tW_antitop_5f_inclusiveDecays_powheg",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ST_tW_top_5f_inclusiveDecays ={\
"name" : "ST_tW_top_5f_inclusiveDecays_powheg",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

#T_tWch_DS ={\
#"name" : "T_tWch_DS",
#"chunkString":"T_tWch_DS",
#"dir":  path ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}

#DiBoson_WW = {\
#"name" : "DiBoson_WW",
#"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WW_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
#"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WW_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount/",
#"rootFileLocation":"tree.root",
#"treeName":"tree",
#'isData':False
#}

DiBoson_WW_noskim = {\
"name" : "DiBoson_WW",
"chunkString":"cmgTuples_MC25ns_September_noSkim_WW_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_noSkim",
"dir":  pathDaniel+"cmgTuples_MC25ns_September_noSkim_WW_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_noSkim/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

DiBoson_WW = {\
"name" : "DiBoson_WW",
"chunkString":"cmgTuples_MC25ns_1l_September_WW_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathDaniel+"cmgTuples_MC25ns_1l_September_WW_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

DiBoson_WZ = {\
"name" : "DiBoson_WZ",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_WZ_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_WZ_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

DiBoson_ZZ = {\
"name" : "DiBoson_ZZ",
"chunkString":"cmgTuples_MC25ns_v1_v3_1l_July_ZZ_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir":  pathEce+"cmgTuples_MC25ns_v1_v3_1l_July_ZZ_TuneCUETP8M1_13TeV-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WWTo2L2Nu = {\
"name" : "WWTo2L2Nu",
"chunkString":"cmgTuples_MC25ns_1l_August_WWTo2L2Nu_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_WWTo2L2Nu_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WWToLNuQQ = {\
"name" : "WWToLNuQQ",
"chunkString":"cmgTuples_MC25ns_1l_August_WWToLNuQQ_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_WWToLNuQQ_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WWToLNuQQ_noskim = {\
"name" : "WWToLNuQQ_powheg",
"chunkString":"cmgTuples_MC25ns_September_noSkim_WWToLNuQQ_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_noSkim",
"dir": pathDaniel+"cmgTuples_MC25ns_September_noSkim_WWToLNuQQ_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_noSkim/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WWToLNuQQ_withExt = {\
"name" : "WWToLNuQQ_extended",
"chunkString":"cmgTuples_MC25ns_September_noSkim_WWToLNuQQ_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_withExt",
"dir": pathDaniel+"cmgTuples_MC25ns_September_noSkim_WWToLNuQQ_13TeV-powheg_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_comb/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WWToLNuQQ_amc_noskim = {\
"name" : "WWToLNuQQ",
"chunkString":"cmgTuples_MC25ns_September_noSkim_WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_noSkim",
"dir": pathDaniel+"cmgTuples_MC25ns_September_noSkim_WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_noSkim/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WZTo1L1Nu2Q = {\
"name" : "WZTo1L1Nu2Q",
"chunkString":"cmgTuples_MC25ns_1l_August_WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WZTo1L3Nu = {\
"name" : "WZTo1L3Nu",
"chunkString":"cmgTuples_MC25ns_1l_August_WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

WZTo2L2Q = {\
"name" : "WZTo2L2Q",
"chunkString":"cmgTuples_MC25ns_1l_August_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ZZTo2L2Nu = {\
"name" : "ZZTo2L2Nu",
"chunkString":"cmgTuples_MC25ns_1l_August_ZZTo2L2Nu_13TeV_powheg_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_ZZTo2L2Nu_13TeV_powheg_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ZZTo2L2Q = {\
"name" : "ZZTo2L2Q",
"chunkString":"cmgTuples_MC25ns_1l_August_ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

ZZTo2Q2Nu = {\
"name" : "ZZTo2Q2Nu",
"chunkString":"cmgTuples_MC25ns_1l_August_ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1",
"dir": pathDaniel+"cmgTuples_MC25ns_1l_August_ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_MC25ns_v1/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount/",
"rootFileLocation":"tree.root",
"treeName":"tree",
'isData':False
}

####Signal Samples###
SMS_T5qqqqVV_TuneCUETP8M1 ={\
"name" : "SMS_T5qqqqVV_TuneCUETP8M1",
"chunkString":"SMS_T5qqqqVV_TuneCUETP8M1",
"dir": "/afs/hephy.at/data/easilar01/Ra40b/cmgTuples/SignalScan_nocut/signal_noCUT/",
"dbsName" : "",
"skimAnalyzerDir":"skimAnalyzerCount",
"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
"treeName":"tree",
'isData':False
}


#T5qqqqVV_mGluino_600To675_mLSP_1to550 ={\
#"name" : "T5qqqqVV_mGluino_600To675_mLSP_1to550",
#"chunkString":"T5qqqqVV_mGluino_600To675_mLSP_1to550",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_600To675_mLSP_1to550/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_700To775_mLSP_1To650 ={\
#"name" : "T5qqqqVV_mGluino_700To775_mLSP_1To650",
#"chunkString":"T5qqqqVV_mGluino_700To775_mLSP_1To650",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_700To775_mLSP_1To650/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_800To975_mLSP_1To850 ={\
#"name" : "T5qqqqVV_mGluino_800To975_mLSP_1To850",
#"chunkString":"T5qqqqVV_mGluino_800To975_mLSP_1To850",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_800To975_mLSP_1To850/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_1000To1075_mLSP_1To950 ={\
#"name" : "T5qqqqVV_mGluino_1000To1075_mLSP_1To950",
#"chunkString":"T5qqqqVV_mGluino_1000To1075_mLSP_1To950",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_1000To1075_mLSP_1To950" ,
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_1100To1175_mLSP_1to1050 ={\
#"name" : "T5qqqqVV_mGluino_1100To1175_mLSP_1to1050",
#"chunkString":"T5qqqqVV_mGluino_1100To1175_mLSP_1to1050",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_1100To1175_mLSP_1to1050/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_1200To1275_mLSP_1to1150 ={\
#"name" : "T5qqqqVV_mGluino_1200To1275_mLSP_1to1150",
#"chunkString":"T5qqqqVV_mGluino_1200To1275_mLSP_1to1150",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_1200To1275_mLSP_1to1150/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_1300To1375_mLSP_1to1250 ={\
#"name" : "T5qqqqVV_mGluino_1300To1375_mLSP_1to1250",
#"chunkString":"T5qqqqVV_mGluino_1300To1375_mLSP_1to1250",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_1300To1375_mLSP_1to1250/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_1400To1550_mLSP_1To1275 ={\
#"name" : "T5qqqqVV_mGluino_1400To1550_mLSP_1To1275",
#"chunkString":"T5qqqqVV_mGluino_1400To1550_mLSP_1To1275",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_1400To1550_mLSP_1To1275/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
#T5qqqqVV_mGluino_1600To1750_mLSP_1To950 ={\
#"name" : "T5qqqqVV_mGluino_1600To1750_mLSP_1To950",
#"chunkString":"T5qqqqVV_mGluino_1600To1750_mLSP_1To950",
#"dir": "/data/easilar/SignalScans2016/Chunks_T5qqqqVV_mGluino_1600To1750_mLSP_1To950/",
#"dbsName" : "",
#"skimAnalyzerDir":"skimAnalyzerCount",
#"rootFileLocation":"/treeProducerSusySingleLepton/tree.root",
#"treeName":"tree",
#'isData':False
#}
