import sys
import Workspace.DegenerateStopAnalysis.tools.degTools as degTools
import Workspace.DegenerateStopAnalysis.samples.baselineSamplesInfo as samplesInfo
import pickle
import ROOT
import os
u_float = degTools.u_float 


        

def getPkl( pkl_path, def_dict={}):
    pkl_path = os.path.expandvars(pkl_path)
    print 'get pkl %s'%pkl_path
    if os.path.isfile( pkl_path):
        try:
            ret = pickle.load( open(pkl_path,'r') )

        except:
            print "Something wrong with the pickle file:\n %s \n Got this Error: \n %s"%(pkl_path, sys.exc_info()[0] )
            raise
    else:
        ret = deepcopy( def_dict )
        print "def", ret.keys()
    return ret


absSysFunc    = lambda a,b : (abs(1.- (b/a).val)   * 100) if a.val else 0
#SignedSysFunc = lambda a,b : ((-1.+ (b/a).val)   * 100) if a.val else 0
SignedSysFunc = lambda a,b : (((b-a)/a.val)   * 100) if a.val else u_float( 0 )
mean          = lambda l :   sum(l)/float(len(l)) if len(l) else None


def meanSys(*a):
    """assume first value is the central value"""
    central = a[0]
    variations = a[1:]
    if not variations:
        raise Exception("No Variations Given! %s"%a)
    systs = []
    for var in variations:
        systs.append( absSysFunc(central, var) )
    #print systs, mean(systs)
    return mean(systs)


def round_sig(x, sig=2):
    return round(x, sig - int(floor(log10(abs(x) )))-1) 

def getSign(val):
    return -1*(val<0) + 1*(val>=0)

def convertRelSysForCard( rel_sys , convert_to = "lnN" ):
    dists = ["lnN"]
    if not convert_to in dists:
        raise Exception( "Only the following distributions are implemented %s"%dists )
    unc = pow( (1+abs(rel_sys)) , getSign(rel_sys) ) 
    return unc


def meanSysSigned(*a): ### keep track of the signs somehow for systematics in cards
    """assume first value is the central value
    """
    central = a[0]
    variations = a[1:]
    if not variations:
        raise Exception("No Variations Given! %s, %s"%(a, variations) )
    systs = []
    sign = 1
    #signed_systs = []
    for var in variations:
        syst_val = sign*SignedSysFunc(central, var)
        #syst_val = SignedSysFunc(central, var) 
        systs.append( syst_val)
        #signed_systs.append( sign* syst_val ) 
        sign *= -1
    #print systs
    syst_sign = (sum(systs).val < 0)*(-1) + (sum(systs).val >= 0)*(1)
    syst_mean = mean([abs(x.val) for x in systs])
    stat_errs = mean(systs).sigma ## do we want to include stat error in syst?
    #return u_float( syst_sign * syst_mean, stat_errs)
    ret = syst_sign * syst_mean
    return round(ret, 4)

getSysts = lambda *vals: [ meanSys(*vals) , meanSysSigned(*vals) ] 

def getBkgSysts(varYlds, varTypes, keys = []):
    assert varTypes[0]=='central'
    return { k:degTools.dict_manipulator( [varYlds[varType][k] for varType in varTypes], meanSysSigned ) for k in keys }
    #return degTools.dict_manipulator( [ bkgPreds[varType][bkg] for varType in varTypes], getSysts )


def getSystsFromVariations( varYlds, varTypes, bins=[], processes=[] , niceNames = {}):
    assert varTypes[0] == 'central'
    syst_dict = {}
    bins = bins if bins else varYlds['central'].keys()
    processes_ = processes[:]
    for b in bins:
        processes = processes_ if processes_ else varYlds['central'][b].keys()
        syst_dict[b]={}
        for p in processes : 
            #print [ (varType, p in varYlds[varType][b]  ) for varType in varTypes ]
            #print p
            vals = [ varYlds[varType][b][p] for varType in varTypes ]
            #print b, p, vals
            syst = meanSysSigned( *vals )
            pName = niceNames.get(p,p)
            syst_dict[b][pName]= syst
    return syst_dict

