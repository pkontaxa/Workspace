# shapeComparison.py
# Script for making comparing W and TT shape (superimposed) 
# Mateusz Zarucki 2016

import ROOT
import os, sys
import argparse
#import Workspace.DegenerateStopAnalysis.toolsMateusz.ROOToptions
from Workspace.DegenerateStopAnalysis.toolsMateusz.drawFunctions import *
#from Workspace.DegenerateStopAnalysis.toolsMateusz.pythonFunctions import *
from Workspace.DegenerateStopAnalysis.tools.degTools import CutClass, Plots, getPlots, drawPlots, Yields, setEventListToChains, setup_style
from Workspace.DegenerateStopAnalysis.tools.degPlots import DegPlots
from Workspace.DegenerateStopAnalysis.tools.degCuts import Cuts
from Workspace.DegenerateStopAnalysis.tools.bTagWeights import bTagWeights
from Workspace.DegenerateStopAnalysis.tools.degCuts import *
from Workspace.DegenerateStopAnalysis.tools.getSamples_8012 import getSamples
from Workspace.DegenerateStopAnalysis.samples.cmgTuples_postProcessed.cmgTuplesPostProcessed_mAODv2_2016 import cmgTuplesPostProcessed
from array import array
from math import pi, sqrt #cos, sin, sinh, log

#Sets TDR style
setup_style()

#Input options
parser = argparse.ArgumentParser(description = "Input options")
parser.add_argument("--getData", dest = "getData",  help = "Get data samples", type = int, default = 0)
parser.add_argument("--region", dest = "region",  help = "Region", type = str, default = "presel")
parser.add_argument("--scale", dest = "scale",  help = "Scale", type = int, default = 0)
parser.add_argument("--btag", dest = "btag",  help = "B-tagging option", type = str, default = "sf")
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
getData = args.getData
region = args.region
scale = args.scale
btag = args.btag
logy = args.logy
save = args.save
verbose = args.verbose

print makeDoubleLine()
print "Plotting MC distributions"
print makeDoubleLine()

#Samples
samplesList = ["tt", "w"]
#samplesList = ["vv", "st", "qcd", "z", "dy", "tt", "w"]
if getData: 
   data = "dblind"
   samplesList.append(data)

cmgPP = cmgTuplesPostProcessed()
samples = getSamples(cmgPP = cmgPP, skim = 'preIncLep', sampleList = samplesList, scan = False, useHT = True, getData = getData) 

if verbose:
   print makeLine()
   print "Using samples:"
   newLine()
   for s in samplesList:
      if s: print samples[s].name,":",s
      else: 
         print "!!! Sample " + sample + " unavailable."
         sys.exit(0)
 
#Save
if save: #web address: http://www.hephy.at/user/mzarucki/plots
   tag = samples[samples.keys()[0]].dir.split('/')[7] + "/" + samples[samples.keys()[0]].dir.split('/')[8]
   savedir = "/afs/hephy.at/user/m/mzarucki/www/plots/%s/WTTplots"%tag
   #savedir += "/" + skim
   #if btag: savedir += "/" + btag
   #else: savedir += "/no_btag"
   suffix = "_" + region
   if scale: suffix += "_areaNormalised" 
   if not os.path.exists("%s/root"%(savedir)): os.makedirs("%s/root"%(savedir))
   if not os.path.exists("%s/pdf"%(savedir)): os.makedirs("%s/pdf"%(savedir))

