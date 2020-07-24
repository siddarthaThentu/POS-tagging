# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:24:50 2020

@author: siddarthaThentu
"""

import numpy as np
import math

def initialize(states,tag_counts,A,B,corpus,vocab):
    
    num_tags = len(tag_counts)
    
    #initialzize best_probs matrix
    best_probs = np.zeros((num_tags,len(corpus)))
    best_paths = np.zeros((num_tags,len(corpus)),dtype=int)
    
    s_idx = states.index("--s--")
    
    for i in range(num_tags):
        if(A[s_idx,i])==0:
            best_probs[i,0] = float('-inf')
        else:
            best_probs[i,0] = math.log(A[s_idx,i]) + math.log(B[i,vocab[corpus[0]]])
    
    return best_probs,best_paths

def forward(A,B,test_corpus,best_probs,best_paths,vocab):
    
    num_tags = best_probs.shape[0]
    #num_words = best_probs.shape[1]
    
    for i in range(1,len(test_corpus)): 
        if(i%5000==0):
            print("Words processed : ",i)
        for j in range(num_tags):
            best_prob_i = float("-inf")
            index = None
            for k in range(num_tags):
                best_prob = best_probs[k][i-1]+math.log(A[k][j])+math.log(B[j][vocab[test_corpus[i]]])
                if(best_prob>best_prob_i):
                    best_prob_i = best_prob
                    index = k
            #print(i,j)
            best_probs[j,i] = best_prob_i
            best_paths[j,i] = index
            
    return best_probs,best_paths

def backward(best_probs,best_paths,corpus,states):

    num_words = best_paths.shape[1]
    num_tags = best_paths.shape[0] 
    z = [0]*num_words
    pred = ['']*num_words
    
    best_prob_for_last_word = float('-inf')
    
    for i in range(num_tags):
        if(best_probs[i][num_words-1]>best_prob_for_last_word):
            best_prob_for_last_word = best_probs[i][num_words-1]
            z[num_words-1] = i
    pred[num_words-1] = states[z[num_words-1]]
    
    for i in range(num_words-1,0,-1):
        pos_tag_for_word_i = best_paths[z[i],i]
        z[i-1] = pos_tag_for_word_i
        pred[i-1] = states[z[i-1]]
        
    return pred
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        