def getValFrom1BinnedHistOrGraph( hist ):
    """
        if input is AsymTGraph, the average of errors is given 
    """
    if type(hist) in [ ROOT.TH1F , ROOT.TH1D ]:
        v = hist.GetBinContent(1)
        e = hist.GetBinError(1)
    if type(hist) in [ ROOT.TH2F , ROOT.TH2D ]:
        v = hist.GetBinContent(1,1)
        e = hist.GetBinError(1,1)
    if type(hist) in [ROOT.TGraphAsymmErrors]:
        v = hist.GetY()[0]
        el = hist.GetEYlow()[0]
        eh = hist.GetEYhigh()[0]
        if el and eh:
            e  = sum( [abs(el), abs(eh)] )/2.
        else:
            e  = max(abs(el),abs(eh))
        #print hist , (v,el,eh)
        #return (v, el, eh )
    return degTools.u_float(v,e)


def getMLFBins( mlfit ):
    prefit_dir = mlfit.Get("shapes_prefit")
    channels = [x.GetName() for x in prefit.GetListOfKeys()]
    bins     = [x.replace("ch1_","") for x in channels]
    return bins   

def getTobj(filename,objname):
  tfile = ROOT.TFile(filename,"READ")
  tobj = tfile.Get(objname)
  tobj.SetDirectory(0)
  return tobj

def getPrePostFitFromMLF( mlfit ):
    if type(mlfit)==type(""):
        mlfit = ROOT.TFile(mlfit, "READ")
    shape_dirs = ['shapes_prefit', 'shapes_fit_b', 'shapes_fit_s']
    shape_hists = {}
    for shape_dir_name in shape_dirs:
        shape_dir = mlfit.Get(shape_dir_name)
        list_of_channels = [x.GetName() for x in shape_dir.GetListOfKeys() if x.IsFolder()]
        shape_hists[shape_dir_name] = {}
        for channel_name in list_of_channels:
            channel  = shape_dir.Get(channel_name)
            bin_name = channel_name.replace("ch1_","")
            list_of_hists = [x.GetName() for x in channel.GetListOfKeys() ]
            shape_hists[shape_dir_name][bin_name] = {}
            for hist in list_of_hists:
                shape_hists[shape_dir_name][bin_name][hist] = channel.Get(hist)
                #try: 
                #    shape_hists[shape_dir_name][bin_name][hist].SetDirectory(0)
                #    print "------------- SetDirectory for ", shape_hists[shape_dir_name][bin_name][hist]
                #except:
                #    print "------------- Couldnt SetDirectory for ", shape_hists[shape_dir_name][bin_name][hist]
                
    shape_results = degTools.dict_function( shape_hists, func = getValFrom1BinnedHistOrGraph )
    return {'hists':shape_hists, 'results':shape_results }


h_colors ={
                    "Total": ROOT.kBlack,
                    "WJets": ROOT.kGreen,
                    "Fakes": ROOT.kViolet,
                   "TTJets": ROOT.kAzure,
                   "Others": ROOT.kOrange,
                   'signal': ROOT.kRed,
                  }

#uniqueHash = degTools.uniqueHash
uniqueHash = lambda : degTools.uniqueHash()[:15]


