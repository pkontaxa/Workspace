# baselineSamplesInfo.py
# Baseline Lumis, Triggers (Filters), Cuts and Weight Options
import Workspace.DegenerateStopAnalysis.tools.degTools as degTools
### Samples Names ###
sample_names = {
                    'vv': "VV",
                    #'z':  '#{Z\rightarrow \nu\nu+jets}',
                    'z':  'Z#rightarrow#nu#nu+jets', 
                    'st': 'Single top',
                    #'dy': '#{Z/\gamma^{*} +jets}',
                    'dy': 'Z#gamma*+jets',
                    'w' :  'WJets',
                    'tt': 'TTJets',
                   'ttx': 'ttX',
                   #'ttx': 'TTX',
                   #'ttx': 'TTX',
                }

sample_names_db = {
                'allSignal'  : {'latexName': "allSignal",                       'niceName':'allSignal',      },#'shortName':'vv'     },     
                'Total'  : {'latexName': "Total",                       'niceName':'Total',      },#'shortName':'vv'     },     
                'others' : {'latexName': "Rare",                      'niceName':'Others',     },#'shortName':'vv'     },     
                'fakes'  : {'latexName': "Nonprompt",                       'niceName':'Fakes',      },
                'data'   : {'latexName': "Data",                        'niceName':'Data',       },
                    'vv' : {'latexName': "VV",                          'niceName':'VV',         },#'shortName':'vv'     },     
                    'z'  : {'latexName': 'Z#rightarrow#nu#nu+jets', 'niceName':'ZInv',       },#'shortName':'z'      },     
                    'st' : {'latexName': 'Single top',                  'niceName':'Single top', },#'shortName':'st'     }, 
                    'dy' : {'latexName': 'Z#gamma*+jets',        'niceName':'DY',         },#'shortName':'dy'     },
                    'w'  : {'latexName': 'W+jets',                       'niceName':'WJets',      },#'shortName':'w'      },     
                    'tt' : {'latexName': 't#bar{t}',                      'niceName':'TTJets',     },#'shortName':'tt'     },                        'tt_1l': {'latexName': 'TT_1l',                      'niceName':'TT_1l',    },# 'shortName':'tt_1l'    },     
                 'tt_1l' : {'latexName': 't#bar{t}(1l)',                       'niceName':'TT_1l',      },# 'shortName':'tt_1l'    },     
                 'tt_2l' : {'latexName': 't#bar{t}(1l)',                       'niceName':'TT_2l',      },# 'shortName':'tt_2l'    },     
                'tt_pow' : {'latexName': 'TT_Pow',                      'niceName':'TT_Pow',     },#    'shortName':'tt_pow' },     
                  'ttx'  : {'latexName': 'ttX',                         'niceName':'ttX',       },#'shortName':'qcd'    },      
                   'qcd' : {'latexName': 'QCD',                         'niceName':'QCD',        },#'shortName':'qcd'    },      
                  't2tt' : {'latexName': 'T2tt',                        'niceName':'T2tt_',       },#'shortName':'qcd'    },      
                  't2bw' : {'latexName': 'T2bW',                        'niceName':'T2bW_',       },#'shortName':'qcd'    },      
                
                'hino'  : {'latexName': 'Hino' , 'niceName':'Hino_', } ,
                'n2c1h' : {'latexName': 'N2C1' , 'niceName':'N2C1H_', } ,
                'c1c1h' : {'latexName': 'C1C1' , 'niceName':'C1C1H_', } ,
                'c1n1h' : {'latexName': 'C1N1' , 'niceName':'C1N1H_', } ,
                'n2n1h' : {'latexName': 'N2N1' , 'niceName':'N2N1H_', } ,
                'tchiwz': {'latexName': 'TChiWZ', 'niceName':'TChiWZ_', } ,

                 }

for vv in [ 'vvinc','vv2', 'ww','zz','wz','wwNLO','wzNLO','zzNLO']:
    sample_names_db[vv]= {'latexName':vv.upper(), 'niceName':vv.upper() }






for short_name, sample_name_db in sample_names_db.items():
    sample_name_db['shortName'] = short_name

