from optlang import Model, Variable, Constraint, Objective
from random import *
import pandas as pd
from xlwt import Workbook
from spearman_kendall_coef import RankingCompareSpearman, RankingCompareKendall

''' Définition des variables du modele  avec Contraintes "inégalités" 20 à 29'''
x1 = Variable ('x1', lb=17, ub = 20)
x2 = Variable ('x2', lb=17, ub = 20)
x3 = Variable ('x3', lb=13, ub = 16.5)
x4 = Variable ('x4', lb=13, ub = 16.5)
x5 = Variable ('x5', lb=10, ub = 12.5)
x6 = Variable ('x6', ub = 20)
x7 = Variable ('x7', lb=10, ub = 12.5)
x8 = Variable ('x8', lb=17, ub = 20)
x9 = Variable ('x9', lb= 10, ub = 12.5)
x10 = Variable ('x10', lb=10, ub = 12.5)
x11 = Variable ('x11', lb=13, ub = 16.5)
x12 = Variable ('x12', lb=10, ub = 12.5)
x13 = Variable ('x13', lb=13, ub = 16.5)
x14 = Variable ('x14', lb=7, ub = 9.5)
x15 = Variable ('x15', lb=10, ub = 12.5)
x16 = Variable ('x16', lb=7, ub = 9.5)
x17 = Variable ('x17', lb=13, ub = 16.5)
x18 = Variable ('x18', lb=7, ub = 9.5)
x19 = Variable ('x19', lb=13, ub = 16.5)
x20 = Variable ('x20', lb=0, ub = 6.5)
x21 = Variable ('x21', lb=13, ub = 16.5)
x22 = Variable ('x22', lb=0, ub = 6.5)
x23 = Variable ('x23', lb=10, ub = 12.5)
x24 = Variable ('x24', lb=0, ub = 6.5)

''' Définitions des variables y == f^a...f^l des réels entre 0 et 20'''
y1 = Variable ('y1', lb=0, ub = 20)
y2 = Variable ('y2', lb=0, ub = 20)
y3 = Variable ('y3', lb=0, ub = 20)
y4 = Variable ('y4', lb=0, ub = 20)
y5 = Variable ('y5', lb=0, ub = 20)
y6 = Variable ('y6', lb=0, ub = 20)
y7 = Variable ('y7', lb=0, ub = 20)
y8 = Variable ('y8', lb=0, ub = 20)
y9 = Variable ('y9', lb=0, ub = 20)
y10 = Variable ('y10', lb=0, ub = 20)
y11 = Variable ('y11', lb=0, ub = 20)
y12 = Variable ('y12', lb=0, ub = 20)


''' Contraintes "égalité"  4 à 15 '''
c1 = Constraint ((0.6 * x1 + 0.4 * x2)-y1, lb = 0, ub = 0)
c2 = Constraint((0.6 * x3 + 0.4 * x4)-y2, lb = 0, ub = 0)
c3 = Constraint((0.6 * x5 + 0.4 * x6)-y3, lb = 0, ub = 0)
c4 = Constraint((0.6 * x7 + 0.4 * x8)-y4, lb = 0, ub = 0)
c5 = Constraint((0.6 * x9 + 0.4 * x10)-y5, lb = 0, ub = 0)
c6 = Constraint((0.6 * x11 + 0.4 * x12)-y6, lb = 0, ub = 0)
c7 = Constraint((0.6 * x13 + 0.4 * x14)-y7, lb = 0, ub = 0)
c8 = Constraint((0.6 * x15 + 0.4 * x16)-y8, lb = 0, ub = 0)
c9 = Constraint((0.6 * x17 + 0.4 * x18)-y9, lb = 0, ub = 0)
c10 = Constraint((0.6 * x19 + 0.4 * x20)-y10, lb = 0, ub = 0)
c11 = Constraint((0.6 * x21 + 0.4 * x22)-y11, lb = 0, ub = 0)
c12 = Constraint((0.6 * x23 + 0.4 * x24)-y12, lb = 0, ub = 0)