def plotResults( result_dict , bkg_procs , data_tag = "data" , sig_tag = "signal" , bin_order=[], prefix="" , hist_colors = {} , hist_decors = {}):
    if not bin_order:
        bin_order = result_dict.keys()
    hists = {}
    for proc in bkg_procs + [ data_tag ] + [sig_tag] + ['total_background','total_covar','total_signal'] :
        hists[proc] = degTools.makeHistoFromDict( result_dict , name = prefix + proc +"_"+ uniqueHash() ,bin_order = bin_order , func = lambda x: x.get(proc, degTools.u_float(0)) )
        if hist_colors:
            if proc == data_tag:
                hists[proc].SetMarkerStyle(20)
                hists[proc].SetMarkerSize(0.9)
                hists[proc].SetLineColor(ROOT.kBlack)
                hists[proc].SetMarkerColor(ROOT.kBlack)
            elif proc == sig_tag  and proc in hist_colors :
                hists[proc].SetLineStyle(5)
                hists[proc].SetLineWidth(3)
                hists[proc].SetLineColor( hist_colors[proc] )
            elif proc in bkg_procs and proc in hist_colors:
                hists[proc].SetFillColor( hist_colors[proc])
                hists[proc].SetLineColor( hist_colors[proc])
                hists[proc].SetMarkerSize( 0.8 )
            
        if proc in hist_decors:
            hist_decors[proc](hists[proc])

    stack = ROOT.THStack(prefix + "stack"+ "_"+uniqueHash() , prefix + "stack" + "_"+uniqueHash() )    
    print '++++', stack
    

    for proc in bkg_procs:
        #hists[proc].SetDirectory(0)
        stack.Add(hists[proc])
    #print "getting ratio"
    #ratio = hists[data_tag].Clone( prefix + "ratio" + "_"+uniqueHash())
    total = hists["total_background"]
    #total = stack.GetHists()[0].Clone(prefix + "total"+"_"+uniqueHash())
    #total.Reset()
    #total.Merge( stack.GetHists() )
    #ratio.Divide( total ) 
    #hists['ratio'] = ratio
    hists['total'] = total
    hists['stack'] = stack
    return hists




def getDataMCRatios( data_hist, mc_hist ):
    import array as ar
    efill = 3002
    
    if type(mc_hist) == ROOT.THStack :
        stack = mc_hist.Clone("stack"+uniqueHash())
        mc_hist = stack.GetHists().Last().Clone("mc_hist" + uniqueHash() )
        mc_hist.Reset()
        mc_hist.Merge( stack.GetHists() )
        

    unity = mc_hist.Clone( "IAmOne" +uniqueHash())
    unity.SetLineColor(1)
    unity.SetLineWidth(1)
    unity.SetFillColor(0)
    nBins = unity.GetNbinsX()
    mc_noe = mc_hist.Clone( "mc_noerror" + uniqueHash())
    #mc_noe.Sumw2(0)
    mc_noe.SetError(ar.array( "d",[0]*(nBins+1) ) ) 
    
    mc_e = mc_hist.Clone( "mc_error" + uniqueHash())
    mc_e.Divide(mc_noe)
    mc_e.SetFillStyle(efill)
    mc_e.SetFillColor(1)
    mc_e.SetMarkerSize(0)

    for ib in range( nBins+1 ):
        unity.SetBinContent(ib, 1)
        unity.SetBinError(ib, 0)

    data_ratio = data_hist.Clone( "data_ratio" + uniqueHash() )
    data_ratio.Divide( mc_noe )

    mc_eb = mc_hist.Clone("mc_errorbar" + uniqueHash())
    mc_eb.SetFillStyle( efill )
    mc_eb.SetMarkerSize(0)
    mc_eb.SetFillColor(ROOT.kBlue-5)

    return data_ratio, mc_e, mc_eb , unity, mc_noe


def testdivide(mc_hist):
    import array as ar
    nBins = mc_hist.GetNbinsX()
    mc_noe = mc_hist.Clone( "mc_noerror" + uniqueHash())
    mc_noe.SetError(ar.array( "d",[0]*(nBins+1) ) )
    mc_e = mc_hist.Clone( "mc_error" + uniqueHash())
    mc_e.Divide(mc_noe)
    lb = mc_noe.GetBinError( nBins)
    if lb>100000:
        return mc_e
    else:
        return  True



def drawCMSHeader( preliminary = "Preliminary", lumi = 35.9, lxy = [0.16,0.91], rxy=[0.77,0.91]):
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    font=22
    latex.SetTextFont(font)
    #latexTextL = "#font[%s]{CMS %s}"%(font, preliminary)
    latexTextL = "CMS %s"%(preliminary)
    latexTextR = "\\mathrm{%0.1f\, fb^{-1} (13\, TeV)}"%(lumi)
    latex.DrawLatex(lxy[0],lxy[1],  latexTextL)
    latex.DrawLatex(rxy[0],rxy[1],  latexTextR)


