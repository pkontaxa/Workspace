# ISRtagEff.py
# Mateusz Zarucki 2017

import ROOT
import os, sys
import argparse
import copy
import Workspace.DegenerateStopAnalysis.toolsMateusz.ROOToptions
from Workspace.DegenerateStopAnalysis.toolsMateusz.drawFunctions import *
from Workspace.DegenerateStopAnalysis.toolsMateusz.pythonFunctions import *
from Workspace.DegenerateStopAnalysis.tools.degTools import CutClass, Plots, getPlots, drawPlots, Yields, setEventListToChains, setup_style, makeSimpleLatexTable, makeDir, makeLegend
from Workspace.DegenerateStopAnalysis.tools.degCuts2 import Cuts, CutsWeights
from Workspace.DegenerateStopAnalysis.samples.baselineSamplesInfo import cutWeightOptions, triggers, filters, lumis
#from Workspace.DegenerateStopAnalysis.tools.colors import colors
from Workspace.DegenerateStopAnalysis.tools.getSamples import getSamples
from Workspace.DegenerateStopAnalysis.samples.cmgTuples_postProcessed.cmgTuplesPostProcessed_mAODv2_Summer16 import cmgTuplesPostProcessed
#from Workspace.DegenerateStopAnalysis.tools.mvaTools import getMVATrees
from Workspace.HEPHYPythonTools import u_float
from pprint import pprint
from array import array
from math import pi, sqrt

#Sets TDR style
setup_style()

#Input options
parser = argparse.ArgumentParser(description = "Input options")
parser.add_argument("--sample", dest = "sample", help = "Sample", type = str, default = "tt_1l")
parser.add_argument("--getData", dest = "getData",  help = "Get data samples", type = int, default = 0)
parser.add_argument("--getSignal", dest = "getSignal",  help = "Get signal samples", type = int, default = 0)
parser.add_argument("--genISR", dest = "genISR",  help = "Generated ISR", type = str, default = "")
parser.add_argument("--doControlPlots", dest = "doControlPlots",  help = "Do control plots", type = int, default = 1)
parser.add_argument("--region", dest = "region",  help = "Region", type = str, default = "none")
parser.add_argument("--logy", dest = "logy",  help = "Toggle logy", type = int, default = 1)
parser.add_argument("--save", dest = "save",  help = "Toggle save", type = int, default = 1)
parser.add_argument("--verbose", dest = "verbose",  help = "Verbosity switch", type = int, default = 0)
parser.add_argument("-b", dest = "batch",  help = "Batch mode", action = "store_true", default = False)
args = parser.parse_args()
if not len(sys.argv) > 1:
   print makeLine()
   print "No arguments given. Using default settings."
   print makeLine()
   #exit()

#Arguments
sample =         args.sample
getData =        args.getData
getSignal =      args.getSignal
genISR =         args.genISR
doControlPlots = args.doControlPlots
region =         args.region
logy =           args.logy
save =           args.save
verbose =        args.verbose

if verbose:
   print makeDoubleLine()
   print "Running ISR script"
   print makeDoubleLine()

#Samples
cmgPP = cmgTuplesPostProcessed()

samplesList = [sample]
#samplesList = ["s30_FullSim", "s20_FullSim", "s50_FullSim"]
#samplesList = ["st", "vv", "qcd", "dy5to50", "dy", "z", "tt_2l", "tt_1l", "w"]

if getData: 
   data = "dblind"
   samplesList.append(data)

samples = getSamples(cmgPP = cmgPP, skim = 'met200', sampleList = samplesList, scan = getSignal, useHT = True, getData = getData, def_weights = [])
#samples = getSamples(cmgPP = cmgPP, skim = 'preIncLep', sampleList = samplesList, scan = getSignal, useHT = True, getData = getData, def_weights = [])

#deltaMhists = {'T2tt':{'lt20':{10:[], 20:[], 30:[], 40:[], 50:[], 60:[], 70:[], 80:[]},
#                       'gt20':{10:[], 20:[], 30:[], 40:[], 50:[], 60:[], 70:[], 80:[]}}}
#
#for x in ratiosPkl['hists']:
#   for y in ratiosPkl['hists'][x]:
#      deltaMhists[y.split('-')[0]][x][int(y.split('-')[1])-int(y.split('-')[2])].append(ratiosPkl['hists'][x][y])

