# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 08:36:15 2020

@author: siddarthaThentu
"""

def compute_accuracy(pred,y):
    
    num_correct = 0
    total = 0
    
    for prediction,y in zip(pred,y):
        word_tag_tuple = y.split()
        if(len(word_tag_tuple)!=2):
            continue
        word,tag = word_tag_tuple
        if(tag==prediction):
            num_correct+=1
        total+=1
        
    return num_correct/total