def drawNiceDataPlot( data_hist, mc_stack, sig_stack = None ,mc_total = None, options={} , saveDir = "./" , name = "plot", leg= None):
    """
           mc_total can be given in order to propegate errors fully, otherwise errors in mc_stack will be added in quad
    """

    canv = []
    ratios = [] 
    uq    = name+"_"+uniqueHash()
    print uq

    if not mc_total:
        mc_total = mc_stack.GetHists()[0].Clone( "total"+"_"+uq)
        mc_total.Reset()
        mc_total.Merge( mc_stack.GetHists() )


    canv_hw=(800,800)
    canv  = degTools.makeCanvasMultiPads( uq , canv_hw[0], canv_hw[1] , pads=[], padRatios =[2,1] )
    print canv
    canv[1].cd()
    setLogY = options.get('logy',1)
    canv[1].SetLogy( setLogY )
    ratios = getDataMCRatios( data_hist  , mc_total )
    data_ratio , mc_e, mc_eb, unity, mc_noe = ratios
    ymax = max( degTools.getHistMax( mc_noe )[1] , degTools.getHistMax( data_hist )[1] )
    if sig_stack:
        ymin = min( [degTools.getHistMin( mc_stack.GetHists().First() )[1] , degTools.getHistMax( data_hist )[1] , ])
    else:
        ymin = min( [degTools.getHistMin( mc_stack.GetHists().First() )[1] , degTools.getHistMax( data_hist )[1] , degTools.getHistMax( sig_stack.GetHists().First() )[1] ])
    ymin = 1E-2
    extras = [mc_stack]
    print '---------------', mc_stack
    mc_stack.Print("all")
    mc_eb.Draw("E2")
    # Recreating the stack here for some reason because ROOT segfaults if I use mc_stack ( no clue why! )
    stack = ROOT.THStack( mc_stack.GetTitle() + "2", mc_stack.GetName() )  
    for h in mc_stack.GetHists():
        stack.Add(h)
        print h.Draw("same")
    mc_stack = stack
    # Seems like a bug, should probably tell Rene!
    mc_stack.Draw("hist")
    mc_stack.SetMaximum(ymax* ( 1.5 + 15*setLogY) )
    mc_stack.SetMinimum( ymin )
    mc_eb.Draw("E2same")
    mc_e.Print("all")
    data_hist.Draw("same")
    if sig_stack:
        sig_stack.Draw("same hist")

    drawCMSHeader()
    if leg:
        leg.Draw()
    canv[2].cd()
    unity.Draw()
    mc_e.Draw("E2same")
    unity.GetYaxis().SetLabelSize( unity.GetYaxis().GetLabelSize()*2)
    unity.SetNdivisions(505, "y")
    nBinsX = unity.GetNbinsX()
    xsize = canv_hw[0]/( nBinsX +1)/180. #180 scale is arbitrary (but emperical!)
    xsize = min([0.12, xsize])
    unity.GetXaxis().SetLabelSize( xsize )
    unity.GetXaxis().LabelsOption("v")
    mc_e.Draw("E2same")
    data_ratio.Draw("E0p same")
    data_ratio.SetMaximum(2)
    data_ratio.SetMinimum(0)
    degTools.saveCanvas( canv[0], saveDir , name)
    return canv, ratios  


def makeTLegends():
    pass