if verbose:
   print makeLine()
   print "Using samples:"
   newLine()
   for s in samplesList:
      if s: print samples[s].name,":",s
      else: 
         print "!!! Sample " + sample + " unavailable."
         sys.exit()

#Save
if save: #web address: http://www.hephy.at/user/mzarucki/plots
   tag = samples[samples.keys()[0]].dir.split('/')[7] + "/" + samples[samples.keys()[0]].dir.split('/')[8]
   savedir1 = "/afs/hephy.at/user/m/mzarucki/www/plots/%s/ISR/tagEff"%tag
   
   suff = "_" + sample 

   if genISR:
      savedir1 += "/GenJets"
      suff += "_GenJets"
   else:   
      savedir1 += "/RecoJets"
      suff += "_RecoJets"
   
   suff += "_" + region
   
   savedir1 += "/" + region
   
   savedir2 = savedir1 + "/controlPlots"

   makeDir("%s/root"%savedir1)
   makeDir("%s/pdf"%savedir1)
   makeDir("%s/root"%savedir2)
   makeDir("%s/pdf"%savedir2)

if 'all' in sample:

   from Workspace.DegenerateStopAnalysis.tools.Sample import Sample, Samples

   sampleDict = {}   

   allSignal = ROOT.TChain("Events", "Events")
   for s in samples.sigList():
      if 't2tt' in s and not 't2ttold' in s:
         allSignal.Add(samples[s].tree)

   sampleDict.update({
      'allSignal':{'name':'allSignal', 'sample':{'dir':samples[samples.keys()[0]].dir}, 'tree':allSignal, 'color':ROOT.kRed, 'isSignal':3 , 'isData':0, 'lumi':lumis["MC_lumi"]},
   })

   sampleDict2 = {}
   sampleDict2['allSignal'] = Sample(**sampleDict['allSignal'])
   samples = Samples(**sampleDict2)

cuts_weights = CutsWeights(samples, cutWeightOptions)

# N-1 
reg = cuts_weights.cuts.removeCut(region, 'ISR100')
if reg != region: isrPtInc = '_no_ISR100'
else: isrPtInc = ''

var = {}

if genISR:
   trueISR = 'trueGenISR'
   var['pt'] = 'GenIsrPt'
   if doControlPlots:
      var['recoil'] = 'GenISR_Recoil'
      var['dRmin'] =  'GenISR_dRmin'
      var['pdgId'] =  'GenISR_pdgId'
else:
   trueISR = 'trueISR'
   var['pt'] = 'isrPt'
   if doControlPlots:
      var['recoil'] =         'ISR_recoil'
      var['dRmin'] =          'ISR_dRmin'
      var['pdgId'] =          'ISR_pdgId'
      var['mcFlavour'] =      'ISR_mcFlavour'
      var['partonFlavour'] =  'ISR_partonFlavour'
      var['mcMatchFlav'] =    'ISR_mcMatchFlav'
      var['partonId'] =       'ISR_partonId'
      var['partonMotherId'] = 'ISR_partonMotherId'
      var['qgl'] =            'ISR_qgl'

cuts_weights.cuts.addCut(region + isrPtInc, "ISRinEvt")
isrInEvt = "_plus_ISRinEvt"

# True ISR
cuts_weights.cuts.addCut(region + isrPtInc + isrInEvt, trueISR)
trueISRcutName = '_plus_' + trueISR

if not genISR:
   cuts_weights.cuts.addCut(region + isrPtInc + isrInEvt, "ISRfromGluon")

cuts_weights.cuts._update(reset = False)
cuts_weights._update()

variables = {}
for v in var:
   variables[v] = cuts_weights.cuts.vars_dict_format[var[v]]

if doControlPlots:   
   variables['ht'] = 'ht'

plotList = [var['pt']]
if doControlPlots:
   plotList.append(var['recoil'])
   plotList.append(var['dRmin'])
   plotList.append(var['pdgId'])
   #plotList.append(var['ht']) 
   if not genISR:
      plotList.extend([var['mcFlavour'], var['partonFlavour'], var['mcMatchFlav'], var['partonId'], var['partonMotherId']])#, var['qgl']])

plotDict = {
   var['pt']:       {'var':variables['pt'],       "bins":[50,0,1000],   "nMinus1":"", "decor":{"title":"isrPt",    "x":"%s ISR Jet p_{T}"%genISR,       "y":"Events", 'log':[0,logy,0]}},
   }
