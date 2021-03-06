""" Sample definition file for CMG post-processed ntuples using 2016 data and MC production at 25 ns for the degenerate stop analysis.
 
Each set of ntuples is produced with a git tag of HephySusySW.Workspace repository and and is saved in a directory:
  
   {path}/cmgTuples/{processingEra}/{processingTag}/{campaign}/{inc/soft/...}
   
    processingEra: postProcessed_mAODv2_v* (always starts with "postProcessed_")
    processingTag: 80X_postProcessing_v* (git tag of HephySusySW.Workspace)
    
    campaign:
        MC production campaign for MC samples  (e.g. RunIISpring16MiniAODv2, with _25ns added as additional identification)
        Energy, reconstruction tag, era for data (e.g. 13TeV_PromptReco_Collisions15_25ns, taken from JSON name file)
    
The corresponding py sample files are called: 
    RunIISpring16MiniAODv2_v*.py 
    Data2016_v*.py

"""

import copy
import os
import sys
import pickle

# most recent paths, can be replaced when initializing the cmgTuplesPostProcessed class
ppDir =  '/afs/hephy.at/data/mzarucki02/cmgTuples/postProcessed_mAODv2/8025_mAODv2_v10/80X_postProcessing_v0/analysisHephy_13TeV_2016_v2_6/step1'
mc_path     = ppDir + "/RunIISummer16MiniAODv2_v10"
data_path   = ppDir + "/Data2016_v10"
signal_path = mc_path

# Lumi that was used in the weight calculation of PostProcessing in pb-1
lumi_mc = 10000.