def getSFsFromPostPreFitPlots( plots , plotDir , saveDir , bins = [] , keys = [ 'Fakes', 'WJets', 'TTJets' , 'stack' ] , name = "PostPre", hist_colors=h_colors, dOpt="hist text") :
    """
        Get SF as the ratio of postfit/prefit (fit_b/prefit) only keeping the postfit uncertainty
    """
    plot_values = degTools.dict_function( plots, lambda x: degTools.getTH1FbinContent( x , get_errors=True)  ) #if type( x ) in [ ROOT.TH1F , ROOT.TH2F] else None ) 
    #SFs = {'WJets':{}, 'TTJets':{} , 'Fakes':{} , 'stack':{}}
    SFs = {k:{} for k in keys}
    SF_hists = degTools.deepcopy(SFs)
    canv_sfs = ROOT.TCanvas( "SFs", "SFs", 1000,800 )
    dOpt_ = "%s"%dOpt
    ROOT.gStyle.SetPaintTextFormat("0.2f")
    hsh = degTools.uniqueHash()
    for bkg in keys:
        SFs[bkg]      = degTools.dict_manipulator( [ plot_values[f][bkg] for f in ['fit_b', 'prefit' ] ] ,  lambda a,b: a/b.val if b.val else u_float(1.0) )
        SF_hists[bkg] = degTools.makeHistoFromDict( SFs[bkg], bin_order = bins, name = "TF_%s_%s"%(bkg,hsh))
        SF_hists[bkg].GetXaxis().SetLabelSize(0.05)
        SF_hists[bkg].SetLineColor( hist_colors[bkg] )
        SF_hists[bkg].SetMarkerColor( hist_colors[bkg] )
        SF_hists[bkg].SetMarkerColor( hist_colors[bkg] )
        SF_hists[bkg].Draw(dOpt_)
        SF_hists[bkg].SetMinimum(0.65)
        SF_hists[bkg].SetMaximum(1.7)
        dOpt_='same %s'%dOpt
    #output_name = name.replace(".pkl", "_SFs.pkl")
    name = name if name.endswith(".pkl") else "%s.pkl"%name
    degTools.pickle.dump( SFs, file('%s/%s'%(saveDir, name) , 'w') )
    degTools.saveCanvas( canv_sfs, plotDir, name.replace(".pkl","") )
    return SFs, SF_hists

def makeTableFromMLFResults( mlf_res , bins = [] , data='data', signal='signal', total='total_background' , bkg=['WJets', 'TTJets', 'Fakes', 'Others'] , 
                                       niceNames = {'total_background': 'Total MC', 'data':'Data'} , 
                                       func = lambda x, samp: int(x.val) if samp=='data' else x.round(2) ):
    fits = mlf_res.keys()
    sample_legends = bkg + [ total, data, signal ]
    bins_ = bins[:]
    table_list = []
    bins = bins_ if bins_ else sorted( [b for b in mlf_res.keys() if 'cr' in b] )
    table_list.append( [''] + [ niceNames.get(samp, samp) for samp in sample_legends] )
    for b in bins : 
        table_list.append( [niceNames.get(b,b)]+[func(mlf_res[b].get(samp, u_float(-0,0)), samp) for samp in sample_legends] )
    return table_list 
    

