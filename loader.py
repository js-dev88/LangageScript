import pandas as pd
import math

def loadModel(csv_name, type='excel'):
    """
    load a model from a csv or an excel file

    Args:
        args1: csv name if placed in the directory of the main class
        args2: type (excel or csv)
    Return:
        the parsed file in dataframes and list
    """
    if type == 'csv':
        df = pd.read_csv(csv_name) 
    elif type == 'excel':
        df = pd.read_excel(csv_name) 
        
    return parseDataframe(df)
      
def buildCriteriaBaremedf(df_criteria_list, df_bareme):
    
    df_criteria_bareme = df_criteria_list.copy()
    
    for criteria in df_criteria_list.iloc[:,1:]:
        df_criteria_bareme = pd.merge(df_criteria_bareme, df_bareme, how='left', left_on=criteria, right_on=['Note'])
        df_criteria_bareme = df_criteria_bareme.drop(['Note'],1)
        df_criteria_bareme = df_criteria_bareme.rename(columns={'Min_value': f'Min_value_{criteria}', 'Max_value': f'Max_value_{criteria}'})
    
    return df_criteria_bareme

def buildCoeffList(df):
    
    coeff = df['Coefficient']
    coeff_list = list()
    for c in coeff:
        if not math.isnan(c):
            coeff_list.append(c)
    return coeff_list

def parseDataframe(df):
    """
    parse the dataframe from the excel file in usefull compenents

    Args:
        args1: a Dataframe

    Return:
        score : the score column
        coeff_list : list of coefficient
        df_criteria_list : a sub dataframe with Produits and criterias columns
        df_criteria_bareme : a sub dataframe with the criterias columns and the boundaries of each value
    """
    
    score  = df['Score'].copy()
    coeff_list = buildCoeffList(df)
    df_bareme = df[['Note','Min_value','Max_value']].copy()
    df_criteria_list = df.drop(['Score', 'Coefficient','Note','Min_value','Max_value'], 1).copy()
    df_criteria_bareme = buildCriteriaBaremedf(df_criteria_list, df_bareme)
    
    return score, coeff_list, df_criteria_list, df_criteria_bareme
