

import re
import pickle
from Workspace.DegenerateStopAnalysis.tools.degTools import natural_sort

def getBin(name):
    name = name[:name.index("to")]
    return int( re.split('_|-|Pt|HT', name)[-1] )

l = lambda x: int(re.split('_|-|to' ,x[0])[-2])



import os





def printSample(compName, comp, ext_comp= None):
    sampleName = "_".join(comp.dataset.split("/")[1:3])
    xsec = comp.xSection if not comp.isData else None
    ext_comp_string = '"ext":%s,'%ext_comp if ext_comp else ""
    isFastSim = '"isFastSim":True,' if getattr(comp,"isFastSim",False) else ""


    temp =\
"""

{compName} ={{
'cmgName':"{compName}",
"name" : "{sampleName}",
"chunkString":"{sampleName}",
"dir": sample_path +"/" + "{sampleName}",
"dbsName" : "{dbsName}",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": {isData},
"xsec": {xsec},
{ext_comp}
{isFastSim}
}}
allComponents.append({compName})

""".format(sampleName=sampleName, isData= comp.isData , dbsName = comp.dataset , xsec = xsec, compName = compName, ext_comp = ext_comp_string, isFastSim=isFastSim)
    #print temp
    return temp

def printCMGProcessingFile(     cmgPickle, 
                                mc_path      =  "/data/nrad/cmgTuples/%s/RunIISpring16MiniAODv2"    , 
                                data_path    =  "/data/nrad/cmgTuples/%s/Data25ns"    , 
                                output_dir  =   "$CMSSW_BASE/src/Workspace/DegenerateStopAnalysis/python/samples/cmgTuples/"    , 
                                write       =   True    ,
                           ):
    output_dir  = os.path.expandvars(output_dir)
    tag = os.path.splitext(os.path.basename(cmgPickle))[0]
    data_path = data_path%tag
    mc_path   = mc_path%tag
    componentDict = pickle.load(file(cmgPickle))
    data_output = []
    mc_output   = []
    data_output.append( "sample_path = '%s'   \nallComponents=[] \n"%data_path)
    mc_output.append(   "sample_path = '%s'   \nallComponents=[] \n"%mc_path)

    ## getting common datasets for extentions
    dataset_names = {}
    for compName, comp in componentDict.iteritems():
        dataset_name = comp.dataset.rsplit("/")[1]
        if dataset_name in dataset_names:
            dataset_names[dataset_name].append(compName)
        else:
            dataset_names[dataset_name] = [compName]


    debug = False
    if debug:
        return componentDict.keys()

    #exts =["_ext", "_ext1", "_ext2","_ext3" ]
    #for compName, comp in  sorted( componentDict.iteritems() ) :
    sorted_keys = natural_sort( componentDict.keys() ) 
    for compName  in  sorted_keys :
        comp = componentDict[compName]
        #print '------------------', compName
        ext_comps = []
        if not comp.isData:
            #ext = [ e for e in exts if compName.endswith(e) ]
            #print 'exts:', ext
            #if len(ext) > 1  :
            #    raise Exception("Unclear extention.... %s"%ext) 
            #else:
            #    ext = ext[0] if ext else ""
            #    
            ##if compName.endswith(ext):
            #print ext
            #if ext and compName.endswith(ext):
            #    print "this is an extention, with ", ext
            #    norm_compName = compName.replace(ext,"")
            #    if norm_compName in componentDict:
            #        ext_comps.append(compName)
            #        ext_comps.append(norm_compName)
            #elif ext and compName+ext in componentDict:
            #    print "this sample has an extention"
            #    ext_comps.extend([compName, compName+ext])
            dataset_name = comp.dataset.rsplit("/")[1]
            common_datasets = dataset_names[dataset_name]
            if len( common_datasets ) > 1 :
                ext_comps = common_datasets
            print '-------------' , compName
            print ext_comps
            mc_output.append( printSample(compName, comp , ext_comps)) 
        else:
            data_output.append( printSample(compName, comp)  )
    data_sample_file    = os.path.splitext(os.path.basename(data_path))[0]    
    mc_sample_file      = os.path.splitext(os.path.basename(mc_path))[0]      

    if len(data_output)>1:
        data_file_path = output_dir +"/%s.py"%data_sample_file
        data_file = open( data_file_path ,'w')
        for l in data_output:
            data_file.write(l)
        print "Data CMGProcessing sample file written to %s"%data_file_path
        data_file.close()
    if len(mc_output)>1:
        mc_file_path = output_dir +"/%s.py"%mc_sample_file
        mc_file = open( mc_file_path ,'w')
        for l in mc_output:
            mc_file.write(l)
        mc_file.close()
        print "MC CMGProcessing sample file written to %s"%mc_file_path
    return {'data': data_output, 'mc':mc_output }


if __name__ == '__main__':

    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_20/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8020_mAODv2_v0.pkl"
    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_20/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8020_mAODv2_v5.pkl"
    cmgPickle = "/afs/cern.ch/work/n/nrad/CMSSW/CMSSW_8_0_25/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8025_mAODv2_v7_1.pkl"
    cmgPickle = "/afs/cern.ch/work/n/nrad/CMSSW/CMSSW_8_0_25/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8025_mAODv2_v7.pkl"
    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_20/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8020_mAODv2_OldJetClean_v2.pkl"
    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_12/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8012_mAODv2_v3_1.pkl"
    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_11/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8011_mAODv2_v1_1.pkl"
    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_12/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/8012_mAODv2_v0.pkl"
    #cmgPickle = "/afs/cern.ch/user/n/nrad/CMSSW/CMSSW_8_0_11/src/CMGTools/SUSYAnalysis/cfg/crab_with_das/mAODv2_v1_1.pkl" 
    out = printCMGProcessingFile(cmgPickle)