class MaxLikelihoodResult():
    """
        Runs the MLF, starting from card to the post/pre plots
        input bins will be masked , i.e. for CR only fit
    """
    fits = ['prefit', 'fit_b', 'fit_s']
    
    h_colors ={
                "Total": ROOT.kBlack,
                "stack": ROOT.kBlack,
                "WJets": ROOT.kGreen,
                "Fakes": ROOT.kViolet,
               "TTJets": ROOT.kAzure,
               "Others": ROOT.kOrange,
               "signal": ROOT.kRed,
              }


    def __init__(self, mlf_file , bins = None  , plotDir ="./", saveDir = "./", output_name = "mlf_output.pkl" , hist_colors = h_colors, fits = fits , rerun=True, sig_name=None):


        sr_bins = [ b for b in bins if 'sr' in b ] 
        cr_bins = [ b for b in bins if 'cr' in b ] 

        if mlf_file.endswith(".root"):
            pass
        if mlf_file.endswith(".txt"):
            card = mlf_file[:]
            import Workspace.DegenerateStopAnalysis.tools.limitTools as limitTools
            mlf_basename = card.replace(".txt","_mlf.root")
            mlf_file_srmasked     = mlf_basename.replace("_mlf.root", "_mlf_SRMasked.root")       #CROnly Fit
            mlf_file_nosrmasked     = mlf_basename.replace("_mlf.root", "_mlf_NoSRMasked.root")
            mlf_file = mlf_file_srmasked 
            if rerun or not os.path.isfile(mlf_file):
                print '\n Running MLF on %s , the output will be %s \n '%(card, mlf_file) 
                limitTools.runMLF( card , mlf_basename , bins = sr_bins ) 
        print mlf_file
        if not os.path.isfile( mlf_file):
            raise Exception(" File not found : %s"%mlf_file )
        #self.mlfit         = ROOT.TFile(mlf_file, "READ")
        #self.mlf_out       = getPrePostFitFromMLF( self.mlfit )
        self.mlf_out       = getPrePostFitFromMLF( mlf_file )
        self.mlf_results   = self.mlf_out['results']
        self.file_basename = degTools.get_filename( mlf_file )

        degTools.makeDir( saveDir)
        degTools.makeDir( plotDir)
        pickle.dump( self.mlf_results , file(saveDir + "/" + output_name , "w")) 
    
        plots   = {}
        self.plots = plots 


        hists      = {}
        hists_crs  = {}
        hists_srs  = {}
        extraPlots ={"SR":{},"CR":{}}
        plots      = {}
        degTools.makeDir(saveDir)
        degTools.makeDir(plotDir)

        canvs = []
        junk  = []
        junk.append( extraPlots ) 
        drawCRs = True

        bkg_list = ["WJets", "TTJets", "Fakes","Others"]
        isFirst = True

        for fit in fits : 
            hists[fit] = plotResults(    
                                        self.mlf_results['shapes_%s'%fit] , list( reversed( bkg_list)) , 
                                        bin_order = sr_bins + cr_bins   , 
                                        prefix = fit                    ,   
                                        hist_colors = hist_colors          ,
                                    )
            if isFirst:
                isFirst = False
                loc = [0.6, 0.66, 0.8, 0.87]
                leg = ROOT.TLegend(*loc)
                leg.SetFillColor(0)
                leg.SetFillColorAlpha(0,0)
                leg.SetBorderSize( 0 )
                hists_info =  [{'hist':hists[fit][name], 'name':samplesInfo.sampleName(name,"latexName") , 'opt':'f'} for name in bkg_list ]
                degTools.addHistsToLeg(leg, hists_info) 
                #leg2 = ROOT.TLegend(loc[0]-0.3,loc[1],loc[2]-0.3,loc[3])
                #leg2.SetFillColor(0)
                #leg2.SetFillColorAlpha(0,0)
                #leg.SetBorderSize( 0 )
                if sig_name:
                    sig_name = sig_name
                sig_name = sig_name if sig_name else "T2tt"
                hists_info = [ 
                                {'hist':hists[fit]['data']    , 'name':samplesInfo.sampleName('data',"latexName") , 'opt':'lep'} ,
                                {'hist':hists[fit]['signal']  , 'name':sig_name , 'opt':'l'} 
                             ]
                degTools.addHistsToLeg(leg, hists_info) 
                junk.append(leg)


            if drawCRs:
                ROOT.gStyle.SetPaintTextFormat("0.2f") 
                hists_crs[fit] = plotResults(    
                                            self.mlf_results['shapes_%s'%fit] , list( reversed( bkg_list)) , 
                                            bin_order = cr_bins   , 
                                            prefix = "CR"+fit                    ,   
                                            hist_colors = hist_colors          ,
                                        )
                hists_srs[fit] = plotResults(    
                                            self.mlf_results['shapes_%s'%fit] , list( reversed( bkg_list)) , 
                                            bin_order = sr_bins   , 
                                            prefix = "SR"+fit                    ,   
                                            hist_colors = hist_colors          ,
                                        )
                hsh = degTools.uniqueHash()
                stack = hists_crs[fit]['stack'].Clone('stack_%s'%hsh)
                normalized_stack = degTools.normalizeStack( stack ) 
                canv = ROOT.TCanvas( "Canv_%s_%s"%(fit, hsh), "Canv_%s_%s"%(fit, hsh), 1000, 800)
                normalized_stack.Draw("hist text0")
                degTools.saveCanvas( canv, plotDir, "CRsComposition_%s"%fit ) 
                #
                stack.Draw("hist text0")
                canv.SetLogy(1)
                data = hists_crs[fit]['data'].Clone('data_%s'%hsh)
                data.Draw("same")
                degTools.saveCanvas( canv, plotDir, "CRs_%s"%fit ) 
                canvs.append(canv)
                junk.append(canvs)
                junk.append(stack)
                junk.append(normalized_stack)

                #regions compositions
                stack = hists[fit]['stack'].Clone('Regions_stack_%s'%hsh)
                normalized_stack = degTools.normalizeStack( stack ) 
                canv.SetLogy(0)
                normalized_stack.Draw("hist")
                degTools.saveCanvas( canv, plotDir, "Regions_Composition_%s"%fit ) 
                #SR Compositions

                
                stack = hists_srs[fit]['stack'].Clone('SRs_stack_%s'%hsh)
                normalized_stack = degTools.normalizeStack( stack ) 
                canv.SetLogy(0)
                h = normalized_stack.GetHists().First()
                h.LabelsOption("V")
                h.Draw("hist")
                normalized_stack.Draw("hist")
                leg.Draw()
                degTools.saveCanvas( canv, plotDir, "SRs_Composition_%s"%fit ) 
                #
                #stack.Draw("hist text0")
                #canv.SetLogy(1)
                #data = hists_crs[fit]['data'].Clone('data_%s'%hsh)
                #data.Draw("same")
                #degTools.saveCanvas( canv, plotDir, "CRs_%s"%fit ) 
                #canvs.append(canv)
                #junk.append(canvs)
                #junk.append(stack)
                junk.append(normalized_stack)



            #canvs[fit] = degTools.makeCanvasMultiPads( fit, 800,800, pads=[], padRatios =[2,1] )
            print 'got hists %s'%fit
            plots[fit] = drawNiceDataPlot( 
                                            data_hist = hists[fit]['data'] , 
                                            mc_stack  = hists[fit]['stack'] , 
                                            sig_stack = hists[fit]['signal'] , 
                                            mc_total  = hists[fit]['total_background'],
                                            options   = {'logy':1} , 
                                            saveDir   = plotDir           , 
                                            name      = fit , 
                                            leg       = leg, 
                                         )
            print 'made plots %s'%fit
            if drawCRs:
                pass
                for srcr, srcrhists in [ ("SR", hists_srs), ("CR",hists_crs)]:
                    extraPlots[srcr][fit] = drawNiceDataPlot( 
                                                    data_hist = srcrhists[fit]['data'] , 
                                                    mc_stack  = srcrhists[fit]['stack'] , 
                                                    sig_stack = srcrhists[fit]['signal'] , 
                                                    mc_total  = srcrhists[fit]['total_background'],
                                                    options   = {'logy':1} , 
                                                    saveDir   = plotDir           , 
                                                    name      = srcr+"_"+fit , 
                                                    leg       = leg, 
                                                 )
        ##
        prefit_hist , postfit_hist = hists['prefit']['total'] , hists['fit_b']['total']
        pulls       = getPullFromPrePostFit( prefit_hist, postfit_hist)
        junk.append(pulls)
        ##

        sf_output_file = output_name.replace(".pkl","_SFs.pkl") 
        self.sf_output_file = sf_output_file
        print "getting sfs"
        self.SFs = getSFsFromPostPreFitPlots( hists , plotDir, saveDir , bins = bins , hist_colors = hist_colors, name = sf_output_file  )  
        if drawCRs:
            print "getting CR sfs"
            self.CRSFs = getSFsFromPostPreFitPlots( hists_crs , plotDir, saveDir , bins = cr_bins , hist_colors = hist_colors, name = "CRSFs.pkl"  )  
            self.hists_crs = hists_crs
            self.hists_crs = hists_srs

        self.junk  = junk
        self.hists = hists
        self.plots = plots
        self.canvs = canvs
        print "Done Here"
        #import gc
        #gc.collect()

