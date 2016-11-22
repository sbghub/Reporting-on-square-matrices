# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:15:51 2016

@author: Somak
"""

import pandas as pda
import numpy as np

def squaremat(csv):  #reads nxn matrix from .csv and provides analysis
    chunk = pda.read_csv(csv, header=None)
    chunk = np.mat(chunk)
    
    evals, evecs = np.linalg.eig(chunk)
    inv = np.linalg.inv(chunk)
    
    #returns eigenvalues, eigenvectors, and the inverse
    return chunk, evals, evecs, inv

def smtxtrep(csv, text): #text report on square matrix
    try:    
        f = open(text, "w")
        
        #runs .csv data through squaremat 
        orig, evals, evecs, inv = squaremat(csv)
        
        #prints the analysis neatly
        f.write('original: \n' + str(orig) +'\n\n')
        f.write('eigenvalues: \n' + str(evals) + '\n\n')
        f.write('eigenvectors: \n' + str(evecs) + '\n\n')
        f.write('inverse: \n' + str(inv))
    finally:
        f.close()

smtxtrep("huh.csv", "what.txt")
