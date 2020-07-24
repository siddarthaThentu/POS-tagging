# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:56:43 2020

@author: siddarthaThentu
"""
import numpy as np

def create_transition_matrix(alpha,tag_counts,transition_counts):
    
    all_tags = sorted(tag_counts.keys())
    num_tags = len(all_tags)
    
    #initialize transition matrix "A"
    A = np.zeros((num_tags,num_tags))
    
    for i in range(num_tags):
        for j in range(num_tags):
            key = (all_tags[i],all_tags[j])
            countTransitions = 0
            if key in transition_counts:
                countTransitions = transition_counts[key]
            countTag = tag_counts[all_tags[i]]
            
            A[i,j] = (countTransitions+alpha)/(countTag+num_tags*alpha)
            
    return A
            
                
def create_emission_matrix(alpha,tag_counts,emission_counts,vocab):

    all_tags = sorted(tag_counts.keys())
    num_tags = len(all_tags)
    num_words = len(vocab)
    
    B = np.zeros((num_tags,num_words))
    
    for i in range(num_tags):
        for j in range(num_words):
            key = (all_tags[i],vocab[j])
            countEmissions = 0
            if key in emission_counts:
                countEmissions = emission_counts[key]
            countTag = tag_counts[all_tags[i]]
            
            B[i,j] = (countEmissions+alpha)/(countTag+alpha*num_words)
            
    return B
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
                