CR_SF_map={
 #'presel': None 
 'sr1a'  :  'cr1a'  , 
 'sr1la' :  'cr1a'  , 
 'sr1ma' :  'cr1a'  , 
 'sr1ha' :  'cr1a'  , 
 'sr1b'  :  'cr1b'  ,
 'sr1lb' :  'cr1b'  ,
 'sr1mb' :  'cr1b'  ,
 'sr1hb' :  'cr1b'  ,
 'sr1c'  :  'cr1c'  ,
 'sr1lc' :  'cr1c'  ,
 'sr1mc' :  'cr1c'  ,
 'sr1hc' :  'cr1c'  ,
 'sr2'   :  'cr2'  ,
 'sr2l'  :  'cr2'  ,
 'sr2m'  :  'cr2'  ,
 'sr2h'  :  'cr2'  ,
 'cr1a'  :  'cr1a'  , 
 'cr1b'  :  'cr1b'  ,
 'cr1c'  :  'cr1b'  , 
 'cr2'   :  'cr1b'  , 
 'crtt'  :  'crtt'  ,
 }

TransferFactorMap ={

    "WJets": 
            { 
                 'sr1a'  :  'cr1a'  ,
                 'sr1la' :  'cr1a'  ,
                 'sr1ma' :  'cr1a'  ,
                 'sr1ha' :  'cr1a'  ,
                 'sr1b'  :  'cr1b'  ,
                 'sr1lb' :  'cr1b'  ,
                 'sr1mb' :  'cr1b'  ,
                 'sr1hb' :  'cr1b'  ,
                 'sr1c'  :  'cr1c'  ,
                 'sr1lc' :  'cr1c'  ,
                 'sr1mc' :  'cr1c'  ,
                 'sr1hc' :  'cr1c'  ,
                 'sr2'   :  'cr2'  ,
                 'sr2l'  :  'cr2'  ,
                 'sr2m'  :  'cr2'  ,
                 'sr2h'  :  'cr2'  ,
                 'cr1a'  :  'cr1a'  , 
                 'cr1b'  :  'cr1b'  ,
                 'cr1c'  :  'cr1b'  , 
                 'cr2'   :  'cr2'  , 
            },
    "TTJets":
            { 
                 'sr1a'  :  'crtt'  ,
                 'sr1la' :  'crtt'  ,
                 'sr1ma' :  'crtt'  ,
                 'sr1ha' :  'crtt'  ,
                 'sr1b'  :  'crtt'  ,
                 'sr1lb' :  'crtt'  ,
                 'sr1mb' :  'crtt'  ,
                 'sr1hb' :  'crtt'  ,
                 'sr1c'  :  'crtt'  ,
                 'sr1lc' :  'crtt'  ,
                 'sr1mc' :  'crtt'  ,
                 'sr1hc' :  'crtt'  ,
                 'sr2'   :  'crtt'  ,
                 'sr2l'  :  'crtt'  ,
                 'sr2m'  :  'crtt'  ,
                 'sr2h'  :  'crtt'  ,
                 'cr1a'  :  'crtt'  , 
                 'cr1b'  :  'crtt'  ,
                 'cr1c'  :  'crtt'  , 
                 'cr2'   :  'crtt'  , 
                 'crtt'  :  'crtt'  , 
            },

        }

