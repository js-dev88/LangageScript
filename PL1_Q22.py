from optlang import Model, Variable, Constraint, Objective
from random import *
import pandas as pd

''' valeurs des f^a  à f^l, à récupérer depuis une liste et utilisé pour la question 2.2
y1 = 17
y2 = 14.5
y3 = y4 = y5 = y6 = 12.5
y7 = y8 = 12
y9 = y10 = y11 = 9.5
y12 = 6.5
'''

''' Définition des variables du modele  avec Contraintes "inégalités" 20 à 29'''
x1 = Variable ('x1', lb=17, ub = 20)
x2 = Variable ('x2', lb=17, ub = 20)
x3 = Variable ('x3', lb=13, ub = 16.5)
x4 = Variable ('x4', lb=13, ub = 16.5)
x5 = Variable ('x5', lb=10, ub = 12.5)
x6 = Variable ('x6', lb=17, ub = 20)
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

''' Contraintes 16 - 19 '''
c13 = Constraint((y1-y2), lb = 0.1)
c14 = Constraint(y2-y3, lb = 0.1)
c15 = Constraint(y3-y4, lb = 0, ub = 0) #Fin contrainte 16
c16 = Constraint(y4-y5, lb = 0, ub = 0)
c17 = Constraint(y5-y6, lb = 0, ub = 0)
c18 = Constraint(y6-y7, lb = 0.1) #Fin contrainte 17
c19 = Constraint(y7-y8, lb = 0, ub = 0)
c20 = Constraint(y9-y10, lb = 0, ub = 0)
c21 = Constraint(y8-y9, lb = 0.1) #Fin contrainte 18
c22 = Constraint(y10-y11,lb=0,ub=0)
c21 = Constraint(y11-y12, lb = 0.1) #Fin contrainte 19

obj = Objective(x1, direction ='max')

model = Model(name = 'Simple model')
model.objective = obj
model.add([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21])
status = model.optimize()
    
print("status: ", model.status)
print("objective value: ", model.objective.value)
print("----------------------")

for var_name, var in model.variables.items():
    print(var_name,"=",var.primal)


#indicepair == performance & indiceimpair== composition
"""for indicepair, elt in enumerate(model.variables):
    if indicepair % 2 == 0:
        print(indicepair," ", model.variables[indicepair].primal)   

print([model.variables[indiceP].primal for indiceP,elt in enumerate(model.variables) if indiceP % 2 == 0])
"""

if(model.status=="infeasible"):
    exported_data = {'Status': model.status,
                     'Message': 'Erreur : le classement n’est pas explicable par un modèle type somme pondérée'}
    df = pd.DataFrame(exported_data, columns = ['Status','Message'],index=[0])
                
else:
    exported_data = {'Status': model.status,
                'Produit': ['a- Joone','b- Pamp. Prem','c- Pamp. Baby','d- Naty','e- Pamp. Activ.','f- Carref.Baby',
                    'g- Lupilu','h- Mots d’enfants', 'i- Love & Green','j- Lotus Baby','k- Pommette',
                    'l- Lillydoo '],
                'Performance':[model.variables[indiceP].primal for indiceP,elt in enumerate(model.variables) if indiceP % 2 == 0],
                'Composition':[model.variables[indiceI].primal for indiceI,elt in enumerate(model.variables) if indiceI % 2 != 0],
                'Score': ['17,00','14,50','12,50','12,50','12,50','12,50','12,00',
                          '12,00','9,50','9,50','9,50','6,50']}
    df = pd.DataFrame(exported_data, columns = ['Status','Produit','Performance','Composition','Score'],index=[0])

df.to_csv('Resultat.csv',encoding='utf-8',index=False)

#if(model.status == "infeasible"):
#    print("Erreur : Classement non explicable par un modèle de type somme pondérée") 
    
    #la modélisation a été faite avec les valeurs exactes de f^a,...f^l puis avec des valeurs entre 0 et 20 de f^a,...f^l 
    # En prenant des évaluation quelconque entre 0 et 20, le PL reste toujours non réalisable.
    #2.3 La compréhension intuitive des résultats, suppose qu'il existe deux critères de classement : Performance et composition
    # La composition compte pour 40%, et la performance pour 60%
    #Or, en modélisant ce problème, avec ces coéfficients liés à ces deux critères, on constate qu'il n'existe pas de solution réalisable exacte de ce problème via un model de somme pondérée.
    # Ces résultats mettent en cause au moins la présentation de cette étude.
