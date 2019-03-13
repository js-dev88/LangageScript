"""
@authors: 
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali
    
"""

from system import checkAdditiveModel, createUpdateModel
from optlang import Variable, Constraint

def main():
    
#Q1
   result_2_1 = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes avec notes',
                      eval_expr='x1',
                      direction='max',
                      with_scores=True)
   print(result_2_1)

#Q2 
   result_2_2 = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes sans note',
                      eval_expr='x1',
                      direction='max')
   
   print(result_2_2)

#Q3.1
   
   update_model_Q3 = createUpdateModel([Variable ('x6', ub = 20)], ['c16', 'c21'])
   
   result_3_1_max = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Meilleur score Joone',
                      eval_expr='y1',
                      direction='max',
                      update_model=update_model_Q3)
   
   print(result_3_1_max)
   
   result_3_1_min = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Pire score Joone',
                      eval_expr='y1',
                      direction='min',
                      update_model=update_model_Q3)
   
   print(result_3_1_min)
   
#Q3.2
   
   result_3_2_max = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Meilleur score Lillydoo',
                      eval_expr='y12',
                      direction='max',
                      update_model=update_model_Q3)
   
   print(result_3_2_max)
   
   result_3_2_min = checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Pire score Lillydoo',
                      eval_expr='y12',
                      direction='min',
                      update_model=update_model_Q3)
   
   print(result_3_2_min)
   


if __name__ == "__main__":
    main()