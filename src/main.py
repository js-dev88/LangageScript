"""
@authors: 
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali
    
"""

from system import checkAdditiveModel
from optlang import Variable, Constraint

def main():
    
#Q1
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes avec notes',
                      eval_expr='x1',
                      direction='max')

#Q2 
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes sans note',
                      eval_expr='x1',
                      direction='max',
                      with_scores=False)

#Q3
   update_model = {}
   update_model['variable'] = {}
   update_model['constraint'] = {}
   update_model['variable']['upd'] = [Variable ('x6', ub = 20)]
   update_model['constraint']['del'] = ['c16', 'c21']
   
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes sans note',
                      eval_expr='y1',
                      direction='max',
                      with_scores=False,
                      update_model=update_model)
   
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes sans note',
                      eval_expr='y1',
                      direction='min',
                      with_scores=False,
                      update_model=update_model)

if __name__ == "__main__":
    main()