class cmgTuplesPostProcessed():

    def makeSample(self, sample):
        i = copy.deepcopy(sample)
        i['dir'] = os.path.join(i['dir'], 'inc')

        pold = copy.deepcopy(sample)
        pold['dir'] = os.path.join(pold['dir'], 'preselection', 'inc')

        p = copy.deepcopy(sample)
        p['dir'] = os.path.join(p['dir'], 'skimPreselect', 'inc')
        
        il = copy.deepcopy(sample)
        il['dir'] = os.path.join(il['dir'], 'incLep')

        ol = copy.deepcopy(sample)
        ol['dir'] = os.path.join(ol['dir'], 'oneLep')
        
        ol20 = copy.deepcopy(sample)
        ol20['dir'] = os.path.join(ol20['dir'], 'oneLep20')

        olg = copy.deepcopy(sample)
        olg['dir'] = os.path.join(olg['dir'], 'oneLepGood')
        
        olg20_isr100 = copy.deepcopy(sample)
        olg20_isr100['dir'] = os.path.join(olg20_isr100['dir'], 'oneLepGood20_ISR100')
        
        olg20 = copy.deepcopy(sample)
        olg20['dir'] = os.path.join(olg20['dir'], 'oneLepGood20')
        
        olg_ht800 = copy.deepcopy(sample)
        olg_ht800['dir'] = os.path.join(olg_ht800['dir'], 'oneLepGood_HT800')
        
        olg_ht100_met40_mt30 = copy.deepcopy(sample)
        olg_ht100_met40_mt30['dir'] = os.path.join(olg_ht100_met40_mt30['dir'], 'oneLepGood_HT100_MET40_MT30')
        
        oelg50_isr100_met40_mt30 = copy.deepcopy(sample)
        oelg50_isr100_met40_mt30['dir'] = os.path.join(oelg50_isr100_met40_mt30['dir'], 'oneElGood50_ISR100_MET40_MT30')
        
        met100 = copy.deepcopy(sample)
        met100['dir'] = os.path.join(met100['dir'], 'met100', 'incLep')
        
        met200 = copy.deepcopy(sample)
        met200['dir'] = os.path.join(met200['dir'], 'met200', 'incLep')

        pil = copy.deepcopy(sample)
        pil['dir'] = os.path.join(pil['dir'], 'skimPreselect', 'incLep')
        
        sf = copy.deepcopy(sample)
        sf['dir'] = os.path.join(sf['dir'], 'skimPreselect', 'filterInc')

        pif = copy.deepcopy(sample)
        pif['dir'] = os.path.join(pif['dir'], 'skimPreselect', 'filter')

        pifsrcr = copy.deepcopy(sample)
        pifsrcr['dir'] = os.path.join(pifsrcr['dir'], 'skimPreselect', 'filterMETHT250')

        pifsrcrjec = copy.deepcopy(sample)
        pifsrcrjec['dir'] = os.path.join(pifsrcrjec['dir'], 'skimPreselect', 'filterMETHT250JEC')

        pifjec = copy.deepcopy(sample)
        pifjec['dir'] = os.path.join(pifjec['dir'], 'skimPreselect', 'filterJEC')

        pifmll = copy.deepcopy(sample)
        pifmll['dir'] = os.path.join(pifmll['dir'], 'skimPreselect', 'filterMLL')


        #pifsrcr = copy.deepcopy(sample)
        #pifsrcr['dir'] = os.path.join(pifsrcr['dir'], 'skimPreselect', 'filterMETHT250_FS')

        pol = copy.deepcopy(sample)
        pol['dir'] = os.path.join(pol['dir'], 'skimPreselect', 'oneLepGood')

        badmu = copy.deepcopy(sample)
        badmu['dir'] = os.path.join(badmu['dir'], 'twoMu_MET100')

        lt120 = copy.deepcopy(sample)
        lt120['dir'] = os.path.join(lt120['dir'], 'LT120')

        return {
            'inc': i,
            #'preOneLep': pold,
            'skimPresel': p,
            'incLep': il,
            'oneLep': ol,
            'oneLep20': ol20,
            'oneLepGood': olg,
            'oneLepGood20': olg20,
            'oneLepGood20_ISR100': olg20_isr100,
            'oneLepGood_HT800': olg_ht800,
            'oneLepGood_HT100_MET40_MT30': olg_ht100_met40_mt30,
            'oneElGood50_ISR100_MET40_MT30': oelg50_isr100_met40_mt30,
            'met100': met100,
            'met200': met200,
            'preIncLep': pil,
            'preSF': sf,
            'preOneLep':  pol, 
            'lt120'    : lt120,
            'twoMu'    : badmu,
            'filter'   : pif,
            'filterMETHT250'   : pifsrcr,
            'filterMETHT250JEC'   : pifsrcrjec,
            'filterJEC'   : pifjec,
            'filterMLL'   : pifmll,
            }

    def getDataSample(self, name, bins):
        s = self.makeSample({
            "name" : name,
            "bins" : [bins] if type(bins)==type("") else bins,
            'dir' : self.data_path,
            })
        #
        return s

    def getSignalSample(self, signal, sampleId=0):
        return {
            "name" : signal,
            "chunkString": signal,
            'dir' : self.signal_path,
            'bins':[signal],
            'sampleId' : sampleId,
            }

    def __init__(self, mc_path=mc_path, signal_path=signal_path, data_path=data_path, lumi_mc=lumi_mc , ichepdata=False):

        self.mc_path = mc_path
        self.signal_path = signal_path
        self.data_path = data_path
        self.lumi = lumi_mc
        self.ichepdata = ichepdata

        print "MC DIR:      ", self.mc_path
        print "SIGNAL DIR:  ", self.signal_path
        print "DATA DIR:    ", self.data_path


        self.TT_pow = self.makeSample({
            "name" : "TT_pow",
            "bins" : [
                        'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                        'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1'
                #"TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",  # # this has a lhehtincoming cut of 600
                ],
            'dir' : self.mc_path,
            'sampleId' : 20,
            })
        
        self.TTJetsInc = self.makeSample({
            "name" : "TTJetsInc",
            "bins" : [
                #"TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",  # # this has a lhehtincoming cut of 600
                     ],
            'dir' : self.mc_path,
            'sampleId' : 20,
            })
        
        self.TTJets_LO = self.TTJetsInc
        
        self.TTJets_NLO = self.makeSample({
            "name" : "TTJets_NLO",
            "bins" : [
                      "TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1"
                ],
            'dir' : self.mc_path,
            'sampleId' : 20,
            })

        self.TTJetsHTLow = self.makeSample({
            "name" : "TTJetsHTLow",
            "bins" : [
                #"TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",  # # this has a lhehtincoming cut of 600
                ],
            'dir' : self.mc_path + "/lheHTlow/",
            'sampleId': 20,
            })

        self.TTJetsHTHigh = self.makeSample({
            "name" : "TTJetsHTHigh",
            "bins" : [
                #"TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1",
                ],
            'dir' : self.mc_path + "/lheHThigh/",
            'sampleId': 20,
            })

        self.TTJetsHTRest = self.makeSample({
            "name" : "TTJetsHT",
            "bins" : [
                #"TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1",
                #"TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1",
                #"TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",
                ],
            'dir' : self.mc_path,
            'sampleId': 20,
            })

        self.TTJets_SingleLepton = self.makeSample({
            "name" : "TTJets_SingleLepton",
            "bins" : [
                         'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1'
                ],
            'dir' : self.mc_path,
            'sampleId': 65,
            })

        self.TTJets_DiLepton = self.makeSample({
            "name" : "TTJets_DiLepton",
            "bins" : [
                         'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                ],
            'dir' : self.mc_path,
            'sampleId': 70,
            })

        self.TTX = self.makeSample({
            "name" : "TTX",
            "bins" : [
                        'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                        'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3',
                        'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1',
                        'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                        'TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                        'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                        'ttWJets_13TeV_madgraphMLM_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1', 
                        'ttZJets_13TeV_madgraphMLM_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                ],
            'dir' : self.mc_path,
            'sampleId': 90,
            })
        self.ttx = self.makeSample({
            "name" : "ttx",
            "bins" : [
                        'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                        'ttWJets_13TeV_madgraphMLM_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1', 
                        'ttZJets_13TeV_madgraphMLM_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                ],
            'dir' : self.mc_path,
            'sampleId': 90,
            })



        self.WJetsHT = self.makeSample({
            "name" : "WJetsHT",
            "bins" : [
                         'WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1',
                         'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1',
                         'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                    ],
            'dir' : self.mc_path,
            'sampleId' : 10,
            })

        self.WJetsToLNu_HT = self.WJetsHT

        self.WJetsPt = self.makeSample({
            "name" : "WJetsPt",
            "bins" : [
                         'WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1'
                    ],
            'dir' : self.mc_path,
            'sampleId' : 10,
            })

        self.WJets_NLO = self.makeSample({
        "name" : "WJets_NLO",
        "bins" : [
                    "WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1"
                ],
        'dir' : self.mc_path,
        'sampleId': 10,
        })

        self.WJets_LO = self.makeSample({
        "name" : "WJets_LO",
        "bins" : [
                    'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                ],
        'dir' : self.mc_path,
        'sampleId': 10,
        })


        self.QCD = self.makeSample({
            "name" : "QCD",
            "bins" :  [
                         'QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2',
                         'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',

                ],
            'dir' : self.mc_path,
            'sampleId' : 30,

        })


        self.QCDPT = self.makeSample({
        "name" : "QCDPT",
        "bins" :  [
#                     'QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
#                     'QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
                  ],
        'dir' : self.mc_path
        })




        self.ZJetsHT = self.makeSample({
            "name" : "ZJetsHT",
            "bins" :  [
                         'ZJetsToNuNu_HT-100To200_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'ZJetsToNuNu_HT-100To200_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'ZJetsToNuNu_HT-200To400_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'ZJetsToNuNu_HT-200To400_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'ZJetsToNuNu_HT-400To600_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'ZJetsToNuNu_HT-400To600_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'ZJetsToNuNu_HT-600To800_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'ZJetsToNuNu_HT-800To1200_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                      ] ,
            'dir' : self.mc_path ,
            'sampleId': 40,
            })


        self.DYJetsM5to50 = self.makeSample({
            "name" : "DYJetsM5to50",
            "bins" :  [
                         'DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1'
                      ] ,
            'dir' : self.mc_path
            })


        self.DYJetsM50HT = self.makeSample({
            "name" : "DYJetsM50HT",
            "bins" :  [
                         'DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                         'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2',
                         'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                         'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1'
                ] ,
            'dir' : self.mc_path,
            'sampleId': 50,
            })


        self.DYJetsToNuNu = self.makeSample({
        "name" : "DYJetsToNuNu",
        "bins" :  [
#                         'DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1',
                  ] ,
        'dir' : self.mc_path
        })

        self.TTX = self.makeSample({
        "name" : "TTX",
        "bins" :  [
                    'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                    'ttWJets_13TeV_madgraphMLM_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                    'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3',
                    'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                    'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1',
                    'ttZJets_13TeV_madgraphMLM_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                    'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                    'TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1'
                  ] ,
        'dir' : self.mc_path
        })


        self.VVInc = self.makeSample({
        "name" : "VVInc",
        "bins" :  [
                        "WW_TuneCUETP8M1_13TeV-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                  ] ,
        'dir' : self.mc_path
        })




        ### VV2 TEST
        self.ZZ = self.makeSample({
        "name" : "ZZ",
        "bins" :  [
                        "ZZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                  ] ,
        'dir' : self.mc_path
        })
        self.WW = self.makeSample({
        "name" : "WW",
        "bins" :  [
                        "WW_TuneCUETP8M1_13TeV-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                  ] ,
        'dir' : self.mc_path
        })
        self.WZ = self.makeSample({
        "name" : "WZ",
        "bins" :  [
                        "WZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                  ] ,
        'dir' : self.mc_path
        })

        self.VV2 = self.makeSample({
        "name" : "VV2",
        "bins" :  [
                        "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1",
                        "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],
        'dir' : self.mc_path
        })

        self.ZZ2 = self.makeSample({
        "name" : "ZZ2",
        "bins" :  [
                        "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo2L2Nu_13TeV_powheg_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],
        'dir' : self.mc_path
        })
        self.WZ2 = self.makeSample({
        "name" : "WZ2",
        "bins" :  [
                        "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3",
                        "WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        #"WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],

        'dir' : self.mc_path
        })
        self.WZ3 = self.makeSample({
        "name" : "WZ3",
        "bins" :  [
                        "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3",
                        "WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        #"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],

        'dir' : self.mc_path
        })
        self.WW2 = self.makeSample({
        "name" : "WW2",
        "bins" :  [
                        #"WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WWToLNuQQ_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1",
                        "WWTo2L2Nu_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WWToLNuQQ_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],
        'dir' : self.mc_path
        })
        self.WG = self.makeSample({
        "name" : "WG",
        "bins" :  [
                        "WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   #     "WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],
        'dir' : self.mc_path
        })



        self.VV = self.makeSample({
        "name" : "VV",
        "bins" :  [
                        "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo2L2Nu_13TeV_powheg_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",

                        "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3",
                        "WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        #"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", #prblm?

                        "WWToLNuQQ_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1",
                        "WWTo2L2Nu_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WWToLNuQQ_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",

                   ],
        'dir' : self.mc_path
        })



        self.VVNLO = self.makeSample({
        "name" : "VVNLO",
        "bins" :  [
                        "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        #"ZZTo2L2Nu_13TeV_powheg_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",

                        "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3",
                        "WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                       #"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", #prblm?

                        "WWToLNuQQ_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1",
                        #"WWTo2L2Nu_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                        "WWToLNuQQ_13TeV-powheg_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",

                        "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1",
                        "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1",
                   ],
        'dir' : self.mc_path
        })


        ### VV2 TEST

        self.ST_tch_Lep = self.makeSample({
        "name" : "SingleTop_tch",
        "bins" :  [
                  ] ,
        'dir' : self.mc_path
        })

        self.ST_tch = self.makeSample({
        "name" : "SingleTop_tch",
        "bins" :  [
                    "ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",
                    "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",
                  ] ,
        'dir' : self.mc_path
        })

        self.ST_wch = self.makeSample({
        "name" : "SingleTop_tW",
        "bins" :  [
                    "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1",
                    "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2",
                  ] ,
        'dir' : self.mc_path
        })

        self.ST = self.makeSample({
        "name" : "SingleTop",
        "bins" :  [
                    'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                    'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1',
                    'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1',
                    'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1'
                  ] ,
        'dir' : self.mc_path
        })

        ######################################################################################################
        #####################################                  ###############################################
        #####################################       DATA       ###############################################
        #####################################                  ###############################################
        ######################################################################################################


        if getattr(self, "ichepdata"):
            dataSamples = [
                            ["MET",      ["MET_Run2016B-PromptReco-v2"           , "MET_Run2016C-PromptReco-v2"              ,  "MET_Run2016D-PromptReco-v2"            ]    ],
                            ["SingleMu", ["SingleMuon_Run2016B-PromptReco-v2"    , "SingleMuon_Run2016C-PromptReco-v2"       ,  "SingleMuon_Run2016D-PromptReco-v2"     ]    ],
                            ["SingleEl", ["SingleElectron_Run2016B-PromptReco-v2", "SingleElectron_Run2016C-PromptReco-v2"   ,  "SingleElectron_Run2016D-PromptReco-v2" ]    ],
                ]

        else:
            dataSamples = [\


                ['MET', ["MET_Run2016B-03Feb2017_ver2-v2",  "MET_Run2016D-03Feb2017-v1" , "MET_Run2016F-03Feb2017-v1" , "MET_Run2016H-03Feb2017_ver2-v1",
                         "MET_Run2016C-03Feb2017-v1"     ,  "MET_Run2016E-03Feb2017-v1" , "MET_Run2016G-03Feb2017-v1" , "MET_Run2016H-03Feb2017_ver3-v1"]],

                ['SingleEl', ["SingleElectron_Run2016B-03Feb2017_ver2-v2",  "SingleElectron_Run2016D-03Feb2017-v1" , "SingleElectron_Run2016F-03Feb2017-v1" , "SingleElectron_Run2016H-03Feb2017_ver2-v1",
                              "SingleElectron_Run2016C-03Feb2017-v1"     ,  "SingleElectron_Run2016E-03Feb2017-v1" , "SingleElectron_Run2016G-03Feb2017-v1" , "SingleElectron_Run2016H-03Feb2017_ver3-v1"]],

                ['SingleMu', ["SingleMuon_Run2016B-03Feb2017_ver2-v2",  "SingleMuon_Run2016D-03Feb2017-v1" , "SingleMuon_Run2016F-03Feb2017-v1" , "SingleMuon_Run2016H-03Feb2017_ver2-v1",
                              "SingleMuon_Run2016C-03Feb2017-v1"     ,  "SingleMuon_Run2016E-03Feb2017-v1" , "SingleMuon_Run2016G-03Feb2017-v1" , "SingleMuon_Run2016H-03Feb2017_ver3-v1"]],

                ['JetHT', ["JetHT_Run2016B-03Feb2017_ver2-v2",  "JetHT_Run2016D-03Feb2017-v1" , "JetHT_Run2016F-03Feb2017-v1" , "JetHT_Run2016H-03Feb2017_ver2-v1",
                           "JetHT_Run2016C-03Feb2017-v1"     ,  "JetHT_Run2016E-03Feb2017-v1" , "JetHT_Run2016G-03Feb2017-v1" , "JetHT_Run2016H-03Feb2017_ver3-v1"]],
                




                ["MET_23Sep", ["MET_Run2016B-23Sep2016-v3",            "MET_Run2016C-23Sep2016-v1",            "MET_Run2016D-23Sep2016-v1",             "MET_Run2016E-23Sep2016-v1", 
                               "MET_Run2016F-23Sep2016-v1",            "MET_Run2016G-23Sep2016-v1",            "MET_Run2016H-PromptReco-v2",            "MET_Run2016H-PromptReco-v3"]], #NOTE: H PromptReco
                
                ["SingleMu_23Sep", ["SingleMuon_Run2016B-23Sep2016-v3",     "SingleMuon_Run2016C-23Sep2016-v1",     "SingleMuon_Run2016D-23Sep2016-v1",      "SingleMuon_Run2016E-23Sep2016-v1", 
                                    "SingleMuon_Run2016F-23Sep2016-v1",     "SingleMuon_Run2016G-23Sep2016-v1",     "SingleMuon_Run2016H-PromptReco-v2",     "SingleMuon_Run2016H-PromptReco-v3"]], #NOTE: H PromptReco
                
                ["SingleEl_23Sep", ["SingleElectron_Run2016B-23Sep2016-v3", "SingleElectron_Run2016C-23Sep2016-v1", "SingleElectron_Run2016D-23Sep2016-v1",  "SingleElectron_Run2016E-23Sep2016-v1", 
                                    "SingleElectron_Run2016F-23Sep2016-v1", "SingleElectron_Run2016G-23Sep2016-v1", "SingleElectron_Run2016H-PromptReco-v2", "SingleElectron_Run2016H-PromptReco-v3"]], #NOTE: H PromptReco
                
                ["JetHT_23Sep",    ["JetHT_Run2016B-23Sep2016-v3",          "JetHT_Run2016C-23Sep2016-v1",          "JetHT_Run2016D-23Sep2016-v1",           "JetHT_Run2016E-23Sep2016-v1", 
                                    "JetHT_Run2016F-23Sep2016-v1",          "JetHT_Run2016G-23Sep2016-v1",          "JetHT_Run2016H-PromptReco-v2",          "JetHT_Run2016H-PromptReco-v3"]], #NOTE: H PromptReco
            ]

        allData = []
        for data in dataSamples:
            sample = self.getDataSample(*data)
            setattr(self, data[0], sample)

        # signal samples

        allSignalStrings = [
            "T2DegStop_300_270",
            "T2DegStop_300_290_FastSim",
            "T2DegStop_300_270_FastSim",
            "T2DegStop_300_240_FastSim",
            "T2tt_300_270_FastSim",
            ]

        for s in allSignalStrings:
            sm = self.makeSample(self.getSignalSample(s))
            setattr(self, s, sm)


        signals_info = {
                             "SMS_T2tt_dM_10to80_genHT_160_genMET_80"                 :    { 'mass_template':  'SMS_T2tt_mStop_%s_mLSP_%s'              , 'pkl':'SMS_T2tt_dM_10to80_genHT_160_genMET_80_mass_dict.pkl'               ,  'scanId':1 , 'shortName':'t2ttold%s_%s' , 'niceName':   'T2tt_%s_%s_mWMin5'},
                             "SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1"   :    { 'mass_template':  'SMS_T2bW_X05_mStop_%s_mLSP_%s_mWMin0p1' , 'pkl':'SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1_mass_dict.pkl' ,  'scanId':2 , 'shortName':'t2bw%s_%s'    , 'niceName':   'T2bW_%s_%s'},
                             "SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1"       :    { 'mass_template':  'SMS_T2tt_mStop_%s_mLSP_%s_mWMin0p1'     , 'pkl':'SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1_mass_dict.pkl'     ,  'scanId':3 , 'shortName':'t2tt%s_%s'    , 'niceName':   'T2tt_%s_%s'},             
                             'SMS_C1C1_higgsino_genHT_160_genMET_80_3p'  :     {  'pkl': 'SMS_C1C1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',   'mass_template':'SMS_C1C1_mChipm1_%s_mLSP_%s'   , 'scanId':123  , 'shortName':'c1c1h%s_%s'   ,'niceName' :'C1C1_%s_%s'    }, 
                             'SMS_C1N1_higgsino_genHT_160_genMET_80_3p'  :     {  'pkl': 'SMS_C1N1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',   'mass_template':'SMS_C1N1_mChipm1_%s_mLSP_%s'   , 'scanId':123  , 'shortName':'c1n1h%s_%s'   ,'niceName' :'C1N1_%s_%s'    },       
                             'SMS_N2C1_higgsino_genHT_160_genMET_80_3p'  :     {  'pkl': 'SMS_N2C1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',   'mass_template':'SMS_N2C1_mChi02_%s_mChipm01_%s'    , 'scanId':123  , 'shortName':'n2c1h%s_%s'   ,'niceName' :'N2C1_%s_%s'    },       
                             'SMS_N2N1_higgsino_genHT_160_genMET_80_3p'  :     {  'pkl': 'SMS_N2N1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',   'mass_template':'SMS_N2N1_mChi02_%s_mLSP_%s'    , 'scanId':123  , 'shortName':'n2n1h%s_%s'   ,'niceName' :'N2N1_%s_%s'    },   
                             'SMS_TChiWZ_genHT_160_genMET_80_3p'         :     {  'pkl': 'SMS_TChiWZ_genHT_160_genMET_80_3p_mass_dict.pkl'       ,   'mass_template':'SMS_TChiWZ_Chipm2_%s_mLSP_%s'  , 'scanId':123  , 'shortName':'tchiwz%s_%s'   ,'niceName' :'TChiWZ_%s_%s'    },                                    
                             'MSSM_higgsino_genHT_160_genMET_80_3p'      :     {  'pkl': 'MSSM_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl'    ,   'mass_template':'MSSM_higgsino_mu_%s_M1_%s'     , 'scanId':123  , 'shortName':'hino%s_%s'   ,'niceName' :'Hino_%s_%s'    },                                    

                       }
  
        self.signals_info = signals_info

        for signal_name, signal_info in signals_info.items():
            mass_template            = signal_info['mass_template']
            scanId                   = signal_info['scanId']
            signal_mass_dict         = signal_info['pkl']
            mass_dict_pickle_file    = os.path.join(signal_path, signal_mass_dict)
            signal_info['mass_dict'] = mass_dict_pickle_file 

            if os.path.isfile(mass_dict_pickle_file):
                mass_dict_pickle = mass_dict_pickle_file
                mass_dict        = pickle.load(open(mass_dict_pickle,"r"))
            else:
                print "!!!!! WARNING !!!!! NO MASS DICT FOUND! %s"%mass_dict_pickle_file
                print "!!!!! If no other fix available, enable useProxyMassDict and set mass_dict_pickle by hand !"
                mass_dict_pickle = None
                mass_dict        = {}

                useProxyMassDict = False
                if useProxyMassDict:
                    mass_dict_pickle = "/afs/hephy.at/data/nrad01/cmgTuples/postProcessed_mAODv2/8012_mAODv2_v3/80X_postProcessing_v10/analysisHephy_13TeV_2016_v0/step1/RunIISpring16MiniAODv2_v3/SMS_T2tt_dM_10to80_genHT_160_genMET_80_mass_dict.pkl"
                    mass_dict        = pickle.load(open(mass_dict_pickle,"r"))
                    print "!!!!!!!!!!! DOUBLE WARNING! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! USING PROXY MASS PICKLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
             
            mass_scan = {}

            for mstop in mass_dict:
                for mlsp in mass_dict[mstop]:
                    #mass_point = "SMS_T2tt_mStop_%s_mLSP_%s" % (mstop, mlsp)
                    mass_point = mass_template % (mstop, mlsp)
                    mass_scan[mass_point] = {
                        "name" : mass_point.replace(".","p"),
                        "bins": [mass_point.replace(".","p")],
                        'dir' : self.signal_path,
                        'sampleId': "%s%s%s" % (scanId, mstop, mlsp)
                        }


            for sig in mass_scan:
                sm = self.makeSample(mass_scan[sig])
                setattr(self, sig.replace(".","p"), sm)

if __name__=="__main__":
    cmgPP = cmgTuplesPostProcessed(mc_path, signal_path, data_path)
