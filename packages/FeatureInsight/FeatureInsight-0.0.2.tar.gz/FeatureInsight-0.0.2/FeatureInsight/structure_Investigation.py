from sklearn.pipeline import Pipeline
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import os
from PIL import Image
import cv2
from tqdm import tqdm
from tabulate import tabulate
#import klib
import dask.dataframe as dd
from feature_engine.encoding import *
def struct_Investigation(df): 
   """plot Overview Information about datatype, variable type, shape, examples
   Detailed explanation 
   Args:  
       df: train in dataframe
       img: ['img1','img1'] the image feature name
   Returns:
      nothing

   """       
   try:
     df.img_listf
   except:
     df.img_list=[]
   print("There are {} instances, {} cols in total".format(df.iloc[:,0].count(),df.iloc[0,:].count()))
   info = pd.DataFrame( columns=["variable","dtype","measure_scales","Unique Count","Null Count","thumbnail"])
   info.variable=df.columns
   info=info.set_index('variable')

   # info.i=df.dtype
   for fea in list(df.columns):
       info.loc[fea,"Null Count"]=str(df[fea].isnull().sum())+"("+str(df[fea].isnull().sum()/df[fea].shape[0]*100)+"%)"
       info.loc[fea,"dtype"]=str(df[fea].dtypes)         
       if str(df[fea].dtypes)=='object':
           info.loc[fea,"dtype"]=str(set([type(x).__name__ for x in df[fea]]))    
       #info.i=df.shape
       #info.loc[fea,"shape"]=list(set([x.shape for x in df[fea]]))    


       if isinstance(info.loc[fea,"dtype"],list):
           print("Feature(s) includes more than one datatype, please do cleaning first")
           info.loc[fea,"measure_scales"]="Unknown"

       elif fea in df.img_list:
           info.loc[fea,"measure_scales"]="Image_address"

       elif type(df[fea].sample(1).tolist()[0])==str:
           info.loc[fea,"thumbnail"]=str(df[fea].sample(3).tolist())
           if len(str(df[fea].sample(1).tolist()[0]).split())>1:
               info.loc[fea,"measure_scales"]="Text"
           else:
               info.loc[fea,"measure_scales"]="Categorical Data"

       elif np.isreal(df[fea].sample(1).tolist()[0]):
           info.loc[fea,"thumbnail"]=str(df[fea].sample(3).tolist())
           if df[fea].nunique()/df[fea].count()<0.1 or df[fea].count()<100:
               info.loc[fea,"measure_scales"]="Categorical Data"
           else:
               info.loc[fea,"measure_scales"]="numerical Data"

       else:  
           info.loc[fea,"measure_scales"]="others"

       #info.i=df.cardinality
       info.loc[fea,"Unique Count"]= str(df[fea].nunique())+ "({p:.2f}%) of total".format(p=df[fea].nunique()/df[fea].count()*100)
   print(tabulate(info, headers='keys', tablefmt='psql'))
   return info
   