plotDict = {
   "lep_mt":           {'var':"LepAll_mt[IndexLepAll_lep[0]]"       ,"bins":[40,0,200]          ,"nMinus1":None         ,"decor":{"title":"lepMT"    ,"x":"M_{{T}}({lepLatex}) "      ,"y":"Events"  ,'log':[0,logy,0] }},
   "lepPt" :        {'var':"LepAll_pt[IndexLepAll_lep[0]]"       ,"bins":[10,0,200]          ,"nMinus1":""      ,"decor":{"title":"lepPt"           ,"x":"Lepton p_{T}"      ,"y":"Events"  ,'log':[0,logy,0] }},
   "lep_Eta" :       {'var':"LepAll_eta[IndexLepAll_lep[0]]"                         ,"bins":[20,-3,3]           ,"nMinus1":""         ,"decor":{"title":"lepEta"     ,"x":"#eta({lepLatex})"       ,"y":"Events  "  ,'log':[0,logy,0] }},
   "lep_Phi" :      {'var':"LepAll_phi[IndexLepAll_lep[0]]"                         ,"bins":[20,-3.15,3.15]           ,"nMinus1":None         ,"decor":{"title":"lepPhi"     ,"x":"lep Phi"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "met":          {'var':"met"                            ,"bins":[40,200,1000]        ,"nMinus1":"met"        ,"decor":{"title":"MET"    ,"x":"E^{miss}_{T}"      ,"y":"Events"  ,'log':[0,logy,0] }},
   "ht":           {'var':"ht_basJet"                     ,"bins":[40,200,1000]        ,"nMinus1":""           ,"decor":{"title":"HT"    ,"x":"H_{T}"      ,"y":"Events"  ,'log':[0,logy,0] }},
   "ct":           {'var':"min(met_pt,ht_basJet)"         ,"bins":[40,100,1000]        ,"nMinus1":""           ,"decor":{"title":"CT"    ,"x":"C_{T}"      ,"y":"Events"  ,'log':[0,logy,0] }},
   "MetPhi":       {'var':"met_phi"                        ,"bins":[20,-3.15,3.15]           ,"nMinus1":None         ,"decor":{"title":"MetPhi"    ,"x":"Met Phi"      ,"y":"Events"  ,'log':[0,logy,0] }},
   "isrPt":        {'var':"Jet_pt[IndexJet_basJet[0]]"     ,"bins":[45,100,1000]          ,"nMinus1":None         ,"decor":{"title":"Leading Jet P_{{T}}"    ,"x":"isrJetPt"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "isrPt2":       {'var':"Jet_pt[IndexJet_basJet[0]]"     ,"bins":[20,100,900]          ,"nMinus1":None         ,"decor":{"title":"Leading Jet P_{{T}}"    ,"x":"isrJetPt"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "isrPt_fine":   {'var':"Jet_pt[IndexJet_basJet[0]]"    ,"bins":[100,0,1000]          ,"nMinus1":None         ,"decor":{"title":"Leading Jet P_{{T}} "    ,"x":"isrJetPt"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "nJets30":      {'var':"nBasJet"                       ,"bins":[10,0,10]          ,"nMinus1":None         ,"decor":{"title":"Number of Jets with P_{{T}} > 30GeV"    ,"x":"Number of Jets with P_{T} > 30GeV"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "nJets60":      {'var':"nVetoJet"                      ,"bins":[10,0,10]          ,"nMinus1":None         ,"decor":{"title":"Number of Jets with P_{{T}} > 60GeV"    ,"x":"Number of Jets with P_{T} > 60GeV"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "nSoftBJets":   {'var':"(nBSoftJet)"                   ,"bins":[6,0,6]            ,"nMinus1":None         ,"decor":{"title":"Number of Soft B-Tagged Jets with P_{{T}} < 60GeV"    ,"x":"Number of Soft B-Tagged Jets with P_{T} < 60GeV"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "nHardBJets":   {'var':"(nBHardJet)"                   ,"bins":[6,0,6]            ,"nMinus1":None         ,"decor":{"title":"Number of B-Tagged Jets with P_{{T}} > 60GeV"    ,"x":"Number of Hard B-Tagged Jets with P_{T} > 60GeV"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "nBJets":       {'var':"(nBHardJet + nBSoftJet)"       ,"bins":[6,0,6]            ,"nMinus1":None         ,"decor":{"title":"Number of B-Tagged Jets"                         ,"x":"Number of B-Tagged Jets"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "bJetPt":       {'var':"Jet_pt[ max(IndexJet_bJet[0],0)] *(nBJet>0)"      ,"bins":[100,0,1000]          ,"nMinus1":None         ,"decor":{"title":"bJet P_{{T}} "    ,"x":"P_{T}(BJet)"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "bSoftJetPt":       {'var':"Jet_pt[ max(IndexJet_bSoftJet[0],0)] *(nBSoftJet>0)"      ,"bins":[10,20,70]          ,"nMinus1":None         ,"decor":{"title":"bSoftJet P_{{T}} "    ,"x":"P_{T}(Soft BJet)"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   "bHardJetPt":       {'var':"Jet_pt[ max(IndexJet_bHardJet[0],0)] *(nBHardJet>0)"      ,"bins":[100,0,1000]          ,"nMinus1":None         ,"decor":{"title":"bHardJet P_{{T}} "    ,"x":"P_{T}(Hard BJet)"      ,"y":"Events  "  ,'log':[0,logy,0] }},
   }

#degplots = DegPlots("LepAll", "lep")
#plotsDict = degplots.plots

#bTagWeights
bWeightDict = bTagWeights(btag)
bTagString = bWeightDict['sr1_bjet'] #corresponds to bVeto
#bTagString = "nBJet == 0"

plotsDict = Plots(**plotDict)

degcuts = Cuts("LepAll", "lep", sr1c_opt = "MT95_IncCharge", isrpt = 100, btag = 'sf')

sr1IncCharge = CutClass ("SR1IncCharge", [
   ["CT300","min(met,ht_basJet-100) > 300 "],
   ["Veto BJets",bTagString],
   ["LepEta1.5","abs(LepAll_eta[IndexLepAll_lep[0]])<1.5"],
   #["{lep}Pt30".format(lep=lep.title()),"{lepCol}_pt[{lepIndex}[0]]<30".format(lepCol=lepCollection, lepIndex=lepIndex)],
   ],
   baseCut = degcuts.presel)

negCharge = CutClass("NegCharge", [
   ["negLep","(LepAll_pdgId[IndexLepAll_lep[0]]==13 || LepAll_pdgId[IndexLepAll_lep[0]]==11 )"],
   ],
   baseCut = sr1IncCharge,
)

sr1 = CutClass("SR1", [], baseCut = degcuts.presel)
sr1.add(sr1IncCharge)
sr1.add(negCharge)

if region == "presel": cut = degcuts.presel
elif region == "SR1": cut = sr1 #no lepPt cut

WTT_plots = getPlots(samples, plotsDict, cut, samplesList, plotList = ["lepPt"], addOverFlowBin='upper')
WTT_plots2 = drawPlots(samples, plotsDict, cut, samplesList, plotList = ["lepPt"], plotLimits = [1, 100], denoms=["w"], noms = ["tt"], fom="RATIO", fomLimits=[0,1.8], normalize = False, save=False) #, plotMin = 0.1

if scale:
   hist_tt = WTT_plots2['hists']['tt']['lepPt']
   hist_w = WTT_plots2['hists']['w']['lepPt']
   hist_tt.SetFillColorAlpha(hist_tt.GetFillColor(), 0.7)
   #hist_w.SetFillColorAlpha(hist_w.GetFillColor(), 0.80)
   
   hist_w.Scale(1/hist_w.Integral())
   hist_tt.Scale(1/hist_tt.Integral())
   
   hist_w.Draw('hist')
   hist_w.GetYaxis().SetTitle()
   hist_tt.Draw('histsame')
  
   if not logy: 
      hist_w.SetMinimum(0)
      hist_w.SetMaximum(0.225)
   
   WTT_plots2['legs'][0].Draw('same')
   
   latex = ROOT.TLatex()
   latex.SetNDC()
   latex.SetTextSize(0.04)
   
   latex.DrawLatex(0.16,0.92,"#font[22]{CMS Simulation}")
   
   ROOT.gPad.Modified()
   ROOT.gPad.Update()
   
   WTT_plots2['canvs']['lepPt'][2].cd()
   ratio = hist_tt.Clone()
   ratio.Divide(hist_w)
   ratio.SetMinimum(-0.5)
   ratio.SetMaximum(2.5)
   ratio.GetYaxis().SetTitle("TT/W Ratio")
   
   ratio.Draw()
   ROOT.gPad.Modified()
   ROOT.gPad.Update()

#Save canvas
if save: #web address: http://www.hephy.at/user/mzarucki/plots
      for canv in WTT_plots2['canvs']:
         #if plot['canvs'][canv][0]:
         WTT_plots2['canvs'][canv][0].SaveAs("%s/WTTshapeComparison_%s%s.png"%(savedir, canv, suffix))
         WTT_plots2['canvs'][canv][0].SaveAs("%s/root/WTTshapeComparison_%s%s.root"%(savedir, canv, suffix))
         WTT_plots2['canvs'][canv][0].SaveAs("%s/pdf/WTTshapeComparison_%s%s.pdf"%(savedir, canv, suffix))
