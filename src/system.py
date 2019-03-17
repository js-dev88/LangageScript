from loader import loadModel, parseDataframe
import pandas as pd
from scipy.stats import spearmanr,kendalltau
from optlang import Model, Variable, Constraint, Objective

def checkAdditiveModel(csv_name, eval_expr, direction, model_name, type='excel', with_scores=False, update_model=None):
    """
    Résolution du programme linéaire
        
    Args:
        csv_name : path du fichier de données (répertoire data)
        eval_expr: variable de la fonction objectif ou 'all' pour appliquer direction à toutes les variables
        direction: min / max  variables 
        model_name: nom du modèle
        type: excel par défaut, 'csv' possible
        with_scores : mode avec ou sans score (Q2 / Q3 / Q4)
        update_model : liste des éléments pou la suppression / modification de contraintes
        
    
    Return: message d'erreur si pas de solution
            Dataframe avec les résultats corespondants dans la colonne score
            Cas max al (Q4) Dataframe avec toutes les solutions correspondants 
            au max des variables dans la colonne score
    """
    
    df = loadModel(csv_name, type)
    if eval_expr != 'all':
        model, df_criteria_list = linearProgramSolver(df, eval_expr, direction , model_name, with_scores, update_model)       
        if model.status == 'infeasible':
            result = f'Le {model.name} \n du fichier {csv_name} n\'admet pas de solution'  
        else:
            result = displayModel(model, df_criteria_list)
    else:      
        result = displayAllProductMaxScore(df, direction , model_name, update_model)
            
    return result
    
def displayAllProductMaxScore(df, direction , model_name, update_model):
    """
    Construction du Dataframe de la question 4
        
    Args:
        df : Dataframe original issu du fichier excel
        direction: min / max  variables
        model_name: nom du modèle
        update_model : liste des éléments pou la suppression / modification de contraintes
        
    
    Return: Renvoie un Dataframe prêt à être exporter / afficher
    """
    all_results = None
    for i in range(len(df['Produit'])):
         model, df_criteria_list = linearProgramSolver(df, f'y{i+1}', direction, model_name,False, update_model) 
         result = displayModel(model, df_criteria_list)
         #Construction du dataframe pour la preière variable
         if all_results is None:
             all_results = pd.DataFrame(columns=result.columns)
         #Insertion du score max pour la variable dans le dataframe
         all_results = all_results.append(result.iloc[i])
         
    return all_results
    
        
def linearProgramSolver(df, eval_expr, direction, model_name, with_scores = False, update_model=None):
    """
    Construction et résolution du programme linéaire hors question 4
        
    Args:
        df : Dataframe original issu du fichier excel
        eval_expr: variable de la fonction objectif ou 'all' pour appliquer direction à toutes les variables
        direction: min / max  variables
        model_name: nom du modèle
        with_scores : mode avec ou sans score (Q2 / Q3 / Q4)
        update_model : liste des éléments pou la suppression / modification de contraintes
        
    
    Return: Renvoie un Dataframe prêt à être exporter / afficher
    """
    df_score, coeff_list, df_criteria_list, df_criteria_bareme, dict_boundaries, _, _, _= parseDataframe(df)
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
            obj = Objective(expression=var, direction=direction)
        
    #Model
    model = buildModel(constraint_list, obj, model_name) 
    
    return model, df_criteria_list 

def update_variable_list_from_dict(update_model, variable_list):
    """
    Met à jours les contraintes portant sur les bornes des variables exemple : 17 < xc2
    Ne fonctionne qu'en mode mis à jour (nous n'utilisons pas le mode de suppression)
        
    Args:
        update_model : dict avec la modification (nouvel objet Variable cf Main)
        variable_list: listes variables existantes

    Return: la liste des variables mise à jour
    """
    if len(update_model['upd']) > 0:
        for var_to_update in update_model['upd']:
            for k, v in variable_list.items():
                for idx, var in enumerate(v):
                    if var_to_update.name == var.name:
                        v[idx] = var_to_update
                        
    return variable_list
                    
def update_constraint_list_from_dict(update_model, constraint_list):
    """
    Supprime des contraintes de la liste 
        
    Args:
        update_model : dict avec la modification (liste des contraintes à supprimer)
        constraint_list: listes contraintes existantes

    Return: la liste des contraintes mise à jour
    """
    if len(update_model['del']) > 0:
        for constraint_to_del in update_model['del']:
            for constraint in constraint_list:
                if constraint_to_del == constraint.name:
                   constraint_list.remove(constraint)
                    
    return constraint_list
    
def buildModel(constraint_list, obj, model_name):
    """
    Construit le model et l'excute pour le résoudre
    En décommentant les lignes, il est possible d'afficher les élements constitutifs d'un modèle (debug)
        
    Args:
        constraint_list : listes contraintes existantes
        obj: fonction objectif
        model_name: nom du model

    Return: l'objet modèle
    """
    model = Model(name = model_name)
    model.objective = obj
    model.add(constraint_list)
    model.optimize() 
    #Print du modèle pour débug
#    for cons in model.constraints.items():
#        print(cons[1])
#    for var in model.variables.items():
#        print(var)
    return model

