from loader import loadModel, parseDataframe
import numpy as np


def comparesTo(a,b): # cette fonction retourne "True" quand a >= b sinon elle retourne "False"
    """
    Compare deux notes a et b 
    
    Args : notes a et b que nous souhaitons comparer
    Return : un booléen valant True/1 si a est supérieur à b sinon il retourne False/0
    
    """
    comparator=0
    if(a[0]=="+" and b[0]=="+" and len(a)>=len(b)):
        comparator=1
    elif(a[0]=="+" and b[0]=="-"):
        comparator=1
    elif(a[0]=="-" and b[0]=="-" and len(a)<=len(b)): 
        comparator=1
    else: 
        comparator=0
        
    return comparator

 
def ConcordancePartielleHbi(csv_name,direction,type='excel'):
    """
    Calcule la matrice de concordance partielle entre les produits et les profils selon le nombre de critères
    
    Args : 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : la matrice de concordance partielle (H,bi)
    
    """
    df = loadModel(csv_name, type)
    _ , _, df_criteria_list, _, _, df_criteria_profils, _, _ = parseDataframe(df)  
    nb_criteria=len(df_criteria_list.columns) #nb de critères
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    
    listHbi = [] #Liste qui va contenir toutes les matrices de concordance créées
    
    if(direction=="max"):
        
        for z in range(1,nb_criteria):
            concMatrixHbi = np.zeros((nb_produits, nb_profils),dtype=int) #Matrice de concordance (H,bi)
            criteria = df_criteria_list.iloc[:,[z]]
            profilCriteria = df_criteria_profils.iloc[:,[z]]
            
            for i in range(0,nb_produits):
                 for j in range(0,nb_profils):
                    concMatrixHbi[i,j]= comparesTo(criteria.values[i,0], profilCriteria.values[j,0])

            listHbi.append(concMatrixHbi)
      
    elif(direction=="min"):
        
         for z in range(1,nb_criteria):
             criteria = df_criteria_list.iloc[:,[z]]
             profilCriteria = df_criteria_profils.iloc[:,[z]]
             concMatrixHbi = np.zeros((nb_produits, nb_profils),dtype=int) #Matrice de concordance (H,bi)
             for i in range(0,nb_produits):
                 for j in range(0,nb_profils):
                     concMatrixHbi[i,j]= comparesTo(profilCriteria.values[j,0],criteria.values[i,0])
             listHbi.append(concMatrixHbi) 
          
    return listHbi
                
def ConcordancePartiellebiH(csv_name,direction,type='excel'):
    """
    Calcule la matrice de concordance partielle entre les profils et les produits par nombre de critères
    
    Args : 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : la matrice de concordance partielle (bi,H)
    
    """
    df = loadModel(csv_name, type)
    _ , _, df_criteria_list, _, _, df_criteria_profils, _, _ = parseDataframe(df)  
    nb_criteria=len(df_criteria_list.columns) #nb de critères
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    listbiH = [] #Liste qui va contenir toutes les matrices de concordance créées


    if(direction=="max"):
        for z in range(1,nb_criteria):
            concMatrixbiH = np.zeros((nb_profils, nb_produits),dtype=int) #Matrice de concordance (bi,H)
            criteria = df_criteria_list.iloc[:,[z]]
            profilCriteria = df_criteria_profils.iloc[:,[z]]
            
            for j in range(0,nb_profils):
                 for i in range(0,nb_produits):
                    concMatrixbiH[j,i]= comparesTo(profilCriteria.values[j,0], criteria.values[i,0])

            listbiH.append(concMatrixbiH) 
      
    elif(direction=="min"):
        for z in range(1,nb_criteria):
            concMatrixbiH = np.zeros((nb_profils, nb_produits),dtype=int) #Matrice de concordance (bi,H)
            criteria = df_criteria_list.iloc[:,[z]]
            profilCriteria = df_criteria_profils.iloc[:,[z]]
            
            for j in range(0,nb_profils):
                for i in range(0,nb_produits):
                    concMatrixbiH[j,i]= comparesTo(criteria.values[i,0],profilCriteria.values[j,0])
            listbiH.append(concMatrixbiH) 
    
    return listbiH              
                
                
def ConcordonceGlobaleHbi(csv_name,direction,type='excel'):
    """
    Calcule la matrice de concordance globale entre les profils et les produits 
    
    Args : 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : la matrice de concordance globale (bi,H)
    
    """
    df = loadModel(csv_name, type)
    _ ,coeff_list, df_criteria_list, _, _, df_criteria_profils, _, _ = parseDataframe(df) 
    nb_criteria=len(df_criteria_list.columns)-1 #nb de critères
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    listHbi=ConcordancePartielleHbi(csv_name,direction,type='excel')
    globalMatrixHbi = np.zeros((nb_produits, nb_profils),dtype=float) #Matrice de concordance globale (H,bi)

    sum_weight=0.0
    
    for z in range(nb_criteria):
        sum_weight+=coeff_list[z]
    
    for i in range(0,nb_produits):
        for j in range(0,nb_profils): 
            for k in range(0,nb_criteria):
                globalMatrixHbi[i,j] += (coeff_list[k]*listHbi[k][i][j])/sum_weight
                
    return globalMatrixHbi
    

def ConcordonceGlobalebiH(csv_name,direction,type='excel'):
    """
    Calcule la matrice de concordance globale entre les profils et les produits
    
    Args : 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : la matrice de concordance globale (bi,H)
    
    """
    df = loadModel(csv_name, type)
    _ ,coeff_list, df_criteria_list, _, _, df_criteria_profils, _, _ = parseDataframe(df) 
    nb_criteria=len(df_criteria_list.columns)-1 #nb de critères
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    listbiH=ConcordancePartiellebiH(csv_name,direction,type='excel')
    globalMatrixbiH = np.zeros((nb_profils,nb_produits),dtype=float) #Matrice de concordance globale (bi,H)

    sum_weight=0.0
    
    for z in range(nb_criteria):
        sum_weight+=coeff_list[z]

    for j in range(0,nb_profils):
        for i in range(0,nb_produits): 
            for k in range(0,nb_criteria):
                globalMatrixbiH[j,i] += (coeff_list[k]*listbiH[k][j][i])/sum_weight
                
    return globalMatrixbiH   


