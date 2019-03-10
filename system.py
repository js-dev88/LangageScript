from optlang import Model, Variable, Constraint, Objective
from loader import loadModel
import pandas as pd
import math


def checkAdditiveModel(csv_name, type='excel'):
    
    model = linearProgramSolver(csv_name, type, 'x1', 'max', 'Linear Program With Scores')
    displayModel(model)
    

def linearProgramSolver(csv_name, type, eval_expr, direction, model_name):
    score, coeff_list, df_criteria_list, df_criteria_bareme = loadModel(csv_name, type)
    nb_criteria = len(df_criteria_list.columns)
    # variables definition
    variable_list = buildVariableDefinitionList(df_criteria_list, df_criteria_bareme)
    # constraint definition
    constraint_list = buildConstraintDefinitionList(coeff_list, variable_list, nb_criteria, score)
    #objective definition
    if eval_expr == 'x1':
        obj = Objective(variable_list[0], direction)
    #Model
    model = buildModel(constraint_list, obj, model_name) 
    return model

def buildModel(constraint_list, obj, model_name):
    
    model = Model(name = model_name)
    model.objective = obj
    model.add(constraint_list)
    model.optimize() 
    return model
    
def displayModel(model):
    
    print("status: ", model.status)
    print("objective value: ", model.objective.value)
    print("----------------------")
    
    for var_name, var in model.variables.items():
        print(var_name,"=",var.primal)
    
def buildVariableDefinitionList(df_criteria_list, df_criteria_bareme):

    i=0
    variable_list = list()
    for _, row in df_criteria_bareme.iterrows():
        for criteria in df_criteria_list.iloc[:,1:]:
            i+=1
            var = Variable (f'x{i}', lb=row[f'Min_value_{criteria}'], ub = row[f'Max_value_{criteria}'])
            variable_list.append(var)
    return variable_list

def buildConstraintDefinitionList(coeff_list, variable_list, nb_criteria, score):
    
    constraint_list = list()
    cons_num = 0
    for var_num in range(1,len(variable_list),nb_criteria-1):
        var_index = var_num
        list_of_parameter=list() 
        for i in range(0, nb_criteria-1):
           coeff_var = (coeff_list[i], variable_list[var_index-1])
           list_of_parameter.append(coeff_var)
           var_index+=1
        constraint_list.append(createConstraint(list_of_parameter, score[cons_num]))
        cons_num += 1
    return constraint_list
               
def createConstraint(list_of_parameter,score):
    list_expr = []
    for t in list_of_parameter:
        expr = t[0]* t[1]
        list_expr.append(expr)
    
    expr = list_expr[0]
    for exp in list_expr[1:]:
        expr += exp

    constraint = Constraint(expr, lb = score, ub = score)
    return constraint            


checkAdditiveModel('input_couches.xlsx')