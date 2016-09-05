from Workspace.DegenerateStopAnalysis.tools.degTools import Weight
from Workspace.DegenerateStopAnalysis.tools.btag_sf_map import BTagSFMap
import re






def make_match_func(tothis):
   def match_func ( x ):
   ##      should use search instead, and then replace to make things less messy!
   ##      re.search( ".*%s"%(tothis.replace("(","\(").replace(")","\)").replace("*","\*")), x )
   ##
      return re.match( ".*%s"%(tothis.replace("(","\(").replace(")","\)").replace("*","\*")), x )
   return match_func




class Weights():
    def __init__(   self,
                    lepCol="LepAll",
                    lep="lep",
                    btag="sf",
                    jet="",
                    pu="puReweight", 
                    wpt="", 
                    ttpt="", 
                    isr="",
                    teff="",
                    lumis="",
                ):


        weightDict={}

        lepCol  = lepCol
        lep     = lep 
        lepIndex = "Index{lepCol}_{Lep}".format(lepCol=lepCol, Lep=lep)

        wptOpt = wpt
        if wptOpt:
            print wptOpt
            if wptOpt=='2wpt':
                wptweight_a_template = "(({wpt}<200)*1.+({wpt}>200&&{wpt}<250)*(2*1.008-1)+({wpt}>250&&{wpt}<350)*(2*1.063-1)+({wpt}>350&&{wpt}<450)*(2*0.992-1)+({wpt}>450&&{wpt}<650)*(2*0.847-1)+({wpt}>650&&{wpt}<800)*(2*0.726-1)+({wpt}>800)*(2*0.649-1))"
                wptweight_p_template = "(({wpt}<200)*1.+({wpt}>200&&{wpt}<250)*(2*1.016-1)+({wpt}>250&&{wpt}<350)*(2*1.028-1)+({wpt}>350&&{wpt}<450)*(2*0.991-1)+({wpt}>450&&{wpt}<650)*(2*0.842-1)+({wpt}>650&&{wpt}<800)*(2*0.749-1)+({wpt}>800)*(2*0.704-1))"
                wptweight_n_template = "(({wpt}<200)*1.+({wpt}>200&&{wpt}<250)*(2*0.997-1)+({wpt}>250&&{wpt}<350)*(2*1.129-1)+({wpt}>350&&{wpt}<450)*(2*1.003-1)+({wpt}>450&&{wpt}<650)*(2*0.870-1)+({wpt}>650&&{wpt}<800)*(2*0.687-1)+({wpt}>800)*(2*0.522-1))"
            else:
                wptweight_a_template = "(({wpt}<200)*1.+({wpt}>200&&{wpt}<250)*1.008+({wpt}>250&&{wpt}<350)*1.063+({wpt}>350&&{wpt}<450)*0.992+({wpt}>450&&{wpt}<650)*0.847+({wpt}>650&&{wpt}<800)*0.726+({wpt}>800)*0.649)"
                wptweight_p_template = "(({wpt}<200)*1.+({wpt}>200&&{wpt}<250)*1.016+({wpt}>250&&{wpt}<350)*1.028+({wpt}>350&&{wpt}<450)*0.991+({wpt}>450&&{wpt}<650)*0.842+({wpt}>650&&{wpt}<800)*0.749+({wpt}>800)*0.704)"
                wptweight_n_template = "(({wpt}<200)*1.+({wpt}>200&&{wpt}<250)*0.997+({wpt}>250&&{wpt}<350)*1.129+({wpt}>350&&{wpt}<450)*1.003+({wpt}>450&&{wpt}<650)*0.870+({wpt}>650&&{wpt}<800)*0.687+({wpt}>800)*0.522)"

            wpt = "(sqrt(({lepCol}_pt[max(0,{lepIndex}[0])]*cos({lepCol}_phi[max(0,{lepIndex}[0])]) + met_pt*cos(met_phi) ) **2 + ( {lepCol}_pt[max(0,{lepIndex}[0])]*sin({lepCol}_phi[max(0,{lepIndex}[0])])+met_pt*sin(met_phi) )^2 ))".format(lepCol = lepCol , lepIndex = lepIndex, Lep=lep)
            wptweight_a = wptweight_a_template.format(wpt=wpt)
            wptweight_n = wptweight_n_template.format(wpt=wpt)
            wptweight_p = wptweight_p_template.format(wpt=wpt)

            weightDict.update({
                     "w": {
                            "cuts":{ 
                                        #"neg_mu":      (wptweight_n  , lambda x: re.match( "n{lepCol}_{lep}==1".format(lepCol=lepCol, lep=lep), x ) and re.match( ".*{lepCol}_pdgId\[{lepIndex}\[0\]\]==-13.*".format(lepCol=lepCol, lepIndex=lepIndex) , x )  ),   ## cut_finder tries to match to the cutstring
                                        #"pos_mu":      (wptweight_p  , lambda x: re.match( "n{lepCol}_{lep}==1".format(lepCol=lepCol, lep=lep), x ) and re.match( ".*{lepCol}_pdgId\[{lepIndex}\[0\]\]==13.*".format(lepCol=lepCol, lepIndex=lepIndex) , x  )  ),
                                        #"mixed_mu":    (wptweight_a  , lambda x: re.match( "n{lepCol}_{lep}==1".format(lepCol=lepCol, lep=lep), x ) and not ( re.match( ".*{lepCol}_pdgId\[{lepIndex}\[0\]\]==13.*".format(lepCol=lepCol, lepIndex=lepIndex) , x  ) or re.match( ".*{lepCol}_pdgId\[{lepIndex}\[0\]\]==13.*".format(lepCol=lepCol, lepIndex=lepIndex) , x  ) ) ),
                                        "neg_mu":      (wptweight_n  , lambda x:  ("n{lepCol}_{lep}==1".format(lepCol=lepCol, lep=lep) in x) and ( "{lepCol}_pdgId[{lepIndex}[0]]==13".format(lepCol=lepCol, lepIndex=lepIndex) in x ) )  ,   ## cut_finder tries to match to the cutstring
                                        "pos_mu":      (wptweight_p  , lambda x: ( "n{lepCol}_{lep}==1".format(lepCol=lepCol, lep=lep) in x ) and ( "{lepCol}_pdgId[{lepIndex}[0]]==-13".format(lepCol=lepCol, lepIndex=lepIndex)  in x )),
                                        "mixed_mu":    ( wptweight_a  , lambda x: ( "n{lepCol}_{lep}==1".format(lepCol=lepCol, lep=lep) in x ) and not ( ( "{lepCol}_pdgId[{lepIndex}[0]]==13".format(lepCol=lepCol, lepIndex=lepIndex) in x  ) or ( "{lepCol}_pdgId[{lepIndex}[0]]==13".format(lepCol=lepCol, lepIndex=lepIndex) in x  ) )) ,
                                   }
                           }})
        if ttpt:
            if ttpt=='2ttpt':
                ttptweight = "(1.24)*exp(0.156-0.5*0.00137*({top1pt}+{top2pt}))".format(top1pt="Max$(GenPart_pt*(GenPart_pdgId==6))" , top2pt="Max$(GenPart_pt*(GenPart_pdgId==-6))")
            else:
                ttptweight = "1.24*exp(0.156-0.5*0.00137*({top1pt}+{top2pt}))".format(top1pt="Max$(GenPart_pt*(GenPart_pdgId==6))" , top2pt="Max$(GenPart_pt*(GenPart_pdgId==-6))")
            weightDict['tt'] = {
                            "top_pt": ttptweight
                           }

        if isr:
            #isrWeightFunc = lambda norm: '(1.+{norm}*GenPart_mass[stopIndex1]) *(1.*(stops_pt<120.)+0.95*(stops_pt>=120.&&stops_pt<150.)+0.9*(stops_pt>=150.&&stops_pt<250.)+0.8*(stops_pt>=250.))'.format(norm=norm)
            #isrWeight = isrWeightFunc(9.5e-5)
            #isrWeightFunc = lambda norm: '(1.+{norm}*GenPart_mass[stopIndex1]) *(1.*(stops_pt<120.)+0.95*(stops_pt>=120.&&stops_pt<150.)+0.9*(stops_pt>=150.&&stops_pt<250.)+0.8*(stops_pt>=250.))'.format(norm=norm)
            #isrWeight = isrWeightFunc(9.5e-5)
            isrWeightString = "{normFact} * ( (nIsr==0) + (nIsr==1)*0.882  + (nIsr==2)*0.792  + (nIsr==3)*0.702  + (nIsr==4)*0.648  + (nIsr==5)*0.601  + (nIsr>=6)*0.515 ) "
            isrWeightFunc   = lambda normFact: isrWeightString.format( normFact=normFact )
            isrWeight       = isrWeightFunc("(7.279e-05 *(GenSusyMStop) + 1.108)")
            weightDict['scan'] = {
                                    'isrReweight' : isrWeight
                                 }


        #
        # def_weights (i.e weights common to all MC samples)
        #

        def_weights = {}

        def_weights['baseWeight']= "weight"

        if teff:
            trigeff = "{p0}*0.5*(1+TMath::Erf(({x}-{p1})/{p2}))".format( p0=0.980, p1=102.5, p2=90.76, x="met")
            def_weights['teff']=trigeff

        
        if pu:
            def_weights['pu']=pu

        if lumis:
            def_weights['lumis']=lumis

        if not btag.lower() == 'btag':
            btag_sf_map = BTagSFMap(btag)
            btag_to_sf  = btag_sf_map.btag_to_sf
            sf_to_btag  = btag_sf_map.sf_to_btag
            def_weights["cuts"]=dict( [ (sf, (sf, make_match_func(sf))  )  for sf in sf_to_btag.keys()  ])


        self.def_weights = def_weights
        self.weights={}
        for samp in weightDict:
            self.weights[samp]= Weight( weightDict[samp], self.def_weights )



        self.weightDict= weightDict
        self.def_weights = def_weights

        pass




default_weight_params = {
                         'btag'  : 'sf',
                         'lepCol': 'LepGood',
                         'lep'   : 'lep',
                         'lumis' : {
                                    'DataBlind_lumi': 12864.4,
                                    'DataUnblind_lumi': 804.2,
                                    'mc_lumi': 10000.0,
                                    'target_lumi': 13000.0
                                   },
                         'pu'    : 'puReweight',
                         'ttpt'  : '',
                         'isr'   : '',
                         'wpt'   : ''
                         }


weights_    = Weights(**default_weight_params)
weights     = weights_.weights
def_weights = weights_.def_weights


















"""
Branching Ratio reweight = 1.022  ,  
Pythia ignores the given SLHA BR for stop decay to leptons (vs taus) and uses equal BR of 10.8%.
The reweighting factor to come to 11.1% is 1.028 for one stop, and 1.022 for two stops.

"""

