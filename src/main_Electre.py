"""
@authors:
    Ayoub Afrass
    Ikram Bouhya
    Badreddine Machkour
    Julien Saussier
    Abdelkader Zerouali

"""


from Electre_tri import ConcordancePartielleHbi, ConcordancePartiellebiH, ConcordonceGlobaleHbi,ConcordonceGlobalebiH 
from Electre_tri import SurclassementHbi,SurclassementbiH,EvaluationPessimiste,EvaluationOptimiste, compareClassification
from loader import getElectreTriData, exportInExcel

def main():
#------------------------------------------------------------
#Etape 1: Concordance partielle
#------------------------------------------------------------
   csv_name='../data/data_couches_original.xlsx'
   direction="max"
   lamda=0.55
   result_original = getElectreTriData(csv_name) 



   print("Concordance partielle (H,bi)",ConcordancePartielleHbi(csv_name=csv_name,
                      direction=direction))

   print("Concordance partielle (bi,H)", ConcordancePartiellebiH(csv_name=csv_name,
                      direction=direction))

   print("Concordance globale (H,bi)", ConcordonceGlobaleHbi(csv_name=csv_name,
                      direction=direction ))

   print("Concordance globale (bi,H)", ConcordonceGlobalebiH(csv_name=csv_name,
                      direction=direction ))

   print("Matrice de Surclassement (H,bi)", SurclassementHbi(lamda=lamda,
                      csv_name=csv_name,
                      direction=direction))

   print("Matrice de Surclassement (bi,H)", SurclassementbiH(lamda=lamda,
                     csv_name=csv_name,
                     direction=direction))
   
   EvalOptimisteResult = EvaluationPessimiste(lamda=lamda,
                     csv_name=csv_name,
                     direction=direction)
   
   print("Evaluation Pessimiste", EvalOptimisteResult)
   
   
   EvalPessimisteResult = EvaluationOptimiste(lamda=lamda,
                     csv_name=csv_name,
                     direction=direction)
   
   print("Evaluation Pessimiste",EvalPessimisteResult )
   
   
   taux_mauvaise_classification= compareClassification(TypeEval="optimiste",
                                                       lamda=lamda,
                                                       csv_name=csv_name,
                                                       direction=direction)
   
   print("Taux mauvaise classification Opt", taux_mauvaise_classification)
   
   
   taux_mauvaise_classification1 = compareClassification(TypeEval="pessimiste",
                                                       lamda=lamda,
                                                       csv_name=csv_name,
                                                       direction=direction)
   
   print("Taux mauvaise classification Pess", taux_mauvaise_classification1)
   
   
   exportInExcel('./Resultats_Electre_tri.xlsx', 'Electre-tri',
                 [result_original,taux_mauvaise_classification,taux_mauvaise_classification1],
                 [EvalOptimisteResult],
                 [EvalPessimisteResult])

if __name__ == "__main__":
    main()