from optlang import Model, Variable, Constraint, Objective
from loader import loadModel
import pandas as pd
import math


def checkAdditiveModel(csv_name, eval_expr, direction, type='excel', with_scores=True):
    
    if with_scores:
        model_name = 'programme lineaire avec notes'
    else:
        model_name = 'programme lineaire sans note'
        
    model = linearProgramSolver(csv_name, type, eval_expr, direction , model_name, with_scores)
    
    if model.status == 'infeasible':
        print(f'Le {model.name} du fichier {csv_name} n\'admet pas de solution')
        print(f'Scores : {with_scores}')     
    else:
        displayModel(model)
        """TODO export in excel"""
    print('-----------------------------------------------------')
    print(model)
    

def linearProgramSolver(csv_name, type, eval_expr, direction, model_name, with_scores):
    
    df_score, coeff_list, df_criteria_list, df_criteria_bareme, dict_boundaries = loadModel(csv_name, type)
    
    nb_criteria = len(df_criteria_list.columns)
    
    # variables definition
    variable_list={}
    variable_list_x, variable_list_y  = buildVariableDefinitionList(df_criteria_list, df_criteria_bareme, with_scores, dict_boundaries)
    variable_list['variable_list_x'] = variable_list_x
    variable_list['variable_list_y'] = variable_list_y
    
    # constraint definition
    constraint_list = buildConstraintDefinitionList(coeff_list, variable_list, nb_criteria, df_score, with_scores)
    
    #objective definition
    for var in variable_list_x + variable_list_y:
        if var.name == eval_expr:
            obj = Objective(var, direction)
        
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
    
    print('status: ', model.status)
    print('objective value: ', model.objective.value)
    print('----------------------')
    
    for var_name, var in model.variables.items():
        print(var_name,'=',var.primal)   
    
def buildVariableDefinitionList(df_criteria_list, df_criteria_bareme, with_scores, dict_boundaries):
    """
    Construction des variable du modèle
        
    Args:
        df_criteria_list: le dataFrame contenant les critères qualitatifs
        df_criteria_bareme: le dataFrame contenant les critères avec leurs bornes respectives
        with_scores: utilisation des notes ou non
        dict_boundaries: le min et le max des barèmes (0 et 20)
        
    
    Return: les listes de variables x et y
    """
    i=0
    variable_list_x = []
    variable_list_y = []
    for idx, row in df_criteria_bareme.iterrows():
        for criteria in df_criteria_list.iloc[:,1:]:
            i+=1
            var_x = Variable (f'x{i}', lb=row[f'Min_value_{criteria}'], ub = row[f'Max_value_{criteria}'])
            variable_list_x.append(var_x)
            
    if not with_scores:
        for idx, row in df_criteria_bareme.iterrows():
            var_y = Variable (f'y{idx+1}', lb = dict_boundaries['min'], ub = dict_boundaries['max'])
            variable_list_y.append(var_y)
        
    return variable_list_x, variable_list_y

def buildConstraintDefinitionList(coeff_list, variable_list, nb_criteria, df_score, with_scores):
    
    constraint_list = []
    constraint_num = 0
    for var_num in range(1,len(variable_list['variable_list_x']),nb_criteria-1):
        var_index = var_num
        list_of_parameter=list() 
        for i in range(0, nb_criteria-1):
           coeff_var = (coeff_list[i], variable_list['variable_list_x'][var_index-1])
           list_of_parameter.append(coeff_var)
           var_index+=1
        if not with_scores:
            constraint_list.append(createConstraint(list_of_parameter, constraint_num, variable_list_y = variable_list['variable_list_y'][constraint_num]))
        else:
            constraint_list.append(createConstraint(list_of_parameter, constraint_num, score = df_score[constraint_num]))
        constraint_num += 1
    
    if not with_scores:
        constraint_list += createScoreConstraint(df_score, variable_list['variable_list_y'], constraint_num)
    return constraint_list
               
def createConstraint(list_of_parameter, constraint_num, score=None, variable_list_y=None):
        
    list_expr = []
    for t in list_of_parameter:
        expr = t[0]* t[1]
        list_expr.append(expr)
    
    expr = list_expr[0]
    for exp in list_expr[1:]:
        expr += exp

    if score != None:
        constraint = Constraint(expr, name=f'c{constraint_num+1}', lb = score, ub = score)
    else:
        constraint = Constraint(expr-variable_list_y, name=f'c{constraint_num+1}', lb = 0, ub = 0)
        
    return constraint            

def createScoreConstraint(df_score, variable_list_y, constraint_num):
    
    scoreContraints = []
    for i in range(len(df_score)-1):
        if df_score.iloc[i] != df_score.iloc[i+1]:
            scoreContraints.append(Constraint(variable_list_y[i] - variable_list_y[i+1], name=f'c{constraint_num+i+1}', lb = 0.1))
        else: 
            scoreContraints.append(Constraint(variable_list_y[i] - variable_list_y[i+1], name=f'c{constraint_num+i+1}', lb = 0, ub = 0))
    return scoreContraints
    
    

