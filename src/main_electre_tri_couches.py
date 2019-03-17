"""
@authors:
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali

"""


from electre_tri import ConcordancePartielleHbi, ConcordancePartiellebiH, ConcordonceGlobaleHbi,ConcordonceGlobalebiH 
from electre_tri import SurclassementHbi,SurclassementbiH,EvaluationPessimiste,EvaluationOptimiste, compareClassification
from loader import getElectreTriData, exportInExcel
import pandas as pd

def main():
#------------------------------------------------------------
#Etape 1: Concordance partielle
#------------------------------------------------------------
   csv_name='../data/data_couches_original.xlsx'
   csv_export='./results/Couches_Analyse_Classement.xlsx'
   
   direction="max"
   lambda_1=0.55
   lambda_2=0.75
   result_original = getElectreTriData(csv_name) 
  


   print("Concordance partielle (H,bi)",ConcordancePartielleHbi(csv_name=csv_name,
                      direction=direction))

   print("Concordance partielle (bi,H)", ConcordancePartiellebiH(csv_name=csv_name,
                      direction=direction))

#------------------------------------------------------------
#Etape 2: Concordance globale
#------------------------------------------------------------
   
   print("Concordance globale (H,bi)", ConcordonceGlobaleHbi(csv_name=csv_name,
                      direction=direction ))

   print("Concordance globale (bi,H)", ConcordonceGlobalebiH(csv_name=csv_name,
                      direction=direction ))
   
#------------------------------------------------------------
#Etape 3-1: Matrices de surclassement pour Lambda = 0.55 
#------------------------------------------------------------
   
   print('---------------------------------------------------------------')
   print('lambda = 0.55')
   print('---------------------------------------------------------------')
   

   print("Matrice de Surclassement (H,bi) - lambda 0.55", SurclassementHbi(lamda=lambda_1,
                      csv_name=csv_name,
                      direction=direction))

   print("Matrice de Surclassement (bi,H) - lambda 0.55", SurclassementbiH(lamda=lambda_1,
                     csv_name=csv_name,
                     direction=direction))
   
#------------------------------------------------------------------------------
#Etape 4-1: Application de l'Evaluation Optimiste & Pessimiste pour lamda=0.55
#------------------------------------------------------------------------------  
    
   
   EvalPessimisteResult_lambda_1 = EvaluationPessimiste(lamda=lambda_1,
                     csv_name=csv_name,
                     direction=direction)
   
   print("Evaluation Pessimiste - lambda 0.55", EvalPessimisteResult_lambda_1)
   
   
   EvalOptimisteResult_lambda_1 = EvaluationOptimiste(lamda=lambda_1,
                     csv_name=csv_name,
                     direction=direction)
   
   print("Evaluation Optimiste - lambda 0.55 ",EvalOptimisteResult_lambda_1 )
   

#----------------------------------------------------------------------
#Etape 5-1: Calcul des taux de mauvaise classification pour lamda=0.55
#----------------------------------------------------------------------
   
   taux_mauvaise_classification_opt_lambda_1= compareClassification(TypeEval="optimiste",
                                                       lamda=lambda_1,
                                                       csv_name=csv_name,
                                                       direction=direction)
   
   print("Taux mauvaise classification Opt - lambda 0.55", taux_mauvaise_classification_opt_lambda_1)
   
   
   taux_mauvaise_classification1_pess_lambda_1 = compareClassification(TypeEval="pessimiste",
                                                       lamda=lambda_1,
                                                       csv_name=csv_name,
                                                       direction=direction)
   
   print("Taux mauvaise classification Pess - lambda 0.55", taux_mauvaise_classification1_pess_lambda_1)
   
   
   
    
   df_Eval_Opt_lambda1=pd.DataFrame(EvalOptimisteResult_lambda_1,columns=["Classement Optimiste"])
   df_Eval_Pes_lambda1=pd.DataFrame(EvalPessimisteResult_lambda_1,columns=["Classement Pessimiste"])
   
   
   new_df_lambda1 = pd.concat([result_original, df_Eval_Opt_lambda1, df_Eval_Pes_lambda1], axis=1, sort=False)
   
   result_lambda1 = {"Tx Optimiste": taux_mauvaise_classification_opt_lambda_1, "Tx Pessimiste" :taux_mauvaise_classification1_pess_lambda_1  }
 
#------------------------------------------------------------
#Etape 3-2: Matrices de surclassement pour Lambda = 0.75 
#------------------------------------------------------------ 
   
   print('---------------------------------------------------------------')
   print('lambda = 0.75')
   print('---------------------------------------------------------------')
   

   print("Matrice de Surclassement (H,bi) - lambda 0.55", SurclassementHbi(lamda=lambda_2,
                      csv_name=csv_name,
                      direction=direction))

   print("Matrice de Surclassement (bi,H) - lambda 0.55", SurclassementbiH(lamda=lambda_2,
                     csv_name=csv_name,
                     direction=direction))

#-----------------------------------------------------------------------------
#Etape 4-2: Application de l'Evaluation Optimiste & Pessimiste pour lamda=0.75
#-----------------------------------------------------------------------------    
   
   
   EvalPessimisteResult_lambda_2 = EvaluationPessimiste(lamda=lambda_2,
                     csv_name=csv_name,
                     direction=direction)
   
   print("Evaluation Pessimiste - lambda 0.75", EvalPessimisteResult_lambda_2)
   
   
   EvalOptimisteResult_lambda_2 = EvaluationOptimiste(lamda=lambda_2,
                     csv_name=csv_name,
                     direction=direction)
   
   print("Evaluation Optimiste - lambda 0.75 ",EvalOptimisteResult_lambda_2 )
   
#----------------------------------------------------------------------
#Etape 5-2: Calcul des taux de mauvaise classification pour lamda=0.75
#----------------------------------------------------------------------
   
   taux_mauvaise_classification_opt_lambda_2= compareClassification(TypeEval="optimiste",
                                                       lamda=lambda_2,
                                                       csv_name=csv_name,
                                                       direction=direction)
   
   print("Taux mauvaise classification Opt - lambda 0.75", taux_mauvaise_classification_opt_lambda_2)
   
   
   taux_mauvaise_classification1_pess_lambda_2 = compareClassification(TypeEval="pessimiste",
                                                       lamda=lambda_2,
                                                       csv_name=csv_name,
                                                       direction=direction)
   
   print("Taux mauvaise classification Pess - lambda 0.75", taux_mauvaise_classification1_pess_lambda_2)
   
   
   
    
   df_Eval_Opt_lambda_2=pd.DataFrame(EvalOptimisteResult_lambda_2,columns=["Classement Optimiste"])
   df_Eval_Pes_lambda_2=pd.DataFrame(EvalPessimisteResult_lambda_2,columns=["Classement Pessimiste"])
   
   
   new_df_lambda_2 = pd.concat([result_original, df_Eval_Opt_lambda_2, df_Eval_Pes_lambda_2], axis=1, sort=False)
   
   result_lambda_2 = {"Tx Optimiste": taux_mauvaise_classification_opt_lambda_2, "Tx Pessimiste" :taux_mauvaise_classification1_pess_lambda_2}  
   
   
   
   
   exportInExcel(csv_export, 'Electre-tri-Couches',
                 [new_df_lambda1, new_df_lambda_2],
                 ['Modèle lambda 0.55', 'Modèle lambda 0.75'],
                 [result_lambda1, result_lambda_2], 
                 electre = True)
   

if __name__ == "__main__":
    main()