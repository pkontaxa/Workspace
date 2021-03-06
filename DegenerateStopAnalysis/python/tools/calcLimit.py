#!/usr/bin/env python
"""
usage:
./calcLimit.py "path/to/card/pattern" path/to/output/pickle.pkl
usage: ./calc_cards_limit.py "../cutbased/cards/reload_scan_2200pbm1/Reload_Inc_T2_4bd*" ../cutbased/pkl/RunII_Reload_Scan_Limits_2260.pkl
"""


import glob
import os 


import pickle
import json

from optparse import OptionParser

import Workspace.DegenerateStopAnalysis.tools.limitTools as limitTools
import Workspace.DegenerateStopAnalysis.tools.degTools as degTools
import Workspace.HEPHYPythonTools.user as user


getFileName  = lambda f : os.path.splitext( os.path.basename(f) )[0] 

combineLocation = getattr(user, "combineLocation") 
if not combineLocation:
    raise Exception("This script only works within the Higgs combine limits tools framework \n\
                     Add the location for your combine limit setup in HEPHYPythonTools/python/user.py \n\
                    ")


def calcLimitAndStoreResults( card, output_dir = "./", output_name = None, exts =["pkl", "json"] , combineLocation = combineLocation, signif= False):
    res = limitTools.calcLimit( card , combineLocation = combineLocation, signif = signif)
    output_prefix = "Limit_" if not signif else "Signif_"
    card_file_name = getFileName(card)
    if not output_name:
        output_name = output_prefix + card_file_name  
    output_file = output_dir +"/" + output_name 
    for ext in exts:
        if ext=="pkl":
            pickle.dump( res, file( output_file +"."+ext, "w" ) )
            print "%s results for card %s, stored in %s"%(output_prefix.rstrip("_"), card_file_name , output_file+"."+ext)
        elif ext=="json":
            json.dump( res, file( output_file +".json", "w" ) , indent = 4)
            print "%s results for card %s, stored in %s"%(output_prefix.rstrip("_"), card_file_name , output_file+"."+ext)
        else:
            raise Exception("Output extention not recognized")
    return card_file_name, output_file+".pkl",  res
    



if __name__ == '__main__':



    parser = OptionParser()
   
    parser.add_option("--output_script", dest="output_script_name",
                  help="output script for the limit calculations", default="calc_all_limits.sh") 
    parser.add_option("--batch", action="store_true",
                  help="submit to batch",) 
    parser.add_option("--paral", action="store_true",
                  help="run interactively in paralel ", ) 

    parser.add_option("--signif", action="store_true",
                  help="calculate significance ", ) 

    (options,args) = parser.parse_args()
    
    output_script_name = options.output_script_name     
    
    card_pattern = args[0]
    if len(args) > 1:
        output_dir   = args[-1]
            
        if not output_dir.endswith("/"):
            raise Exception("Last argument should be the output directory ending with '/' but it  is %s"%output_dir)
        degTools.makeDir(output_dir)
    else:
         output_dir = "./"
    
    
    print card_pattern
    cards  = glob.glob(card_pattern)
    
    if not cards:
        raise Exception("No Cards Found with the pattern: %s"%card_pattern)
    
    
    calcLimitScript = "$CMSSW_BASE/src/Workspace/DegenerateStopAnalysis/python/tools/calcLimit.py"
    calcLimitScript = os.path.expandvars( calcLimitScript )

    single_card = len(cards)==1


    print "Found %s Cards"%len(cards)
    
 
    make_script = not single_card 
    signifopt = ' --signif ' if options.signif else ''
    # if one card is input the limit will be calculated
    # if a directory is input, then a scrip will be created for each card in the directory 
    if make_script:
        fname = output_script_name
        f = open( fname, "w")
        f.write("##\n")
    for card in cards:
        if make_script:
            command = "python {calcLimitScript}  {card}  {output_dir} {signifopt}".format(calcLimitScript = calcLimitScript , card=card, output_dir = output_dir, signifopt = signifopt) 
            f.write(command)
            f.write("\n")
        else:
            print ""
            card_file_name, output_file, res = calcLimitAndStoreResults( card, output_dir = output_dir, output_name = None, signif=options.signif)
    if make_script:
        f.close()
        batchcommand = "submitBatch.py %s   --title=Limits"%fname
        if options.batch:
            os.system( batchcommand )     
        elif options.paral:
            print batchcommand +"  --paral"
            os.system( batchcommand +"  --paral" )     
        else:
            print "\n \n script to be run: %s "%fname
            print batchcommand
            #f.close()


    if False: 
        limits = {}
        for card, limit in results:
            print card
            mstop, mlsp = getMasses(card)
            try: 
                limits[mstop]
            except KeyError:
                limits[mstop]={}
            limits[mstop][mlsp] = limit 
            
            
        
        
        
        
        if pkl_out.endswith(".pkl"):
            pass
        else:
            pkl_out +=".pkl"
        json_out = pkl_out.replace(".pkl",".json")
        
        print limits
        
        
        pickle.dump(limits,open(pkl_out,"w"))
        json.dump(limits, open(json_out,"w") , indent = 4)
        print "json and pickle written in  \n %s  \n %s"%(pkl_out, json_out)

