# -*- coding: utf-8 -*-
import os
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import random

def read_raw_data():
    with open("./Gene_Chip_Data/microarray.original.txt",'r',encoding='utf-8') as f_in:
        lines=f_in.readlines()
        samples=lines[0][:-1].split('\t')[1:]  # first line sample name
        samples_feature=np.zeros((len(samples), 22283))
        probe_index=0
        for line in lines[1:]:
            probe_data=line[:-1].split('\t')[1:]
            for i in range(len(probe_data)):
                samples_feature[i][probe_index]=probe_data[i]
            print ("line %d"%probe_index)
            probe_index=probe_index+1
    np.save(os.path.join("samples.npy"),samples_feature)
    print ("Samples saved.")

def features_pca():
    samples_feature=np.load("samples.npy")
    pca=PCA(n_components=0.9)
    pca.fit(samples_feature)
    samples_feat_reduced=pca.transform(samples_feature)
    np.save("samples_reduced.npy",samples_feat_reduced)
    print ("PCA is done and reduced dimension feature data is saved.")

read_raw_data()
features_pca()