data_sets_info = [\
           ['DataBlind',  ['B','C','D','E','F','G','H'], {'latexName':'',   'shortName':'dblind',   'niceName':'DataBlind'} ],
           ['DataICHEP',  ['B','C','D']                , {'latexName':'',   'shortName':'dichep',   'niceName':'DataICHEP'} ],
           ['DataBCDE',   ['B','C','D','E']            , {'latexName':'',   'shortName':'dbcde',    'niceName':'DataBCDE' } ],
           ['DataBCDEF',  ['B','C','D','E','F']        , {'latexName':'',   'shortName':'dbcdef',   'niceName':'DataBCDEF'} ],
           ['DataGH',     ['G', 'H']                   , {'latexName':'',   'shortName':'dgh',      'niceName':'DataGH'   } ],
         ]

def sampleName( name, name_opt="niceName", verbose = False):
    """
    name_opt should be one of ['niceName', 'latexName', 'shortName']
    """
    orig_name = name[:] 
    isSignal = degTools.getMasses( name, returnModel = True ) 
    if isSignal:
        model, m1, m2 = isSignal
        name = model

    possibleNames = {}
    for n , ndict in sample_names_db.iteritems():
        possibleNames[n] = ndict.values()
    foundIt = False 
    for n, pNames in possibleNames.iteritems():
        if name in pNames:
            if foundIt:
                raise Exception("found multiple matches to the name %s"%name)
            foundIt = n
    if not foundIt:
        raise Exception("Did not find a sample corresponding to: %s"%name)
    wantedName = sample_names_db[foundIt][name_opt]
    if isSignal:
        wantedName = "%s%s_%s"%( wantedName, m1, m2 )
        wantedName = wantedName.replace(".","p")
    if verbose: print "choose", wantedName, " for ", orig_name
    return wantedName


### Luminosities ###
# bril calc res : /afs/cern.ch/user/n/nrad/public/bril_res/8025_mAODv2_v7/lumis.pkl

lumis = {
            #'DataBlind_lumi':           35854.9, #8025_v7: 35854.9 #8020_v5: 35628.7, # NOTE: calculated with getDataRunsLumi
            'SingleMuDataBlind_lumi':   35808.7, #8025_v7: 35808.6 #8020_v5: 36809.6 
            'SingleElDataBlind_lumi':   35725.2, #8025_v7: 35725.2 #8020_v5: 36726.8
            'SingleLepDataBlind_lumi':  35767.0,
            'JetHTDataBlind_lumi':      35865.2, #8025_v7: 35865.2 #8020_v5: 33781.6 
            'DataBlind_lumi':           35854.9 , #8020_v5: 35628.7, # NOTE: calculated with getDataRunsLumi
            'SingleMuDataBlind_lumi':   35808.6 , #8020_v5: 36809.6 
            'SingleElDataBlind_lumi':   35725.18, #8020_v5: 36726.8
            'SingleLepDataBlind_lumi':  36800.0,
            'JetHTDataBlind_lumi':      33781.6, #NOTE: 8020_v5
            #'DataICHEP_lumi':           12864.4,
            'DataUnblind_lumi':         4303.0,
            'SingleMuDataUnblind_lumi': 4303.0,
            'SingleElDataUnblind_lumi': 4303.0,
            'JetHTDataUnblind_lumi':    4303.0,
            'MC_lumi':                  10000.0, #NOTE: Should be taken directly from samples
        }

lumis['target_lumi'] = lumis['DataBlind_lumi']

data_runs_sep23 = {
                 'B': {'lumi': 5667.931          , 'runs': ('272007', '275376')},
                 'C': {'lumi': 2638.567          , 'runs': ('275657', '276283')},
                 'D': {'lumi': 4353.448          , 'runs': ('276315', '276811')},
                 'E': {'lumi': 3204.684          , 'runs': ('276831', '277420')},
                 'F': {'lumi': 3185.971          , 'runs': ('277772', '278808')},
                 'G': {'lumi': 7721.057          , 'runs': ('278820', '280385')},
                 'H': {'lumi': 8635.591 + 221.442, 'runs': ('280919', '284044')}
                }

data_met_feb03 = {
                 'B' : { 'lumi': 5787.968           , 'runs': ('272007', '275376')  }, 
                 'C' : { 'lumi': 2573.399           , 'runs': ('275657', '276283')  }, 
                 'D' : { 'lumi': 4248.384           , 'runs': ('276315', '276811')  }, 
                 'E' : { 'lumi': 4008.663           , 'runs': ('276831', '277420')  }, 
                 'F' : { 'lumi': 3101.618           , 'runs': ('277772', '278808')  }, 
                 'G' : { 'lumi': 7529.196           , 'runs': ('278820', '280385')  }, 
                 'H' : { 'lumi': 8390.540 + 215.149 , 'runs': ('280919', '284044')  }, 
                  }

