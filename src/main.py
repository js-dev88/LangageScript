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
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx', eval_expr='x1', direction='max')
   checkAdditiveModel(csv_name='../data/data_couches_original.xlsx', eval_expr='x1', direction='max', with_scores=False)

if __name__ == "__main__":
    main()