if doControlPlots:
   plotDict.update({
   var['recoil']:   {'var':variables['recoil'],   "bins":[40,0,8],       "nMinus1":"", "decor":{"title":"Recoil",    "x":"%s ISR Jet p_{T}/MET"%genISR,   "y":"Events", 'log':[0,logy,0]}},
   var['dRmin']:    {'var':variables['dRmin'],    "bins":[50,0,1],       "nMinus1":"", "decor":{"title":"dRminIsr",  "x":"dRmin(GenPart, %s ISR)"%genISR, "y":"Events", 'log':[0,logy,0]}},
   var['pdgId']:    {'var':variables['pdgId'],    "bins":[35,-10,25],    "nMinus1":"", "decor":{"title":"ISR pdgId", "x":"ISR pdgId",                     "y":"Events", 'log':[0,logy,0]}},
   var['ht']:       {'var':variables['ht'],       "bins":[40,200,1000],  "nMinus1":"", "decor":{"title":"HT",        "x":"H_{T} [GeV]",                   "y":"Events", 'log':[0,logy,0]}},
   })

   if not genISR:
      plotDict.update({
      var['mcFlavour']:      {'var':variables['mcFlavour'],      "bins":[35,-10,25], "nMinus1":"", "decor":{"title":"ISR mcFlavour",      "x":"ISR mcFlavour",      "y":"Events", 'log':[0,logy,0]}},
      var['partonFlavour']:  {'var':variables['partonFlavour'],  "bins":[35,-10,25], "nMinus1":"", "decor":{"title":"ISR partonFlavour",  "x":"ISR partonFlavour",  "y":"Events", 'log':[0,logy,0]}},
      var['mcMatchFlav']:    {'var':variables['mcMatchFlav'],    "bins":[35,-10,25], "nMinus1":"", "decor":{"title":"ISR mcMatchFlav",    "x":"ISR mcMatchFlav",    "y":"Events", 'log':[0,logy,0]}},
      var['partonId']:       {'var':variables['partonId'],       "bins":[35,-10,25], "nMinus1":"", "decor":{"title":"ISR partonId",       "x":"ISR partonId",       "y":"Events", 'log':[0,logy,0]}},
      var['partonMotherId']: {'var':variables['partonMotherId'], "bins":[35,-10,25], "nMinus1":"", "decor":{"title":"ISR partonMotherId", "x":"ISR partonMotherId", "y":"Events", 'log':[0,logy,0]}},
      var['qgl']:            {'var':variables['qgl'],            "bins":[25,0,1],    "nMinus1":"", "decor":{"title":"ISR QG Likelihood",  "x":"ISR QG Likelihood",  "y":"Events", 'log':[0,logy,0]}},
      })
plotsDict = Plots(**plotDict)

plots0_ =  getPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc], samplesList, plotList = plotList, addOverFlowBin='both')
plots0 =  drawPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc], samplesList, plotList = plotList, plotLimits = [1, 100], denoms = [sample], noms = [sample], fom = None, fomLimits = [0,1.8], plotMin = 1, normalize = False, save = False, leg = False)

plots1_ =  getPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc + isrInEvt], samplesList, plotList = plotList, addOverFlowBin='both')
plots1 =  drawPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc + isrInEvt], samplesList, plotList = plotList, plotLimits = [1, 100], denoms = [sample], noms = [sample], fom = None, fomLimits = [0,1.8], plotMin = 1, normalize = False, save = False, leg = False)

plots2_ =  getPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc + isrInEvt + trueISRcutName], samplesList, plotList = plotList, addOverFlowBin='both')
plots2 =  drawPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc + isrInEvt + trueISRcutName], samplesList, plotList = plotList, plotLimits = [1, 100], denoms = [sample], noms = [sample], fom = None, fomLimits = [0,1.8], plotMin = 1, normalize = False, save = False, leg = False)

if not genISR:
   plots3_ =  getPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc + isrInEvt + '_plus_ISRfromGluon'], samplesList, plotList = plotList, addOverFlowBin='both')
   plots3 =  drawPlots(samples, plotsDict, [cuts_weights.cuts, region + isrPtInc + isrInEvt + '_plus_ISRfromGluon'], samplesList, plotList = plotList, plotLimits = [1, 100], denoms = [sample], noms = [sample], fom = None, fomLimits = [0,1.8], plotMin = 1, normalize = False, save = False, leg = False)

