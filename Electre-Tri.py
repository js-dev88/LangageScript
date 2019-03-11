from optlang import Model, Variable, Constraint, Objective
from random import *
import pandas as pd
import numpy as np


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
    
print("status: ", obj.direction)
#print("objective value: ", model.objective.value)
#print("----------------------")


k =[3/5 , 2/5] #Poids des critères 
categories = {"C1": "Très Insuffisant", "C2": "Insuffisant", "C3": "Acceptable", "C4":"Bon", "C5":"Très Bon"}

CouchesPerf=np.array(["+++","++","+","+","+","++","++","+","++","++","++","+"])
RefPerf=np.array(["++++","+++","++","+","-","---"])

CouchesCompo=np.array(["+++","++","+++","+++","+","+","-","-","-","--","--","--"])
RefCompo=np.array(["++++","+++","++","+","-","---"])

cpHbi = np.zeros((12, 6), dtype=int)#Matrice de concordance partielle de 12 lignes et 6 colonnes
cpbiH = np.zeros((6, 12), dtype=int)#Matrice de concordance partielle de 12 lignes et 6 colonnes
cpHbi1 = np.zeros((12, 6), dtype=int)#Matrice de concordance partielle de 12 lignes et 6 colonnes
cpbiH1= np.zeros((6,12), dtype=int)#Matrice de concordance partielle de 12 lignes et 6 colonnes

CgHbi = np.zeros((12, 6), dtype=float) #Matrice de concordance globale
CgbiH = np.zeros((6, 12), dtype=float) #Matrice de concordance globale

SurcHbi= np.zeros((12,6), dtype=int)
SurcbiH = np.zeros((6, 12),dtype=int) 

AffectationPessimiste =[] 
AffectationOptimiste =[]

comparator=False
def comparesTo(a,b): # cette fonction retourne "True" quand a >= b sinon elle retourne "False"
    if(a[0]=="+" and b[0]=="+" and len(a)>=len(b)):
        comparator=True
    elif(a[0]=="+" and b[0]=="-"):
        comparator=True
    elif(a[0]=="-" and b[0]=="-" and len(a)<=len(b)): 
        comparator=True
    else: 
        comparator=False
        
    return comparator

#print(comparesTo(CouchesPerf[0],RefPerf[5]))
# print(comparesTo(CouchesPerf[0],RefPerf[1]))


#Calculer la matrice de concordance partielle du critère Performance
if(obj.direction=="max"): 
    for i in range(0,CouchesPerf.size):
        for j in range(0,RefPerf.size):
            cpHbi[i,j]= comparesTo(CouchesPerf[i],RefPerf[j]) #critère 1
            cpHbi1[i,j]= comparesTo(CouchesCompo[i],RefCompo[j]) #critère 2
            
elif(obj.direction=="min"): 
    for i in range(0,CouchesPerf.size):
        for j in range(0,RefPerf.size):
            cpHbi[i,j]= comparesTo(RefPerf[j],CouchesPerf[i]) #critère 1
            cpHbi1[i,j]= comparesTo(RefCompo[j],CouchesCompo[i]) #critère 2
   
print("Matrice de concordance cPerf(H,bi) partielle du critère Performance",cpHbi)
print("Matrice de concordance cComp(H,bi) partielle du critère Composition ",cpHbi1)

    
if(obj.direction=="max"): 
    for j in range(0,RefPerf.size):
        for i in range(0,CouchesPerf.size):
            cpbiH[j,i]= comparesTo(RefPerf[j],CouchesPerf[i]) #critère 1
            cpbiH1[j,i]= comparesTo(RefCompo[j],CouchesCompo[i]) #critère 2

            
elif(obj.direction=="min"): 
    for j in range(0,RefPerf.size):
        for i in range(0,CouchesPerf.size):
            cpbiH[j,i]= comparesTo(CouchesPerf[i],RefPerf[j]) #critère 1
            cpbiH1[j,i]= comparesTo(CouchesCompo[i],RefCompo[j]) #critère 2
            
print("Matrice de concordance cPerf(bi,H) partielle du critère Performance",cpbiH)
print("Matrice de concordance cComp(bi,H) partielle du critère Composition ",cpbiH1)
       

#Calculer la matrice de concordance globale
for i in range(0,CouchesPerf.size):
    for j in range(0,RefPerf.size):  
        CgHbi[i,j]=(k[0]*cpHbi[i,j]+ k[1]*cpHbi1[i,j])/(k[0]+k[1])

#print(k[0]*cpHbi[2,2]+k[1]*cpHbi1[2,2])      
print("Matrice de concordance GLOBALE Cg(H,bi)  ",CgHbi)
#print (k[0]*cpHbi[0,1] +  k[1]*cpHbi1[0,1])

for j in range(0,RefPerf.size):
    for i in range(0,CouchesPerf.size):
        CgbiH[j,i]=k[0]*cpbiH[j,i]+ k[1]*cpbiH1[j,i]/(k[0]+k[1])
        
print("Matrice de concordance GLOBALE Cg(H,bi) ",CgbiH)

#Determiner la relation de surclassment
def SurclassementHbi(lamda):
    for i in range(0,CouchesPerf.size):
        for j in range(0,RefPerf.size): 
            SurcHbi[i,j]= CgHbi[i,j]>=lamda

    return SurcHbi
            
def SurclassementbiH(lamda):
    for j in range(0,RefPerf.size):
        for i in range(0,CouchesPerf.size): 
            SurcbiH[j,i]= CgbiH[j,i]>=lamda

    return SurcbiH
            
SurclassementHbi(0.75)
SurclassementbiH(0.75)

print("Matrice de surclassement (H,bi)",SurclassementHbi(0.55))
print("Matrice de surclassement (bi,H)",SurclassementbiH(0.55))

#Procédure pessimiste
def Evalpessimiste():
    for i in range(0,CouchesPerf.size):
        for j in range(0,RefPerf.size):
            if SurcHbi[i,j]==0 :
                continue
            elif SurcHbi[i,j]==1 and j==0:
                AffectationPessimiste.append(categories.get("C"+str(5)))
            else:
                AffectationPessimiste.append(categories.get("C"+str(6-j)))
                break

                
    return AffectationPessimiste
#je ne traite pas le cas où j'ai que des 0 ? Ce cas est-il possible déjà ? 
print("Affectation pessimiste : ",Evalpessimiste())


#Procédure optimiste
def Evaloptimiste():
    for i in range(0,CouchesPerf.size):
        for j in range(RefPerf.size-1,1):
            if SurcbiH[j,i]==0:
                continue
            elif SurcbiH[j,i]==1 and SurcHbi[i,j]==0:
                AffectationOptimiste.append(categories.get("C"+str(6-j-1)))
                break 
                
                
    return AffectationOptimiste

print("Affectation optimiste : ",Evaloptimiste())