''' Contraintes 16 - 19 
c13 = Constraint((y1-y2), lb = 0.1)
c14 = Constraint(y2-y3, lb = 0.1)
c15 = Constraint(y3-y4, lb = 0, ub = 0) #Fin contrainte 16
#c16 = Constraint(y4-y5, lb = 0, ub = 0)
c17 = Constraint(y5-y6, lb = 0, ub = 0)
c18 = Constraint(y6-y7, lb = 0.1) #Fin contrainte 17
c19 = Constraint(y7-y8, lb = 0, ub = 0)
#c20 = Constraint(y9-y10, lb = 0, ub = 0)
c21 = Constraint(y8-y9, lb = 0.1) #Fin contrainte 18
c22 = Constraint(y10-y11,lb=0,ub=0)
c21 = Constraint(y11-y12, lb = 0.1) #Fin contrainte 19'''

'''
obj = Objective(y12, direction ='max')

model = Model(name = 'Simple model')
model.objective = obj
model.add([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
status = model.optimize()
    
print("status: ", model.status)
print("objective value: ", model.objective.value)
print("----------------------")

for var_name, var in model.variables.items():
    print(var_name,"=",var.primal)
 '''   
''' 
#4.1 
#RESULTATS OBTENUS en maximisant yn le score global de la couche n (n allant de 1 à 12 - a à l):

y1 (=fa) = 20 
y2 (=fb) = 16.5 
y3 (=fc) = 15.5 
y4 (=fd) = 15.5 
y5 (=fe) = 12.5 => descend dans le classement
y6 (=ff) = 14.9 
y7 (=fg) = 13.7 
y8 (=fh) = 11.3 => descend dans le classement
y9 (=fi) = 13.7 
y10 (=fj) = 12.5 
y11 (=fk) = 12.5 
y12 (=fl) = 10.1 
'''

# création wokrbook excel
book = Workbook()

# création de la feuille 1
feuil1 = book.add_sheet('Ranking_Q4')

# ajout des en-têtes
feuil1.write(0,0,'couche')
feuil1.write(0,1,'note')

notes = {"fa" : y1, "fb": y2, "fc" : y3,"fd" : y4, "fe" : y5, "ff" : y6, "fg" : y7, "fh" : y8, "fi" : y9, "fj" : y10, "fk" : y11, "fl" : y12}

for key, value in notes.items():
    obj = Objective(value, direction ='max')

    model = Model(name = 'Simple model')
    model.objective = obj
    model.add([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
    status = model.optimize()
    notes[key] = model.objective.value

i = 1
for key, value in sorted(notes.items(),  key=lambda kv: kv[0]):
    feuil1.write(i,0, key)
    feuil1.write(i,1, value)
    i += 1

ranking_q4 = "ranking_q4.xls"
book.save(ranking_q4)

magazine_input ="input_couches.xlsx"
Data_Ranking = pd.read_excel(magazine_input ,sheet_name ='Feuil1')

Data_RankingQ4 = pd.read_excel(ranking_q4)
rank1 =Data_Ranking['Score'] 
rank2 = Data_RankingQ4['note']

############# SpearMan Q3###############
coef ,p = RankingCompareSpearman(rank1,rank2)
############# Kendall Q3 ################
tau , p_val = RankingCompareKendall(rank1,rank2)

print ("Spearman :\ncoef :", coef, "\np :", p, "\n\n")
print ("Kendall :\ntau :", tau, "\np_val :", p_val)


'''
#Q4.2
Le coefficient de Spearman s'élève à 0.81862, cela nous permet de voir qu'il y a une liaison assez forte et qu'il y a donc une relation monotone entre le classement proposé par le magazine et
le classement obtenu en retirant les contraintes d'ordre sur le classement des couches.
Les deux variables évoluent dans la même direction, lorsque la note évaluée 
par le magazine augmente, celle obtenue indépendamment des notes du magazine augmente également.
Ce coefficient est relativement proche de 1, cela signifie que les deux classements 
sont quasiement identiques.

De même, en calculant le coefficient de Kendall, on obtient un résultat de 0.73571.
Cela nous amène aux mêmes conclusions :
    Il existe une corrélation positive entre le classement obtenu par le magazine et
    celui obtenu en retirant les contraites d'égalité de notes des couches d-e et i-j.
    Le coefficient étant positif, cela signifie que les variables évoluent dans le 
    même sens. 
    La p-value associée au coefficient de Kendall est quasiment nulle (0.00019) ce qui nous permet de rejeter l'hypothèse nulle (l'indépendance des classements). 
    

'''