latex = copy.deepcopy(plots1['latexText'])
#leg = copy.deepcopy(plots1['legs'])
#if len(leg) > 2:
#   leg = [leg[0], leg[1]]

canvs = {}
hists = {}
ratioPlot = {}
for v in var:
   hists[v] = {}

   hists[v]['total'] = plots0['hists'][sample][var[v]].Clone()
   hists[v]['ISR'] =   plots1['hists'][sample][var[v]].Clone()
   hists[v]['true'] =  plots2['hists'][sample][var[v]].Clone()
  
   if not genISR: 
      hists[v]['ISRfromGluon'] = plots3['hists'][sample][var[v]].Clone()

      NISR = hists[v]['ISR'].GetEntries()
      NISRfromGluon = hists[v]['ISRfromGluon'].GetEntries()
      print "# evts with ISR: ", NISR 
      print "# evts with ISR from gluon: ", NISRfromGluon 
      print "# evts with ISR from quarks: ", NISR - NISRfromGluon 
 
   hists[v]['total'].SetFillColor(ROOT.kAzure)
   hists[v]['ISR'].SetFillColor(ROOT.kMagenta+2)
   hists[v]['true'].SetFillColor(ROOT.kRed)
   hists[v]['total'].SetLineColor(1)
   hists[v]['ISR'].SetLineColor(1)
   hists[v]['true'].SetLineColor(1)
   hists[v]['total'].SetLineWidth(1)
   hists[v]['ISR'].SetLineWidth(1)
   hists[v]['true'].SetLineWidth(1)
   
   leg1 = [makeLegend2()]
   leg1[-1].AddEntry(hists[v]['total'], sample, "F")
   leg1[-1].AddEntry(hists[v]['ISR'], sample + ' (ISR Present)', "F")
   leg1[-1].AddEntry(hists[v]['true'], sample + ' (True ISR)', "F")
   
   #leg2 = [makeLegend2()]
   #leg2[-1].AddEntry(hists['ISR'], sample + ' (ISR Present)', "F")
   #leg2[-1].AddEntry(hists['true'], sample + ' (True ISR)', "F")
   
   canvs[v] = drawPlot(hists[v]['total'], legend = leg1, decor = plotsDict[var[v]]['decor'], latexText = latex, ratio = (hists[v]['ISR'], hists[v]['total']), ratioLimits = [0, 1], ratioTitle = "#splitline{Black: % ISR}{Green: True ISR}", unity = True)
   hists[v]['ISR'].Draw("histsame")
   
   #canvs2 = drawPlot(hists['ISR'], legend = leg2, decor = plotsDict[var_pt]['decor'], latexText = latex, ratio = (hists['true'], hists['ISR']), ratioLimits = [0, 1], ratioTitle = "% True ISR", unity = True)
   hists[v]['true'].Draw("histsame")
   
   # Superimposed ratio = True ISR 
   canvs[v]['canvs'][2].cd()
   num = hists[v]['true'].Clone() 
   den = hists[v]['ISR'].Clone()
   num.Sumw2()
   den.Sumw2()
   ratioPlot[v] = num
   ratioPlot[v].Divide(den)
   ratioPlot[v].SetFillColor(ROOT.kBlue-8)
   ratioPlot[v].SetFillStyle(3003)
   ratioPlot[v].SetMarkerColor(8)
   ratioPlot[v].SetMarkerStyle(20)
   ratioPlot[v].SetMarkerSize(1)
   ratioPlot[v].SetLineWidth(2)
   ratioPlot[v].Draw("E2same") #adds shaded area around error bars
   ratioPlot[v].Draw("Esame")

   #Save canvas
   if save: #web address: http://www.hephy.at/user/mzarucki/plots
      suffix = suff
      suffix += '_' + var[v]
   
      if v == "pt":
         savedir = savedir1
      else:
         savedir = savedir2
   
      canvs[v]['canvs'][0].SaveAs("%s/ISR%s.png"%(savedir, suffix))
      canvs[v]['canvs'][0].SaveAs("%s/root/ISR%s.root"%(savedir, suffix))
      canvs[v]['canvs'][0].SaveAs("%s/pdf/ISR%s.pdf"%(savedir, suffix))