data_runs = data_met_feb03

#data_runs = {
#                 'B': {'lumi': 5891.727, 'runs': ('272007', '275376')},
#                 'C': {'lumi': 2645.968, 'runs': ('275657', '276283')},
#                 'D': {'lumi': 4353.448, 'runs': ('276315', '276811')},
#                 'E': {'lumi': 4049.255, 'runs': ('276831', '277420')},
#                 'F': {'lumi': 3160.088, 'runs': ('277772', '278808')},
#                 'G': {'lumi': 7554.453, 'runs': ('278820', '280385')},
#                 'H': {'lumi': 8761.821, 'runs': ('280919', '284044')}
#                }

def getDataRunsLumi( runs, data_runs = data_runs) :
    lumi = sum([data_runs[x]['lumi'] for x in runs] )
    return round(lumi,1)

def getDataRunCut( runs, data_runs=data_runs):
    run_cut_list = []
    for run in runs:
        run_cut_list.append(run_cut)
    run_cuts = " || ".join(run_cut_list)
    return "(%s)"%run_cuts

make_lumi_tag = lambda l: "%0.0fpbm1"%(l)

def makeLumiTag(lumi , latex=False ):
    """ lumi given in pb """
    if latex:
        tag = "%0.1ffb^{-1}"%(lumi/1000.)
    else:
        tag = "%0.1ffbm1"%(lumi/1000.)
    return tag

for dataset_name, runs , name_dict, in data_sets_info:
    lumi = getDataRunsLumi(runs, data_runs)
    lumis[dataset_name+"_lumi"] = lumi
    latexBaseName = name_dict['latexName'] if name_dict['latexName'] else 'Data' 
    name_dict['latexName']=latexBaseName+"(%s)"%makeLumiTag(lumi,latex=True)
    sample_names_db[name_dict['shortName']] = name_dict
#sample_names_db['d'] = {'latexName':'Data(%s)'%makeLumiTag( lumis['DataUnblind_lumi'],latex=False), 'shortName':'d', 'niceName':'DataUnblind' }
sample_names_db['d'] = {'latexName':'Data', 'shortName':'d', 'niceName':'DataUnblind' }

# Setting target lumi to data lumi
lumis['target_lumi'] = lumis['DataBlind_lumi']

### Baseline Filters ###

filters = "Flag_Filters" #NOTE: Combination of filters as defined in post-processing

### Baseline Triggers ###
triggers = {}

triggers['data_met'] = [ # MET PD
                      'HLT_PFMET100_PFMHT100_IDTight',
                      'HLT_PFMET110_PFMHT110_IDTight',
                      'HLT_PFMET120_PFMHT120_IDTight',
                      'HLT_PFMET90_PFMHT90_IDTight'
                       ]

triggers['data_mu'] = "HLT_Mu50" # non-isolated trigger for SingleMu PD 
triggers['data_mu2'] = "HLT_IsoMu24" # SingleMu PD

triggers['data_el'] = "HLT_Ele27_WPTight_Gsf" # SingleEl PD

triggers['data_lep'] = [triggers['data_mu2'], triggers['data_el']]

triggers['data_jet'] = [ # JetHT PD
                      "HLT_PFHT800", 
                      "HLT_PFJet450", 
                      "HLT_AK8PFJet450"
                       ]

for trig in triggers:
   if type(triggers[trig]) == type([]):
      triggers[trig] = '(' + ' || '.join(triggers[trig]) + ')' #NOTE: assuming we always want to use an 'OR' of triggers

### Cuts and Weights Options ###
cutWeightOptions = {}
cutWeightOptions['options']     = ['isr_sig', 'sf', 'STXSECFIX', 'pu', 'isr_tt', 'wpt', 'trig_eff']
cutWeightOptions['def_weights'] = ['weight', 'DataBlind_lumi']
cutWeightOptions['settings'] = {
            'lepCol':    "LepGood",
            'lep':       "lep",
            'lepTag':    "lowpt",
            'tightWP':   "",
            'jetTag':    "def",
            'btagSF':    "SF",
            'mvaId':     None,
            'bdtcut_sr': None,
            'bdtcut_cr': None,
            'lumis' :    lumis,
        }