def SurclassementHbi(lamda,csv_name,direction,type='excel'):
    """
    Calcule la matrice de surclassement entre les produits et les profils
    
    Args : 
        lamda : le seuile de majorité
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : la matrice de surclassement (H,bi)
    
    """
    df = loadModel(csv_name, type)
    _ ,_, df_criteria_list, _, _, df_criteria_profils, _, _ = parseDataframe(df) 
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    
    globalMatrixHbi = ConcordonceGlobaleHbi(csv_name,direction,type='excel') 
    SurcHbi = np.zeros((nb_produits, nb_profils),dtype=int) 
    
    for i in range(0,nb_produits):
        for j in range(0,nb_profils):
            SurcHbi[i,j]= globalMatrixHbi[i,j]>=lamda
            
    return SurcHbi

def SurclassementbiH(lamda,csv_name,direction,type='excel'):
    """
    Calcule la matrice de surclassement entre les profils et les produits
    
    Args : 
        lamda : le seuile de majorité
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : la matrice de surclassement (bi,H)
    
    """
    df = loadModel(csv_name, type)
    _ ,_, df_criteria_list, _, _, df_criteria_profils, _, _ = parseDataframe(df) 
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    
    globalMatrixbiH = ConcordonceGlobalebiH(csv_name,direction,type='excel') 
    SurcbiH = np.zeros((nb_profils,nb_produits),dtype=int) 
    
    for j in range(0,nb_profils):
        for i in range(0,nb_produits):
            SurcbiH[j,i]= globalMatrixbiH[j,i]>=lamda
            
    return SurcbiH           

             
def EvaluationPessimiste(lamda,csv_name,direction,type='excel'):
    """
    Applique l'évaluation pessimiste sur les matrices de surclassement
    
    Args : 
        lamda : le seuil de majorité 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : une liste d'affecation de catégories aux données 
    
    """
    df = loadModel(csv_name, type)
    _ ,_, df_criteria_list, _, _, df_criteria_profils, _, categories = parseDataframe(df) 
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    SurcHbi=SurclassementHbi(lamda,csv_name,direction,type='excel')
    AffectationPessimiste=[]
    
    
    for i in range(0,nb_produits):
        for j in range(0,nb_profils):
            if SurcHbi[i,j]==0:
                continue
            elif SurcHbi[i,j]==1 and j==0: 
                AffectationPessimiste.append(categories.get("C"+str(5)))
                break
            else:
                AffectationPessimiste.append(categories.get("C"+str(6-j)))
                break
    
    return AffectationPessimiste

def EvaluationOptimiste(lamda,csv_name,direction,type='excel'):
    """
    Applique l'évaluation optimiste sur les matrices de surclassement
    
    Args : 
        lamda : le seuil de majorité 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : une liste d'affecation de catégories aux données 
    
    """
    df = loadModel(csv_name, type)
    _ ,_, df_criteria_list, _, _, df_criteria_profils, _, categories = parseDataframe(df) 
    nb_produits=len(df_criteria_list) #nombre de produits
    nb_profils=len(df_criteria_profils) #nombre de profils
    SurcHbi=SurclassementHbi(lamda,csv_name,direction,type='excel')
    SurcbiH=SurclassementbiH(lamda,csv_name,direction,type='excel')
    AffectationOptimiste=[]
    
    
    for i in range(0,nb_produits):
       for j in range(0,nb_profils):
            if SurcbiH[5-j,i]==0:
                continue
            elif SurcbiH[5-j,i]==1 and SurcHbi[i,5-j]==0:
                AffectationOptimiste.append(categories.get("C"+str(j)))
                break
            
    return AffectationOptimiste

    
def compareClassification(TypeEval,lamda,csv_name,direction,type='excel'):
    """
    compare la méthode d'évaluation utilisé avec les résultats obtenues par le magazine
    
    Args : 
        TypeEval : le type d'évaluation utilisé Optimiste ou Pessimiste
        lamda : le seuil de majorité 
        csv_name: le nom du fichier de données placé dans le répertoire data
        type: le type de fichier ('excel' ou 'csv')
        direction: si on veut maximiser ou minimiser 
        
    Return : un seuil de mauvaise classification
    
    """
    global IMauvC
    AffectationOptimiste = EvaluationOptimiste(lamda,csv_name,direction,type='excel')
    AffectationPessimiste = EvaluationPessimiste(lamda,csv_name,direction,type='excel')
    df = loadModel(csv_name, type)
    _ ,_, df_criteria_list, _, _, _, score_bymagazine, categories = parseDataframe(df) 
    nb_produits=len(df_criteria_list) #nombre de produits

    
    if TypeEval =="pessimiste" or TypeEval =="p":
        IMauvC =0 #Indice de mauvaise classification
        for i in range(len(AffectationPessimiste)):
            if list(categories.keys())[list(categories.values()).index(AffectationPessimiste[i])]!=score_bymagazine[i] :
                IMauvC +=1
                
    else:
        IMauvC =0 #Indice de mauvaise classification
        for i in range(len(AffectationOptimiste)):
            if list(categories.keys())[list(categories.values()).index(AffectationOptimiste[i])]!=score_bymagazine[i] :
                IMauvC +=1
        
    return (IMauvC/nb_produits*100)
    
    