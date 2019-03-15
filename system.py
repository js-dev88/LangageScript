from optlang import Model, Variable, Constraint, Objective
from loader import loadModel, parseDataframe
import pandas as pd
import math
from scipy.stats import spearmanr,kendalltau

def checkAdditiveModel(csv_name, eval_expr, direction, model_name, type='excel', with_scores=False, update_model=None):
    
    df = loadModel(csv_name, type)
    if eval_expr != 'all':
        model, df_criteria_list = linearProgramSolver(df, eval_expr, direction , model_name, with_scores, update_model)       
        if model.status == 'infeasible':
            result = f'Le {model.name} du fichier {csv_name} n\'admet pas de solution'  
        else:
            result = displayModel(model, df_criteria_list)
    else:      
        result = displayAllProductMaxScore(df, direction , model_name, update_model)
            
    return result
    
def displayAllProductMaxScore(df, direction , model_name, update_model):
    
    all_results = None
    for i in range(len(df['Produit'])):
         model, df_criteria_list = linearProgramSolver(df, f'y{i+1}', direction, model_name,False, update_model) 
         result = displayModel(model, df_criteria_list)
         if all_results is None:
             all_results = pd.DataFrame(columns=result.columns)
         all_results = all_results.append(result.iloc[i])
         
    return all_results
    
        
def linearProgramSolver(df, eval_expr, direction, model_name, with_scores = False, update_model=None):
    df_score, coeff_list, df_criteria_list, df_criteria_bareme, dict_boundaries = parseDataframe(df)
    nb_criteria = len(df_criteria_list.columns)-1
    
    # variables definition
    variable_list={}
    variable_list_x, variable_list_y  = buildVariableDefinitionList(df_criteria_list, df_criteria_bareme, with_scores, dict_boundaries)
    variable_list['variable_list_x'] = variable_list_x
    variable_list['variable_list_y'] = variable_list_y
    
    #Modification des variables si nécessaire
    if update_model is not None:
        variable_list = update_variable_list_from_dict(update_model['variable'], variable_list)
    # constraint definition
    constraint_list = buildConstraintDefinitionList(coeff_list, variable_list, nb_criteria, df_score, with_scores)
    
    #Modification des contraintes si nécessaire
    if update_model is not None:
        constraint_list = update_constraint_list_from_dict(update_model['constraint'], constraint_list)
        
    #objective definition
    for var in variable_list_x + variable_list_y:
        if var.name == eval_expr:
            obj = Objective(var, direction)
        
    #Model
    model = buildModel(constraint_list, obj, model_name) 
    
    return model, df_criteria_list 

def update_variable_list_from_dict(update_model, variable_list):
    if len(update_model['upd']) > 0:
        for var_to_update in update_model['upd']:
            for k, v in variable_list.items():
                for idx, var in enumerate(v):
                    if var_to_update.name == var.name:
                        v[idx] = var_to_update
                        
    return variable_list
                    
def update_constraint_list_from_dict(update_model, constraint_list):
    if len(update_model['del']) > 0:
        for constraint_to_del in update_model['del']:
            for constraint in constraint_list:
                if constraint_to_del == constraint.name:
                   constraint_list.remove(constraint)
                    
    return constraint_list
    
def buildModel(constraint_list, obj, model_name):
    
    model = Model(name = model_name)
    model.objective = obj
    model.add(constraint_list)
    model.optimize() 
    
    return model

def displayModel(model, df_criteria_list):
    
    col_names = list(df_criteria_list)
    display_df  = pd.DataFrame(columns = col_names)
    display_df.iloc[:,0] = df_criteria_list.iloc[:,0]
    nb_criterias = len(col_names)-1
    
    variable_result_list = []
    
    for var_name, var in model.variables.items():
        variable_result_list.append((var_name,var.primal))
    
    variable_result_list.sort(key=lambda x: (x[0][0],int(x[0][1:])))
    k=0
    for i in range(0, len(df_criteria_list)*nb_criterias,nb_criterias):
        temp_list = []
        for j in range (nb_criterias):
            temp_list.append(variable_result_list[i+j][1])
        display_df.iloc[k,-nb_criterias:] = temp_list
        k+=1
        
    scores_list = variable_result_list[-len(df_criteria_list):]
    scores_list = [i[1] for i in scores_list]
    display_df['Score'] = pd.Series(scores_list)
    
    return display_df
   
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
    for var_num in range(1,len(variable_list['variable_list_x']),nb_criteria):
        var_index = var_num
        list_of_parameter=list() 
        for i in range(0, nb_criteria):
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
    
def createUpdateModel(variable_list, constraint_name_list):
      
    update_model = {}
    update_model['variable'] = {}
    update_model['constraint'] = {}
    update_model['variable']['upd'] = variable_list
    update_model['constraint']['del'] = constraint_name_list
   
    return update_model

def compareRankings(score_df1, score_df2):
    result = {}
    result['coef'], result['p'] = spearmanr(score_df1, score_df2)
    result['tau'],result['p_val'] = kendalltau(score_df1, score_df2)
    print(result)
    return result

