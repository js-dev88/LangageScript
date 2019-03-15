#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:53:38 2019

@author: ikrambouhya
"""


def comparesTo(a,b): # cette fonction retourne "True" quand a >= b sinon elle retourne "False"
    comparator=0
    if(a[0]=="+" and b[0]=="+" and len(a)>=len(b)):
        comparator=1
    elif(a[0]=="+" and b[0]=="-"):
        comparator=1
    elif(a[0]=="-" and b[0]=="-" and len(a)<=len(b)): 
        comparator=1
    else: 
        comparator=0
        
    return comparator

def ConcordancePartielleHbi(direction,nb_criteria,df_criteria_list,df_criteria_profils):
    if(direction=="max"):
        for(i in range(0,len(df_criteria_list))):
            for(i in range(0,len(df_criteria_profils))):
                
                