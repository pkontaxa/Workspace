import ROOT
import os, sys, copy
import pickle, operator

from math import *
from array import array
from Workspace.HEPHYPythonTools.helpers import *
from Workspace.RA4Analysis.helpers import *
from Workspace.RA4Analysis.signalRegions import *
from Workspace.RA4Analysis.general_config import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--singleGluinoMassPoint", dest="singleMP", default=False, action="store_true", help="small set")
parser.add_option("--small", dest="smallSR", default=False, action="store_true", help="small set of signalRegions")
parser.add_option("--mgl", dest="gluinoMass", default=1200, action="store", help="Set gluino mass")
parser.add_option("--useISR", dest="useISR", default=False, action="store_true", help="Use ISR reweighting")


(options, args) = parser.parse_args()

#small = True
#smallSR = False


useISR = options.useISR

print useISR

signalRegions = signalRegions_Moriond2017
signal = SMS_T5qqqqVV_TuneCUETP8M1

#presel = "!isData&&singleLeptonic&&nLooseHardLeptons==1&&nTightHardLeptons==1&&nLooseSoftLeptons==0&&Jet_pt[1]>80&&st>250&&nJet30>2&&htJet30j>500&&flag_crazy_jets"
presel = "singleLeptonic&&nLooseHardLeptons==1&&nTightHardLeptons==1&&nLooseSoftLeptons==0&&Jet_pt[1]>80&&iso_Veto&&flag_crazy_jets"
presel_mod = presel
deltaPhiGenMet = "acos((leptonPt+met_genPt*cos(leptonPhi-met_genPhi))/sqrt(leptonPt**2+met_genPt**2+2*met_genPt*leptonPt*cos(leptonPhi-met_genPhi)))"

WSB   = (3,4)
TTSB  = (4,5)

#lumi = 12.88


use_btagWeights = False
weight = weight_str_signal_plot
nbtag = (0,0)

if useISR: weight+='*weight_ISR_new'

weight_Central_0b     = weight+'*weightBTag0_SF'
weight_Central_1b     = weight+'*weightBTag1p_SF'


#pickleDir = '/afs/hephy.at/data/easilar01/Ra40b/pickleDir/T5qqqqWW_mass_nEvents_xsec_pkl'
#mass_dict = pickle.load(file(pickleDir))

singleMP = options.singleMP
smallSR = options.smallSR
smallSetMGL = int(options.gluinoMass)
mGl = smallSetMGL
#if singleMP: mass_dict = {smallSetMGL:mass_dict[smallSetMGL]}
  

if smallSR:
  signalRegions = {(5,5): {(350, 450): {(500, -1): {'deltaPhi': 1.}},
                            (450, -1):  {(500, -1): {'deltaPhi': .75}}},
                    (6,-1):{(350, 450): {(500, -1): {'deltaPhi': 1.}},
                            (450, -1):  {(500, -1): {'deltaPhi': .75}}}
                   }



bins = ['MB_CR', 'MB_SR', 'SB_W_CR', 'SB_W_SR', 'SB_TT_CR', 'SB_TT_SR']


