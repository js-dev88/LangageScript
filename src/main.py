"""
@authors: 
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali
    
"""

from system import checkAdditiveModel

def main():
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes avec notes',
                      eval_expr='x1',
                      direction='max')
   
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx',
                      model_name='Programme Lineaire - Classement Couches-culottes sans note',
                      eval_expr='x1',
                      direction='max')

if __name__ == "__main__":
    main()