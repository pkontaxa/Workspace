import ROOT
import os, sys, copy

ROOT.gROOT.LoadMacro('../../HEPHYPythonTools/scripts/root/tdrstyle.C')
ROOT.setTDRStyle()
from math import *
from array import array

from Workspace.HEPHYPythonTools.helpers import getVarValue, getChain, deltaPhi
from Workspace.RA4Analysis.cmgTuplesPostProcessed_v8_Phys14V3_HT400ST200 import *
from Workspace.RA4Analysis.helpers import *
from rCShelpers import *
from Workspace.RA4Analysis.signalRegions import *
from localInfo import username

binning=[30,0,1500]

prepresel = 'singleLeptonic&&nLooseHardLeptons==1&&nTightHardLeptons==1&&nLooseSoftPt10Leptons==0&&Jet_pt[1]>80'

bVar = 'nBJetMediumCSV30'

deltaPhiCut=1.
varstring='deltaPhi_Wl'
lepSel = 'hard'

targetLumi = 3. #fb^-1
sampleLumi = 4. #fb^-1
signalRegions = signalRegion3fb

scaleFactor = targetLumi/sampleLumi

cBkg = getChain([WJetsHTToLNu[lepSel], ttJets[lepSel], DY[lepSel], singleTop[lepSel], TTVH[lepSel]],histname='')
signal1 = getChain(T5qqqqWW_mGo1000_mCh800_mChi700[lepSel],histname='')
signal2 = getChain(T5qqqqWW_mGo1200_mCh1000_mChi800[lepSel],histname='')
signal3 = getChain(T5qqqqWW_mGo1500_mCh800_mChi100[lepSel],histname='')

yields = []
yieldsDict = {}

ROOT.TH1F().SetDefaultSumw2()

#Get the yields
for njb in signalRegions:
  yieldsDict[njb] = {}
  for stb in signalRegions[njb]:
    yieldsDict[njb][stb] = {}
    for htb in signalRegions[njb][stb]:
      
      twoBin=[0,signalRegions[njb][stb][htb]['deltaPhi'],3.2]
      bkgH = ROOT.TH1F('bkgH','',len(twoBin)-1, array('d', twoBin))
      sig1H = ROOT.TH1F('sig1H','',len(twoBin)-1, array('d', twoBin))
      sig2H = ROOT.TH1F('sig2H','',len(twoBin)-1, array('d', twoBin))
      sig3H = ROOT.TH1F('sig3H','',len(twoBin)-1, array('d', twoBin))
      
      name, cut = nameAndCut(stb, htb, njb, btb=(0,0), presel=prepresel, btagVar=bVar)
      
      cBkg.Draw(varstring+'>>bkgH','('+cut+')*weight')
      signal1.Draw(varstring+'>>sig1H','('+cut+')*weight')
      signal2.Draw(varstring+'>>sig2H','('+cut+')*weight')
      signal3.Draw(varstring+'>>sig3H','('+cut+')*weight')
      
      yBkg = bkgH.GetBinContent(2)*scaleFactor
      yBkgE = bkgH.GetBinError(2)*scaleFactor
      yS1 = sig1H.GetBinContent(2)*scaleFactor
      yS1E = sig1H.GetBinError(2)*scaleFactor
      yS2 = sig2H.GetBinContent(2)*scaleFactor
      yS2E = sig2H.GetBinError(2)*scaleFactor
      yS3 = sig3H.GetBinContent(2)*scaleFactor
      yS3E = sig3H.GetBinError(2)*scaleFactor
      
      yieldsDict[njb][stb][htb] = {'Jets':njb, 'ST':stb, 'HT':htb, 'Bkg':yBkg, 'BkgError':yBkgE, 'Model1':yS1, 'Model1Error': yS1E, 'Model2':yS2, 'Model2Error':yS2E, 'Model3':yS3, 'Model3Error':yS3E, 'deltaPhi':signalRegions[njb][stb][htb]['deltaPhi']}
      d = {'nJet':njb, 'HT':htb, 'ST':stb, 'B':yBkg, 'S1000':yS1, 'S1200':yS2, 'S1500':yS3, 'deltaPhi':signalRegions[njb][stb][htb]['deltaPhi']}
      print d
      yields.append(d)
      del sig1H, sig2H, sig3H, bkgH

path = '/data/'+username+'/lumi'+str(targetLumi)
yieldFile = open(path+'yields_pkl_final','w')
pickle.dump(yields,yieldFile)
yieldFile.close()


rowsNJet = {}
rowsSt = {}
for srNJet in sorted(signalRegions):
  rowsNJet[srNJet] = {}
  rowsSt[srNJet] = {}
  rows = 0
  for stb in sorted(signalRegions[srNJet]):
    rows += len(signalRegions[srNJet][stb])
    rowsSt[srNJet][stb] = {'n':len(signalRegions[srNJet][stb])}
  rowsNJet[srNJet] = {'nST':len(signalRegions[srNJet]), 'n':rows}

res = yieldsDict

print "Results"
print
print '\\begin{table}[ht]\\begin{center}\\resizebox{\\textwidth}{!}{\\begin{tabular}{|c|c|c|rrr|rrr|rrr|rrr|c|}\\hline'
print ' \\njet     & \ST $[$GeV$]$ & \HT $[$GeV$]$ & \multicolumn{3}{c|}{Background} & \multicolumn{3}{c|}{$T5q^4$ 1.0/0.8/0.7} & \multicolumn{3}{c|}{$T5q^4$ 1.2/1.0/0.8} & \multicolumn{3}{c|}{$T5q^4$ 1.5/0.8/0.1} & $\Delta\Phi$ cut\\\ \\hline'

secondLine = False
for srNJet in sorted(signalRegions):
  print '\\hline'
  if secondLine: print '\\hline'
  secondLine = True
  print '\multirow{'+str(rowsNJet[srNJet]['n'])+'}{*}{\\begin{sideways}$'+varBin(srNJet)+'$\end{sideways}}'
  for stb in sorted(signalRegions[srNJet]):
    print '&\multirow{'+str(rowsSt[srNJet][stb]['n'])+'}{*}{$'+varBin(stb)+'$}'
    first = True
    for htb in sorted(signalRegions[srNJet][stb]):
      if not first: print '&'
      first = False
      print '& $'+varBin(htb)+'$ &' +str(round(res[srNJet][stb][htb]['Bkg'],3)) +' & $\pm$  & ' + str(round(res[srNJet][stb][htb]['BkgError'],3)) \
           +' & '+str(round(res[srNJet][stb][htb]['Model1'],3)) +'& $\pm$ &' + str(round(res[srNJet][stb][htb]['Model1Error'],3)) \
           +' & '+str(round(res[srNJet][stb][htb]['Model2'],3)) +'& $\pm$ &' + str(round(res[srNJet][stb][htb]['Model2Error'],3)) \
           +' & '+str(round(res[srNJet][stb][htb]['Model3'],3)) +'& $\pm$ &' + str(round(res[srNJet][stb][htb]['Model3Error'],3)) \
           +' & '+str(res[srNJet][stb][htb]['deltaPhi']) + '\\\\'
      if htb[1] == -1 : print '\\cline{2-16}'
print '\\hline\end{tabular}}\end{center}\caption{Expected yield for '+str(targetLumi)+'$fb^{-1}$}\label{tab:expYield}\end{table}'


