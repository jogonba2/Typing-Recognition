#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" usuario(clase)_entrada """

from sklearn.svm import LinearSVC
import pickle
from os import listdir
import numpy as np
import GenerateSample

## Entrenar SVM o cargar ya entrenado ##
train_files = listdir("./Corpus/Train")
XT,YT       = [],[]

for t in train_files:
    yT = t[:t.find("_")]
    with open("./Corpus/Train/"+t,"rb") as fd: xT = pickle.load(fd)
    XT.append(np.array(xT)) ; YT.append(yT)
    
svm = LinearSVC()
svm.fit(XT,YT)
##################

v = GenerateSample._generateSample()
GenerateSample._clear()
print "\nEres el usuario: ",svm.predict([v])


