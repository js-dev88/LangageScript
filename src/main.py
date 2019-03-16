"""
@authors: 
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali
    
"""


from system import checkAdditiveModel, createUpdateModel, compareRankings
from optlang import Variable
from loader import getOriginalData, exportInExcel

def main():
#------------------------------------------------------------  
#Q2.1
#------------------------------------------------------------
   csv_name='../data/data_couches_original.xlsx'
    
    
   model_name_1 = 'Programme Lineaire - Classement Couches-culottes avec notes' 
   result_2_1 = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_1,
                      eval_expr='x1',
                      direction='max',
                      with_scores=True)
   print(result_2_1)
   
   
   
#------------------------------------------------------------  
#Q2.2
#------------------------------------------------------------  
   
   
   
   model_name_2 = 'Programme Lineaire - Classement Couches-culottes sans note'
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
   
   
   
   model_name_3 = 'Programme Lineaire - Meilleur score Joone'
   result_3_1_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_3,
                      eval_expr='y1',
                      direction='max',
                      update_model=update_model_Q3)
   print(result_3_1_max)
   
    
  
   model_name_4 = 'Programme Lineaire - Pire score Joone'
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
   
   
   
   exportInExcel('./Partie_1_Analyse_Classement.xlsx', 'Q3.1',
                 [result_original, result_3_1_max, result_3_1_min],
                 ['Modèle Original',model_name_3, model_name_4],
                 [dict_max_y1,dict_min_y1])
#------------------------------------------------------------  
#Q3.2
#------------------------------------------------------------  
  
   model_name_5 = 'Programme Lineaire - Meilleur score Lillydoo'
   result_3_2_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_5,
                      eval_expr='y12',
                      direction='max',
                      update_model=update_model_Q3)
   
   print(result_3_2_max)
   
 
   model_name_6 = 'Programme Lineaire - Pire score Lillydoo'
   result_3_2_min = checkAdditiveModel(csv_name=csv_name,
                      model_name='Programme Lineaire - Pire score Lillydoo',
                      eval_expr='y12',
                      direction='min',
                      update_model=update_model_Q3)
   
   print(result_3_2_min)
   
   
   #------------------------------------------------------------ 
   #Q3.3
   #------------------------------------------------------------ 
   dict_max_y12 = compareRankings(result_original['Score'], result_3_2_max['Score'])
   dict_min_y12 = compareRankings(result_original['Score'], result_3_2_min['Score'])
   
   
   
   exportInExcel('./Partie_1_Analyse_Classement.xlsx', 'Q3.2',
                 [result_original, result_3_2_max, result_3_2_min],
                 ['Modèle Original',model_name_5, model_name_6],
                 [dict_max_y12,dict_min_y12])

#------------------------------------------------------------  
#Q4
#------------------------------------------------------------  
   
   update_model_Q4 = createUpdateModel([Variable ('x6', ub = 20)], ['c13', 'c14', 'c15', 
                                                                    'c16', 'c17', 'c18',
                                                                    'c19', 'c20', 'c21',
                                                                    'c22', 'c23'])
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
   exportInExcel('./Partie_1_Analyse_Classement.xlsx', 'Q4',
                 [result_original, result_4_1_all_max],
                 ['Modèle Original',model_name_7],
                 [dict_max_all])
   
if __name__ == "__main__":
    main()