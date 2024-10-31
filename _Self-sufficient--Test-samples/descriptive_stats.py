import pandas as pd
from collections import Counter
import json
import os

if __name__ == "__main__":

   # JY : Just manually truncated the top 2 non-header rows
   self_sufficient_csv_fpath = "/data/d1/jgwak1/tabby/SUNYIBM_ExplainableAI_2nd_Year_JY/JY_Progress_Directories/Command-Classification----Test-samples/_Self-sufficient--Test-samples/Self-Sufficient_technique-labeled_code-samples_20241031_0841am_VER.csv"
   
   self_sufficient_df = pd.read_csv( self_sufficient_csv_fpath )
   self_sufficient_df


   Counter(  self_sufficient_df['Code-sample'] )
   Counter(  self_sufficient_df['technique'] )
   Counter(  self_sufficient_df['tactic'] )

   tactic2codesample_dict =dict( self_sufficient_df.groupby("tactic")['Code-sample'].apply(list) )

   # See this 'technique2codesample_dict'
   technique2codesample_dict = dict( self_sufficient_df.groupby("technique")['Code-sample'].apply(list) )   

   # tactic2technique_dict =dict( self_sufficient_df.groupby("tactic")['technique'].apply(list) )

   script_directory = os.path.dirname(os.path.abspath(__file__))


   with open( os.path.join( script_directory , "tactic2codesample_dict.json"  ) , "w" ) as json_fp:
      json.dump( tactic2codesample_dict , json_fp )

   with open( os.path.join( script_directory , "technique2codesample_dict.json" ) , "w" ) as json_fp:
      json.dump( technique2codesample_dict , json_fp )

