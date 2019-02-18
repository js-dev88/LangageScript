"""
Created on Tue Feb 12 16:00:28 2019

@author: ayoubafrass
"""


import pandas as pd

def checkAdditiveModel(csv_name):
    mydict = pd.read_excel('input_CheckAdditive.xlsx') #pd.read_csv
    prod = mydict['Name']
    comp = mydict['Composition']
    perf = mydict['Performance ']
    score  = mydict['Score Global']
    
   
  