###
lhe_order = {
                'Q2central_central':'Q2central_central'   ,     ## <weight id="1001"> muR=1 muF=1 
                'Q2central_up'     :'Q2central_up'        ,     ## <weight id="1002"> muR=1 muF=2 
                'Q2central_down'   :'Q2central_down'      ,     ## <weight id="1003"> muR=1 muF=0.5 
                'Q2up_central'     :'Q2up_central'        ,     ## <weight id="1004"> muR=2 muF=1 
                #'Q2up_up'          :'Q2up_up'             ,     ## <weight id="1005"> muR=2 muF=2 
                'Q2up_down'        :'Q2up_down'           ,     ## <weight id="1006"> muR=2 muF=0.5 
                'Q2down_central'   :'Q2down_central'      ,     ## <weight id="1007"> muR=0.5 muF=1 
                'Q2down_up'        :'Q2down_up'           ,     ## <weight id="1008"> muR=0.5 muF=2 
                #'Q2down_down'      :'Q2down_down'         ,     ## <weight id="1009"> muR=0.5 muF=0.5 
              }



import collections
weight_choices = collections.OrderedDict()
weight_choices['nohiwgt']   =  { 'weight_name' : 'nohiwgt'  , 'tag': 'NoHiWgt'  , 'isWeightOpt' : True     }
weight_choices['sf']        =  { 'weight_name' : 'sf'       , 'tag': 'SF'      , 'isWeightOpt' : True     , 'isInSettings':{'btagSF':'SF'           }}
weight_choices['sf_l_up']   =  { 'weight_name' : 'sf'       , 'tag': 'SF_L_Up' , 'isWeightOpt' : True     , 'isInSettings':{'btagSF':'SF_l_Up'      }}
weight_choices['sf_l_down'] =  { 'weight_name' : 'sf'       , 'tag': 'SF_L_Down', 'isWeightOpt' : True    , 'isInSettings':{'btagSF':'SF_l_Down'    }}
weight_choices['sf_b_up']   =  { 'weight_name' : 'sf'       , 'tag': 'SF_b_Up' , 'isWeightOpt' : True     , 'isInSettings':{'btagSF':'SF_b_Up'      }}
weight_choices['sf_b_down'] =  { 'weight_name' : 'sf'       , 'tag': 'SF_b_Down', 'isWeightOpt' : True    , 'isInSettings':{'btagSF':'SF_b_Down'    }}
weight_choices['sf_fs_up']  =  { 'weight_name' : 'sf'       , 'tag': 'SF_FS_Up' , 'isWeightOpt' : True    , 'isInSettings':{'btagSF':'SF_FS_Up'     }}
weight_choices['sf_fs_down']=  { 'weight_name' : 'sf'       , 'tag': 'SF_FS_Down', 'isWeightOpt' : True   , 'isInSettings':{'btagSF':'SF_FS_Down'   }}
weight_choices['noisrsig']  =  { 'weight_name' : 'isr_sig'   , 'tag': 'NoSigIsr'  , 'isWeightOpt' : True }
weight_choices['prompt']    =  { 'weight_name' : 'prompt'   , 'tag': 'Prompt'  , 'isWeightOpt' : True }
weight_choices['STXSECFIX'] =  { 'weight_name' : 'STXSECFIX', 'tag': 'STXSECFIX' , 'isWeightOpt' : True }
weight_choices['pu']        =  { 'weight_name' : 'pu'       , 'tag': 'PU'      , 'isWeightOpt' : True }
weight_choices['pu_up']     =  { 'weight_name' : 'pu_up'    , 'tag': 'PU_Up'   , 'isWeightOpt' : True }
weight_choices['pu_down']   =  { 'weight_name' : 'pu_down'  , 'tag': 'PU_Down' , 'isWeightOpt' : True }
weight_choices['nvtx_gt_20']  =  { 'weight_name' : 'nvtx_gt_20' , 'tag': 'NVTX_GT_20' , 'isWeightOpt' : True }
weight_choices['nvtx_lt_20']  =  { 'weight_name' : 'nvtx_lt_20' , 'tag': 'NVTX_LT_20' , 'isWeightOpt' : True }
weight_choices['isr_tt']    =  { 'weight_name' : 'isr_tt'   , 'tag': 'TTIsr'   , 'isWeightOpt' : True }
weight_choices['wpt'   ]    =  { 'weight_name' : 'wpt'      , 'tag': 'Wpt'     , 'isWeightOpt' : True }
weight_choices['trig_eff']  =  { 'weight_name' : 'trig_eff' , 'tag': 'TrigEff' , 'isWeightOpt' : True }
weight_choices['trig_mc']   =  { 'weight_name' : 'trig_mc'  , 'tag': 'TrigMC'  , 'isWeightOpt' : True }
#weight_choices['lepsf']     =  { 'weight_name' : 'lepsf'    , 'tag': 'lepSF'   , 'isWeightOpt' : True }
#weight_choices['lepsftot']  =  { 'weight_name' : 'lepsftot' , 'tag': 'lepSFTot'   , 'isWeightOpt' : True }
weight_choices['lepsffix']  =  { 'weight_name' : 'lepsffix' , 'tag': 'lepSFFix'   , 'isWeightOpt' : True }
weight_choices['medmu']  =  { 'weight_name' : 'medmu' , 'tag': 'MediumMu'   , 'isWeightOpt' : True }
weight_choices['genmet']    =  { 'weight_name' : ''   , 'tag': 'GenMet'  , 'isWeightOpt' : False   , 'isInSettings':{'corrs':'genMet'          }}
weight_choices['jec_up']    =  { 'weight_name' : ''   , 'tag': 'JEC_Up'  , 'isWeightOpt' : False   , 'isInSettings':{'corrs':'jec_up'          }}
weight_choices['jec_central']    =  { 'weight_name' : ''   , 'tag': 'JEC_Central'  , 'isWeightOpt' : False   , 'isInSettings':{'corrs':'jec_central'          }}
weight_choices['jec_down']  =  { 'weight_name' : ''   , 'tag': 'JEC_Down', 'isWeightOpt' : False   , 'isInSettings':{'corrs':'jec_down'        }}
weight_choices['jer_up']    =  { 'weight_name' : ''   , 'tag': 'JER_Up'  , 'isWeightOpt' : False   , 'isInSettings':{'corrs':'jer_up'          }}
weight_choices['jer_central']    =  { 'weight_name' : ''   , 'tag': 'JER_Central'  , 'isWeightOpt' : False   , 'isInSettings':{'corrs':'jer_central'          }}
weight_choices['jer_down']  =  { 'weight_name' : ''   , 'tag': 'JER_Down', 'isWeightOpt' : False   , 'isInSettings':{'corrs':'jer_down'        }}

