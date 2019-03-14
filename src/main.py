"""
@authors: 
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali
    
"""

from system import checkAdditiveModel, createUpdateModel, compareRankings, getOriginalData
from optlang import Variable, Constraint

def main():
#------------------------------------------------------------  
#Q1
#------------------------------------------------------------  
   result_2_1 = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes avec notes',
                      eval_expr='x1',
                      direction='max',
                      with_scores=True)
   print(result_2_1)
   
#------------------------------------------------------------  
#Q2
#------------------------------------------------------------  
   
   result_2_2 = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes sans note',
                      eval_expr='x1',
                      direction='max')
   
   print(result_2_2)
   
   
   
#Q3
   result_original = getOriginalData('../data/data_couches_original.xlsx') 
   update_model_Q3 = createUpdateModel([Variable ('x6', ub = 20)], ['c16', 'c21'])
#------------------------------------------------------------  
#Q3.1
#------------------------------------------------------------  
   
   
   
   result_3_1_max = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Meilleur score Joone',
                      eval_expr='y1',
                      direction='max',
                      update_model=update_model_Q3)
   
   print(result_3_1_max)
   compareRankings(result_original['Score'], result_3_1_max['Score'])
   
   result_3_1_min = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Pire score Joone',
                      eval_expr='y1',
                      direction='min',
                      update_model=update_model_Q3)
   
   print(result_3_1_min)
   compareRankings(result_original['Score'], result_3_1_min['Score'])

#------------------------------------------------------------  
#Q3.2
#------------------------------------------------------------  
  
   result_3_2_max = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Meilleur score Lillydoo',
                      eval_expr='y12',
                      direction='max',
                      update_model=update_model_Q3)
   
   print(result_3_2_max)
   
   #Q3.3
   compareRankings(result_original['Score'], result_3_2_max['Score'])
   
   result_3_2_min = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Pire score Lillydoo',
                      eval_expr='y12',
                      direction='min',
                      update_model=update_model_Q3)
   
   print(result_3_2_min)
   #Q3.3
   compareRankings(result_original['Score'], result_3_2_min['Score'])

#Q4
   update_model_Q4 = createUpdateModel([Variable ('x6', ub = 20)], ['c13', 'c14', 'c15', 
                                                                    'c16', 'c17', 'c18',
                                                                    'c19', 'c20', 'c21',
                                                                    'c22', 'c23'])
#4.1
   result_4_1_all_max = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Score global maximal pour chaque produit',
                      eval_expr='all',
                      direction='max',
                      update_model=update_model_Q4)
   
   print(result_4_1_all_max)
   #Q3.3
   compareRankings(result_original['Score'], result_4_1_all_max['Score']) 
   
if __name__ == "__main__":
    main()