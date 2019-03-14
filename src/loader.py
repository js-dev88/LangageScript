import pandas as pd
import math

def loadModel(file_name, type='excel'):
    """
    Charge un model depuis un fichier excel ou csv.
    Le fichier excel doit respecter le format fournit en exemple

    Args:
        file_name: le nom du fichier placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
    Return:
        le fichier découpé selon les différents éléments
    """
    if type == 'csv':
        df = pd.read_csv(f'{file_name}')
    elif type == 'excel':
        df = pd.read_excel(f'{file_name}')
        
    return df

def parseDataframe(df):
    """
    Découpe le fichier en élements utiles

    Args:
        df: un DataFrame

    Return:
        df_score : la colonne score
        coeff_list : la liste des coefficients
        df_criteria_list : un Dataframe avec les colonnes produits 
            et les colonnes de critères
        df_criteria_bareme : un Dataframe avec les colonnes de critères
            et leurs bornes respectives por chaque lignes
        dict_boundaries : un Dict avec les valeurs min et max du barème
    """
    
    df_score  = df['Score'].copy()
    coeff_list = buildCoeffList(df)
    df_bareme = df[['Note','Min_value','Max_value']].copy()
    df_criteria_list = df.drop(['Score', 'Coefficient','Note','Min_value','Max_value'], 1).copy()
    df_criteria_bareme = buildCriteriaBaremedf(df_criteria_list, df_bareme)
    dict_boundaries = {}
    dict_boundaries['min'] = df_bareme['Min_value'].min()
    dict_boundaries['max'] = df_bareme['Max_value'].max()

    return df_score, coeff_list, df_criteria_list, df_criteria_bareme, dict_boundaries
      
def buildCriteriaBaremedf(df_criteria_list, df_bareme):
    """
    Pour chaque colonne de critères, rajoute les bornes min et max de 
        la valeur qualitative du critère
        
    Args:
        df_criteria_list: un DataFrame avec les valeurs quantitatives des critères
        df_bareme: un Dataframe avec les bornes min et max (le barème)
    
    Return: un Dataframe avec les colonnes de critères
            et leurs bornes respectives por chaque lignes
    """
    
    df_criteria_bareme = df_criteria_list.copy()
    
    for criteria in df_criteria_list.iloc[:,1:]:
        df_criteria_bareme = pd.merge(df_criteria_bareme, df_bareme, how='left', left_on=criteria, right_on=['Note'])
        df_criteria_bareme = df_criteria_bareme.drop(['Note'],1)
        df_criteria_bareme = df_criteria_bareme.rename(columns={'Min_value': f'Min_value_{criteria}', 'Max_value': f'Max_value_{criteria}'})
    
    return df_criteria_bareme

def buildCoeffList(df):
    """
    Récupère la liste des coefficients
        
    Args:
        df: Le Dataframe correspondant au fichier d'entrée
    
    Return: une liste de coefficient
    """
     
    coeff = df['Coefficient']
    coeff_list = []
    for c in coeff:
        if not math.isnan(c):
            coeff_list.append(c)
            
    return coeff_list