for lheWeight, shortName in lhe_order.items():
    weight_choices[shortName] = { 'weight_name':lheWeight , 'tag':lheWeight, 'isWeightOpt':True}
    


def evalInputWeights( weights_input,  lumiWeight , weight_choices = weight_choices):
    good_weights  = [weight_choices[w] for w in weights_input ] # just to make sure no bad weights given
    weight_list   = [w for w in weight_choices if w in weights_input ]  # keeping the order of weight_choices
    
    weight_tag_list = []
    weight_opts     = []
    
    def_weights = ['weight'  , lumiWeight ]
    options     = [ 'isr_sig' ]
    settings_update = {} 

    for w in weight_list:       # split into options or def_weights
        wname = weight_choices[w]['weight_name']
        if weight_choices[w].get('isInSettings'):
            new_setting = weight_choices[w]['isInSettings']
            assert len( new_setting.keys() + settings_update.keys() ) == len( set ( new_setting.keys() + settings_update.keys()  )) ## make sure no dupblicate settings
            settings_update.update( new_setting ) 
        if weight_choices[w].get( 'isWeightOpt'):
            weight_opts.append( wname )
            if w=='noisrsig':
                options.remove(wname)
            elif wname not in options: 
                options.append( wname)
        else:
            if wname  not in def_weights:
                def_weights.append( wname  )
        weight_tag_list.append( weight_choices[w]['tag'] )
      
    def_weights = filter( lambda x: x , def_weights )
    weight_tag = "_".join(wgt for wgt in weight_tag_list if wgt)
    return {
            'weight_tag'      : weight_tag , 
            'weight_tag_list' : weight_tag_list, 
            'def_weights'     : def_weights, 
            'options'         : options, 
            'settings_update' : settings_update,
           }
