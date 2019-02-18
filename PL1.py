from optlang import Model, Variable, Constraint, Objective
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

''' Contraintes "égalité"  4 à 15 '''
c1 = Constraint (0.6 * x1 + 0.4 * x2, lb = 17, ub = 17)
c2 = Constraint(0.6*x3 + 0.4*x4, lb = 14.5, ub = 14.5)
c3 = Constraint(0.6*x5 + 0.4*x6, lb = 12.5, ub = 12.5)
c4 = Constraint(0.6*x7 + 0.4*x8, lb = 12.5, ub = 12.5)
c5 = Constraint(0.6*x9 + 0.4*x10, lb = 12.5, ub = 12.5)
c6 = Constraint(0.6*x11 + 0.4*x12, lb = 12.5, ub = 12.5)
c7 = Constraint(0.6*x13 + 0.4*x14, lb = 12, ub = 12)
c8 = Constraint(0.6*x15 + 0.4*x16, lb = 12, ub = 12)
c9 = Constraint(0.6*x17 + 0.4*x18, lb = 9.5, ub = 9.5)
c10 = Constraint(0.6*x19 + 0.4*x20, lb = 9.5, ub = 9.5)
c11 = Constraint(0.6*x21 + 0.4*x22, lb = 9.5, ub = 9.5)
c12 = Constraint(0.6*x23 + 0.4*x24, lb = 6.5, ub = 6.5)


obj = Objective(x1, direction ='max')

model = Model(name = 'Simple model')
model.objective = obj
model.add([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
status = model.optimize()
    
print("status: ", model.status)
print("objective value: ", model.objective.value)
print("----------------------")

for var_name, var in model.variables.items():
    print(var_name,"=",var.primal)
    
#if(model.status == "infeasible"):
#    print("Erreur : Classement non explicable par un modèle de type somme pondérée") 
    
    #la modélisation a été faite avec les valeurs exactes de f^a,...f^l
    #Pour la question 2.2, il faudra modifier le model, en modélisant le cas général avec des variables.
    #2.3 La compréhension intuitive des résultats, suppose qu'il existe deux critères de classement : Performance et composition
    # La composition compte pour 40%, et la performance pour 60%
    #Or, en modélisant ce problème, avec ces coéfficients liés à ces deux critères, on constate qu'il n'existe pas de solution réalisable exacte de ce problème via un model de somme pondérée.
    # Ces résultats mettent en cause au moins la présentation de cette étude.