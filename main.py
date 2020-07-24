# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:05:09 2020

@author: siddarthaThentu
"""

from utils_pos import preprocess
from createDictionaries import create_dictionaries
from createMatrices import create_transition_matrix,create_emission_matrix
from computeAccuracy import compute_accuracy
from viterbi import initialize,forward,backward

import pandas as pd

#load training corpus
with open("WSJ_02-21.pos","r") as fp:
    training_corpus = fp.readlines()

print(f"A few items of the training corpus list\n")
print(training_corpus[0:5])

#load vocabulary
with open("hmm_vocab.txt","r") as fp:
    vocab_list = fp.read().split("\n")

print("\nA few words of the vocabulary\n")
print(vocab_list[0:50])
print()
print("\nA few items at the end of vocabulary\n")
print(vocab_list[-50:])

vocab = {}

for i,word in enumerate(sorted(vocab_list)):
    vocab[word]=i

#load test corpus
with open("WSJ_24.pos","r") as fp:
    y = fp.readlines()

print("\nA sample of test corpus\n")
print(y[0:10])

#preparing the test corpus
_,prep = preprocess(vocab,"test.words")

print("\nThe length og preprocessed test corpus:",len(prep))
print("\nThis is a sample of test corpus:\n")
print(prep[0:10])

emission_counts,transition_counts,tag_counts = create_dictionaries(training_corpus,vocab)

states = sorted(tag_counts.keys())
print("\nNumber of POS tags or Number of states : ",len(states))
print("\nPrinting those states:\n")
print(states)

alpha = 0.001

A = create_transition_matrix(alpha,tag_counts,transition_counts)
print("\nView of a subset of transition matrix A")
print(pd.DataFrame(A[30:35,30:35],index=states[30:35],columns=states[30:35]))

B = create_emission_matrix(alpha,tag_counts,emission_counts,list(vocab))

best_probs,best_paths = initialize(states,tag_counts,A,B,prep,vocab)
#print(best_probs.shape)
best_probs,best_paths = forward(A,B,prep,best_probs,best_paths,vocab)

pred = backward(best_probs,best_paths,prep,states)

accuracy = compute_accuracy(pred,y)

print("Accuracy of the algorithm is ",accuracy*100,'%')

print("sample predictions\n")

print('The prediction for pred[-7:m-1] is: \n', prep[-7:len(prep)-1], "\n", pred[-7:len(prep)-1], "\n")
print('The prediction for pred[0:8] is: \n', pred[0:7], "\n", prep[0:7])