unc = {}
for srNJet in sorted(signalRegions):
  unc[srNJet] = {}
  for stb in sorted(signalRegions[srNJet]):
    unc[srNJet][stb] = {}
    for htb in sorted(signalRegions[srNJet][stb]):
      unc[srNJet][stb][htb] = {}
      unc[srNJet][stb][htb]["signals"] = {}
      dPhi = signalRegions[srNJet][stb][htb]['deltaPhi']

      print
      print '#################################################'
      print '## Uncertainties for SR',str(srNJet),str(stb),str(htb)
      print '## Using a dPhi cut value of',str(dPhi)
      print '#################################################'
      print

      nameMB, cutMB     = nameAndCut(stb, htb, srNJet, btb=None, presel = presel)
      nameWSB, cutWSB   = nameAndCut(stb, htb, WSB, btb=None, presel = presel)
      nameTTSB, cutTTSB = nameAndCut(stb, htb, TTSB, btb=None, presel = presel)
      
      nameMB, cutMBgen     = nameAndCut(stb, htb, srNJet, btb=None, presel = presel_mod, stVar = '(leptonPt+met_genPt)')
      nameWSB, cutWSBgen   = nameAndCut(stb, htb, WSB, btb=None, presel = presel_mod, stVar = '(leptonPt+met_genPt)')
      nameTTSB, cutTTSBgen = nameAndCut(stb, htb, TTSB, btb=None, presel = presel_mod, stVar = '(leptonPt+met_genPt)')

      #loop over signal points
      ISRweightDictPath = '/data/easilar/Results2016/ICHEP/signal_Spring16_noCut/mglu'+str(mGl)+'Signals_12p88_isr_scale_updated_fullSRs_pkl'
      if useISR: ISRweightDict = pickle.load(file(ISRweightDictPath))
      unc[srNJet][stb][htb]["signals"][mGl] = {}
      print
      print 'Gluino mass', mGl
      #mLSPs = [100]
      for mLSP in signal[mGl].keys() :
        unc[srNJet][stb][htb]["signals"][mGl][mLSP] = {}
        if useISR: ISRweight = ISRweightDict[srNJet][stb][htb]['signals'][mGl][mLSP]['scale_weight_ISR_new']
        else: ISRweight = 1
        print 'LSP mass', mLSP

        c = getChain(signal[mGl][mLSP],histname='')
        
        uncBin = {}
        # get central yields
        d = [
        {'name':'MB', 'cut':cutMB, 'dPhiVar':'deltaPhi_Wl', 'weight':weight_Central_0b},
        {'name':'SB_W', 'cut':cutWSB, 'dPhiVar':'deltaPhi_Wl', 'weight':weight_Central_0b},
        {'name':'SB_TT', 'cut':cutTTSB, 'dPhiVar':'deltaPhi_Wl', 'weight':weight_Central_1b},

        {'name':'gen_MB', 'cut':cutMBgen, 'dPhiVar':deltaPhiGenMet, 'weight':weight_Central_0b},
        {'name':'gen_SB_W', 'cut':cutWSBgen, 'dPhiVar':deltaPhiGenMet, 'weight':weight_Central_0b},
        {'name':'gen_SB_TT', 'cut':cutTTSBgen, 'dPhiVar':deltaPhiGenMet, 'weight':weight_Central_1b},
        ]
        for job in d:
          h = getPlotFromChain(c, job['dPhiVar'], [0,dPhi,3.2], cutString = job['cut'], weight = job['weight'], binningIsExplicit=True)
          uncBin['yield_'+job['name']+'_CR'] = h.GetBinContent(1)*ISRweight
          uncBin['err_'+job['name']+'_CR'] = h.GetBinError(1)*ISRweight
          uncBin['yield_'+job['name']+'_SR'] = h.GetBinContent(2)*ISRweight
          uncBin['err_'+job['name']+'_SR'] = h.GetBinError(2)*ISRweight
          del h
        #print d[0]
        #print uncBin['yield_MB_SR']
        
        for b in bins:
          uncBin['mod_yield_'+b] = (uncBin['yield_gen_'+b] + uncBin['yield_'+b])/2.
          uncBin['mod_err_'+b]   = abs(uncBin['yield_gen_'+b] - uncBin['yield_'+b])/2.
        
        unc[srNJet][stb][htb]["signals"][mGl][mLSP] = uncBin
        del c
      if useISR: del ISRweightDict


picklePath = '/afs/hephy.at/user/e/easilar/www/Moriond2017/sys/genMET/'
pickleName = 'gen_met_study_'
if useISR: pickleName += 'ISR_'

if singleMP: pickleName+='mgl'+str(smallSetMGL)
else: pickleName+='mgl_all'

pickle.dump(unc, file(picklePath+pickleName+'_pkl','w'))
print
print 'saved results in',picklePath+pickleName+'_pkl'

