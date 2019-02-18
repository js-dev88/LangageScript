import pandas as pd

def checkAdditiveModel(csv_name, type='excel'):
    if type == 'csv':
        mydict = pd.read_csv(csv_name) 
    elif type == 'excel':
        mydict = pd.read_excel(csv_name) 
    
    print(mydict)
    prod = mydict['Produit']
    print(prod)
    perf = mydict['Performance']
    print(perf)
    comp = mydict['Composition']
    print(comp)
    score  = mydict['Score']
    print(score)

checkAdditiveModel('input_couches.xlsx')    
   
  
