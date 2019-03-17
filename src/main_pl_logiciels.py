"""
@authors: 
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali
    
"""


from ressources.system import checkAdditiveModel, createUpdateModel, compareRankings
from optlang import Variable
from ressources.loader import getOriginalData, exportInExcel

def main():
#------------------------------------------------------------  
#Q2.1
#------------------------------------------------------------
   csv_name='../data/data_logiciels_original.xlsx'
   export_name = './results/Logiciels_Analyse_Classement.xlsx'
    
    
   model_name_1 = 'Programme Lineaire - Classement Logiciels avec notes' 
   result_2_1 = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_1,
                      eval_expr='x1',
                      direction='max',
                      with_scores=True)
   print(result_2_1)
   
   
   
#------------------------------------------------------------  
#Q2.2
#------------------------------------------------------------  
   
   
   
   model_name_2 = 'Programme Lineaire - Classement Logiciels sans note'
   result_2_2 = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_2,
                      eval_expr='x1',
                      direction='max')
   print(result_2_2)
   
   
   
#------------------------------------------------------------  
#Q3
#------------------------------------------------------------  
   
   
   result_original = getOriginalData(csv_name) 
   update_model_Q3 = createUpdateModel([Variable ('x6', ub = 20)], ['c16', 'c21'])
   
   
#------------------------------------------------------------  
#Q3.1
#------------------------------------------------------------  
   
   
   
   model_name_3 = 'Programme Lineaire - Meilleur score Dashlane'
   result_3_1_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_3,
                      eval_expr='y1',
                      direction='max',
                      update_model=update_model_Q3)
   print(result_3_1_max)
   
    
  
   model_name_4 = 'Programme Lineaire - Pire score Dashlane'
   result_3_1_min = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_4,
                      eval_expr='y1',
                      direction='min',
                      update_model=update_model_Q3)
   print(result_3_1_min)
   
   
   #------------------------------------------------------------ 
   #Q3.3
   #------------------------------------------------------------ 

   dict_max_y1 = compareRankings(result_original['Score'], result_3_1_max['Score'])
   dict_min_y1 = compareRankings(result_original['Score'], result_3_1_min['Score'])
   
   
   
   exportInExcel(export_name, 'Q3.1',
                 [result_original, result_3_1_max, result_3_1_min],
                 ['Modèle Original',model_name_3, model_name_4],
                 [dict_max_y1,dict_min_y1])
#------------------------------------------------------------  
#Q3.2
#------------------------------------------------------------  
  
   model_name_5 = 'Programme Lineaire - Meilleur score Avast'
   result_3_2_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_5,
                      eval_expr='y10',
                      direction='max',
                      update_model=update_model_Q3)
   
   print(result_3_2_max)
   
 
   model_name_6 = 'Programme Lineaire - Pire score Avast'
   result_3_2_min = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_6,
                      eval_expr='y10',
                      direction='min',
                      update_model=update_model_Q3)
   
   print(result_3_2_min)
   
   
   #------------------------------------------------------------ 
   #Q3.3
   #------------------------------------------------------------ 
   dict_max_y12 = compareRankings(result_original['Score'], result_3_2_max['Score'])
   dict_min_y12 = compareRankings(result_original['Score'], result_3_2_min['Score'])
   
   
   
   exportInExcel(export_name, 'Q3.2',
                 [result_original, result_3_2_max, result_3_2_min],
                 ['Modèle Original',model_name_5, model_name_6],
                 [dict_max_y12,dict_min_y12])

#------------------------------------------------------------  
#Q4
#------------------------------------------------------------  
   
   update_model_Q4 = createUpdateModel([Variable ('x6', ub = 20)], ['c11', 'c12', 'c13', 
                                                                    'c14', 'c15', 'c16',
                                                                    'c17', 'c18', 'c19'])
#------------------------------------------------------------  
#Q4.1
#------------------------------------------------------------
    
    
   model_name_7 = 'Programme Lineaire - Score global maximal pour chaque produit'
   result_4_1_all_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_5,
                      eval_expr='all',
                      direction='max',
                      update_model=update_model_Q4)
   
   print(result_4_1_all_max)
   
#------------------------------------------------------------  
#Q4.2
#------------------------------------------------------------
   dict_max_all = compareRankings(result_original['Score'], result_4_1_all_max['Score']) 
   exportInExcel(export_name, 'Q4',
                 [result_original, result_4_1_all_max],
                 ['Modèle Original',model_name_7],
                 [dict_max_all])
   
if __name__ == "__main__":
    main()