def displayModel(model, df_criteria_list):
    """
    Construit un dataframe prêt à être exporter / afficher
        
    Args:
        model : Un objet Model
        df_criteria_list: liste des critères du classement

    Return: un dataframe de résultats
    """
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
    #Mode sans les scores : on rajoute les variables de score       
    if not with_scores:
        for idx, row in df_criteria_bareme.iterrows():
            var_y = Variable (f'y{idx+1}', lb = dict_boundaries['min'], ub = dict_boundaries['max'])
            variable_list_y.append(var_y)
        
    return variable_list_x, variable_list_y

def buildConstraintDefinitionList(coeff_list, variable_list, nb_criteria, df_score, with_scores):
    """
    Construction des contraintes du modèle
        
    Args:
        coeff_list : liste des coefficients
        variable_list: liste des variables
        nb_criteria: nombre de critères
        df_score: liste des scores
        with_scores: mode avec ou sans score 
        
    
    Return: les listes des contraintes du modèle
    """
    
    constraint_list = []
    constraint_num = 0
    for var_num in range(1,len(variable_list['variable_list_x']),nb_criteria):
        var_index = var_num
        list_of_parameter=list() 
        for i in range(0, nb_criteria):
           coeff_var = (coeff_list[i], variable_list['variable_list_x'][var_index-1])
           list_of_parameter.append(coeff_var)
           var_index+=1
        #Mode sans les scores, on modifie les contraintes de base
        if not with_scores:
            constraint_list.append(createConstraint(list_of_parameter, constraint_num, variable_list_y = variable_list['variable_list_y'][constraint_num]))
        else:
            constraint_list.append(createConstraint(list_of_parameter, constraint_num, score = df_score[constraint_num]))
        constraint_num += 1
    #Mode sans les scores, on rajoute les contraintes d'égalités et d'inégalités entre les variables de scores
    if not with_scores:
        constraint_list += createScoreConstraint(df_score, variable_list['variable_list_y'], constraint_num)
    return constraint_list
               
def createConstraint(list_of_parameter, constraint_num, score=None, variable_list_y=None):
    """
    Constructeur de contraintes
    
    Args:
        list_of_parameter : listes des paramètres (0.4 * x1, 0.6 * x2 ect...)
        constraint_num: numéro de la contrainte
        score: forme de la contrainte (avec ou sans score)
        variable_list_y: liste des variables de score (y1 = fa)
        
    Return: la contrainte
    """   
    list_expr = []
    for t in list_of_parameter:
        expr = t[0]* t[1]
        list_expr.append(expr)
    
    expr = list_expr[0]
    for exp in list_expr[1:]:
        expr += exp
    #Construit la contrainte en fonction du mode avec ou sans score
    if score != None:
        constraint = Constraint(expr, name=f'c{constraint_num+1}', lb = score, ub = score)
    else:
        constraint = Constraint(expr-variable_list_y, name=f'c{constraint_num+1}', lb = 0, ub = 0)
        
    return constraint            

def createScoreConstraint(df_score, variable_list_y, constraint_num):
    """
    Constructeur de contraintes de score (égalité et inégalité entre les différents score de produits)
    
    Args:
        df_score : la colonne des score
        variable_list_y: liste de variables correspondant au score (y1 = fa)
        constraint_num: Numéro de la contrainte
        variable_list_y: liste des variables de score
        
    Return: la liste des contraintes portant sur les scores
    """   
    scoreContraints = []
    for i in range(len(df_score)-1):
        if df_score.iloc[i] != df_score.iloc[i+1]:
            scoreContraints.append(Constraint(variable_list_y[i] - variable_list_y[i+1], name=f'c{constraint_num+i+1}', lb = 0.1))
        else: 
            scoreContraints.append(Constraint(variable_list_y[i] - variable_list_y[i+1], name=f'c{constraint_num+i+1}', lb = 0, ub = 0))
    return scoreContraints
    
def createUpdateModel(variable_list, constraint_name_list):
    """
    Crée un dict avec la liste des variables et des contraintes à mettre à jour / supprimer
    
    Args:
        variable_list : liste des variables passées en paramètre pour mise à jour
        constraint_name_list: liste des contraintes à supprimer
       
        
    Return: le dict correctement formé
    """     
    update_model = {}
    update_model['variable'] = {}
    update_model['constraint'] = {}
    update_model['variable']['upd'] = variable_list
    update_model['constraint']['del'] = constraint_name_list
   
    return update_model

def compareRankings(score_df1, score_df2):
    """
    calcule les indicaeurs sur es classements pour le programme linéaire correspondant
    Spearman, Kendall et la différence moyenne
    Affiche les résultats en console
    
    Args:
        score_df1 : Dataframe Original
        score_df2: Dataframe à comparer (issu du modèle)
       
        
    Return: le dict de résultat prêt à être exporté / affiché
    """    
    result = {}
    result['coef - Spearman'], result['p - Spearman'] = spearmanr(score_df1, score_df2)
    result['tau - Kendall'],result['p_val - Kendall'] = kendalltau(score_df1, score_df2)
    result['Diff Moyenne'] = (score_df2.sum() - score_df1.sum()) / len(score_df1)
    print(result)
    return result

