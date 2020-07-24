# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:26:24 2020

@author: siddarthaThentu
"""
from collections import defaultdict
from utils_pos import get_word_tag

def create_dictionaries(training_corpus,vocab):
    
    emission_counts = defaultdict(int)
    transition_counts = defaultdict(int)
    tag_counts = defaultdict(int)
    
    prev_tag = "--s--"
    
    i=0
    
    for word_tag in training_corpus:
        
        i+=1
        #print for every 50,000 words
        if(i%50000==0):
            print(f"Word count = {i}")
        
        word,tag = get_word_tag(word_tag,vocab)
        
        transition_counts[(prev_tag,tag)] += 1
        emission_counts[(tag,word)] += 1
        tag_counts[tag] += 1
        
        prev_tag = tag
        
    return emission_counts,transition_counts,tag_counts
        
    