# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from xlwt import Workbook
from scipy.stats import spearmanr,kendalltau
from numpy.random import rand
import matplotlib.pyplot as plt


def RankingCompareSpearman(data1,data2): 
    coef, p = spearmanr(data1, data2)
    return coef,p 

def RankingCompareKendall(data1,data2):
    tau,p_val = kendalltau(data1,data2)
    return tau,p_val


'''
Data_Ranking = pd.read_excel('input_couches-2.xlsx',sheet_name ='Feuil1')
Data_RankingQ3 = pd.read_excel('ranking_q3.xls')
Data_RankingQ4 = pd.read_excel('ranking_q4.xls')
rank1 =Data_Ranking['Score'] 
rank2 = Data_RankingQ3['note']
rank3 = Data_RankingQ4['note']



############# SpearMan Q3###############
coef ,p = RankingCompareSpearman(rank1,rank2)
############# Kendall Q3 ################
tau , p_val = RankingCompareKendall(rank1,rank2)


# pour info Coef c'est le coefficient de corrélation 
# p est de uncorrélation 
###################### Spearman Q4  ############
coefQ4 ,pQ4 = RankingCompareSpearman(rank1,rank3)

##################### Kendall Q4 ####################

tauQ4 , p_valQ4 = RankingCompareKendall(rank1,rank3)

'''

