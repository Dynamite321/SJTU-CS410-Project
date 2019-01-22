import torch.utils.data as data
import os
import copy
import random
import torch
import numpy as np

class GeneDataset(data.Dataset):
    def __init__(self, train = True):
        self.set = []
        self.samples = np.load("samples_reduced.npy")
        self.labelOfGene = {}
        index = 0
        label_num = 0
        with open("sex_gene.txt", "r") as f:
            lines = f.readlines()
            for l in lines:
                line = l[:-1].split('\t')
                new_line = copy.deepcopy(line[1:])
                length = int(0.5 + 0.8 * len(line[1:]))
                if (train):
                    random.shuffle(new_line)
                    print(new_line)
                    for i in range(1, length):
                        self.set.append(self.samples[eval(new_line[i-1])])
                        if (not index in self.labelOfGene):
                            self.labelOfGene[index] = label_num
                        index += 1
                    label_num += 1
                else:
                    for i in range(length, len(line[1:])):
                        self.set.append(self.samples[eval(line[i])])
                        if (not index in self.labelOfGene):
                            self.labelOfGene[index] = label_num
                        index += 1
                    label_num += 1
            #print(self.labelOfGene)

    def __getitem__(self, index):
        gene = torch.from_numpy(self.set[index]).float()
        label = self.labelOfGene[index]
        return gene, label

    def __len__(self):
        return len(self.set)

