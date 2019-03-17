#MAIN FINAL LOGICIELS

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
   csv_name='../data/data_logiciels_original.xlsx'
   export_name = './results/Logiciels_Analyse_Classement.xlsx'
   result_original = getOriginalData(csv_name)
    
    
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
   
   
   dict_max_x1 = compareRankings(result_original['Score'], result_2_2['Score'])
   exportInExcel(export_name, 'Q2.2',
			 [result_original, result_2_2],
			 ['Modèle Original',model_name_2],
			 [dict_max_x1])
#------------------------------------------------------------  
#TESTING different scenarios sans contraintes d'égalité - Dashlane max min 
#------------------------------------------------------------  

	#On retire les contraintes d'égalités de score des logiciels
   update_model_test = createUpdateModel([], ['c13', 'c15', 'c19']) #c13 pour y3 = y4, c15 pour y5 = y6 et c19 pour y9 = 10
   
   
   model_name_test = 'Programme Lineaire - Meilleur score Dashlane'
   result_test_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_test,
                      eval_expr='y1',
                      direction='max',
                      update_model=update_model_test)
   print(result_test_max)
   
   model_name_test2 = 'Programme Lineaire - Pire score Dashlane'
   result_test_min = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_test2,
                      eval_expr='y1',
                      direction='min',
                      update_model=update_model_test)
   print(result_test_min)
   
   dict_max_y1 = compareRankings(result_original['Score'], result_test_max['Score'])
   dict_min_y1 = compareRankings(result_original['Score'], result_test_min['Score'])
   
   
   
   exportInExcel(export_name, 'Dashlane',
                 [result_original, result_test_max, result_test_min],
                 ['Modèle Original',model_name_test, model_name_test2],
                 [dict_max_y1,dict_min_y1])
   
#------------------------------------------------------------  
#TESTING different scenarios sans contraintes d'égalité - Avast max min 
#------------------------------------------------------------  

   model_name_test3 = 'Programme Lineaire - Meilleur score Avast'
   result_test_avast_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_test3,
                      eval_expr='y10',
                      direction='max',
                      update_model=update_model_test)
   print(result_test_avast_max)
   
   model_name_test4 = 'Programme Lineaire - Pire score Avast'
   result_test_avast_min = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_test4,
                      eval_expr='y10',
                      direction='min',
                      update_model=update_model_test)
   print(result_test_avast_min)
   
   dict_max_y10 = compareRankings(result_original['Score'], result_test_avast_max['Score'])
   dict_min_y10 = compareRankings(result_original['Score'], result_test_avast_min['Score'])
   
   
   
   exportInExcel(export_name, 'Avast',
                 [result_original, result_test_avast_max, result_test_avast_min],
                 ['Modèle Original',model_name_test3, model_name_test4],
                 [dict_max_y10,dict_min_y10])
#------------------------------------------------------------  
#Q4
#------------------------------------------------------------  
   
   update_model_Q4 = createUpdateModel([], ['c11', 'c12', 'c13', 
                                                                    'c14', 'c15', 'c16',
                                                                    'c17', 'c18', 'c19'])
#------------------------------------------------------------  
#Q4.1
#------------------------------------------------------------
    
    
   model_name_7 = 'Programme Lineaire - Score global maximal pour chaque produit'
   result_4_1_all_max = checkAdditiveModel(csv_name=csv_name,
                      model_name=model_name_7,
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