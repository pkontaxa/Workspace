import ROOT
from Workspace.HEPHYPythonTools.helpers import getChain, getPlotFromChain, getYieldFromChain
from Workspace.RA4Analysis.cmgTuplesPostProcessed_v3 import *
cBkg  = getChain([soft_WJetsHTToLNu, soft_ttJetsCSA1450ns])
cSignal = getChain(soft_T5qqqqWW_Gl_1400_LSP_100_Chi_325)
#cSignal = getChain(soft_T6qqWW_Sq_950_LSP_300_Chi_350)
from math import pi, sqrt

import numpy as np
from scipy import optimize

cuts = [
  {'name':'jet1pt', 'var':'Jet_pt[1]',    'min': 40, 'max':320, 'step':40},\
  {'name':'njet', 'var':'nJet40a',        'min': 2, 'max':6, 'step':1},\
  {'name':'ht', 'var':'htJet40ja',        'min': 500, 'max':1200, 'step':100},\
  {'name':'met', 'var':'met',             'min':200, 'max':700, 'step':100  },\
  ]

prepreprefix = 'cutBasedOptimizer_'
presel = "singleMuonic&&nLooseSoftLeptons==1&&nTightSoftLeptons==1&&nTightHardLeptons==0&&nBJetMedium25==0"
dPhi = "acos((leptonPt+met_pt*cos(leptonPhi-met_phi))/sqrt(leptonPt**2+met**2+2*met*leptonPt*cos(leptonPhi-met_phi)))"
presel+= "&&"+dPhi+">1"

prefix = ''
results=[]
def loop_rec(sel, remainingCuts, appliedCuts=[]):
  if len(cuts)==0:
    fom = getFom(sel, relSysErr=0.20)
    print fom, appliedCuts
#    results+=[fom, appliedCuts]
  else:
    cut=cuts[0]
    for c in range(cut['min'], cut['max']+cut['step'],cut['step']): 
      s=sel+"&&"+cut['var']+">="+str(c)
      loop_rec(s, cuts[1:], appliedCuts+[[cut['var'], c]])


def getFom(cut, relSysErr=0.20, verbose=False):
      
  if verbose: print "Now at cut:",cut
  yieldS = getYieldFromChain(cSignal, cut, weight = "weight") 
  yieldB = getYieldFromChain(cBkg,    cut, weight = "weight")
  if yieldB<=0 or yieldS<=0:
    return -999.
  fom = yieldS/sqrt(yieldB + (relSysErr*yieldB)**2)       
  if verbose: 
    sigeff = getYieldFromChain(cSignal1200, cut, weight = "weight")/getYieldFromChain(cSignal1200, presel, weight = "weight")
    bkgeff = getYieldFromChain(cBkg, cut, weight = "weight")/getYieldFromChain(cBkg, presel, weight = "weight")
    print "Values", cutVals,"fom:",fom,'bkgeff',bkgeff,'sigeff',sigeff, 'yieldB',yieldB,'yieldS',yieldS
  return fom

loop_rec(presel, cuts) 
#
#
#goodRes = []
#c=0
##for met in range(250, 500, 50):
#for st in range(250, 500, 50):
#  for ht in range(500, 1100, 100):
##    for mT in np.linspace(150,350,5):
#    for dPhi in np.linspace(0.5,2.5,6):
##      vals = [met, ht, mT]
#      vals = [st, ht, dPhi]
#      fom = getFom(vals,relSysErr=0.20, verbose=True)
#      c+=1
##      if fom>1.5: 
#      goodRes.append([fom, vals])
#      print c, fom,  vals
#
#goodRes.sort()
#goodRes.reverse()
#print goodRes
#import pickle
#pickle.dump(goodRes, file('/data/schoef/T5FullStuff/cutBased/'+prefix+'_results.pkl','w'))
##pickle.dump(goodRes, file('/data/schoef/T5FullStuff/cutBased/st_ht_dPhi_6j_results.pkl','w'))
#
##
##Optimizing
##x0 = np.array([v['startVal'] for v in cuts])
## Using dMT
##  optThresh = optimize.anneal(lambda x:-getFom(x,relSysErr=0.05, lepCharge=-1,verbose=True), x0, T0=.001, learn_rate=0.7)
### anneal: Values [ 261.06062214   11.94453719  437.81238786] fom: 2.2452353601
##  optThresh = list(optThresh[0])
##  for relSysErr in [0., 0.05, 0.08, 0.15]:
##    print 'relSysErr',relSysErr,"charge:-",getFom(optThresh,relSysErr=relSysErr,lepCharge=-1),"charge:+",getFom(optThresh,relSysErr=relSysErr,lepCharge=+1),'comb',getFom(optThresh,relSysErr=relSysErr)
#
##  optThresh = optimize.fmin(lambda x:-getFom(x,relSysErr=0.05, lepCharge=-1,verbose=True), x0)
##  print "Found maximum",optThresh
##  for relSysErr in [0., 0.05, 0.08, 0.15]:
##    print 'relSysErr',relSysErr,"charge:-",getFom(optThresh,relSysErr=relSysErr,lepCharge=-1),"charge:+",getFom(optThresh,relSysErr=relSysErr,lepCharge=+1),'comb',getFom(optThresh,relSysErr=relSysErr)
###Optimization terminated successfully.
###         Current function value: -2.715423
###         Iterations: 32
###         Function evaluations: 108
###relSysErr 0.0 charge:- 2.73896828448 charge:+ 0.901746679739 comb 1.82387059297
###relSysErr 0.05 charge:- 2.71542309916 charge:+ 0.852811294992 comb 1.71161387649
###relSysErr 0.08 charge:- 2.67987530103 charge:+ 0.790209387858 comb 1.57159670352
###relSysErr 0.15 charge:- 2.54663488097 charge:+ 0.627896383924 comb 1.22430907069