def getPullFromPrePostFit( prefit, postfit ):
    pulls = postfit.Clone()
    pulls.Reset()
    for i in range(1, pulls.GetNbinsX()+1):
        pre_v  = prefit.GetBinContent(i)
        post_v = postfit.GetBinContent(i)
        post_e = postfit.GetBinError(i)
        pull   = (post_v - pre_v )/post_e
        pulls.SetBinContent(i, pull)
    return pulls

def testPulls( pulls_hist ):
    pull_dist = ROOT.TH1F("pulls","pulls", 100,-10,10)
    for p in pulls_hist:
        pull_dist.Fill(p)
    pull_dist.Fit("gaus","S")
    return pull_dist
    

def getBinValErr( hist, ib):
    v = hist.GetBinContent(ib)
    e = hist.GetBinError(ib)
    return degTools.u_float(v,e)    




def applySFsToYields( yldInst, SFs, TF_Map=TransferFactorMap, bkgList = None, bins = None):
    
    bkgYldsOrig = {}
    bkgEst      = {}

    for bkg in bkgList:
        bkgYldsOrig[bkg] = {}
        bkgEst[bkg]      = {}
        applyTF = bkg in TF_Map
        for b in bins:
            v = yldInst[bkg][b]
            sf = 1
            if applyTF:
                transferFrom = TF_Map[bkg].get(b)
                if transferFrom : 
                    sf  = SFs[transferFrom][bkg]
                    print bkg, b, sf
            bkgYldsOrig[bkg][b] = v 
            bkgEst[bkg][b]        = v*sf

    return bkgYldsOrig, bkgEst


if __name__ == '__main__':
    pass
