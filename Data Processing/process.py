import os

'''
merge = ["KSHV infection", "Huntington's Disease (HD)", "lung adenocarcinoma (NCI_Thesaurus C0152013)",
         "with wildtype Streptococcus pyogenes", "B-cell lymphoma", "breast tumor"]

merge = ["Huntington's", "lung adenocarcinoma (NCI_Thesaurus C0152013)",
         "B-cell lymphoma", "breast tumor"]'''

dict = {}
dict_gene = {}

with open("disease_gene.txt", "r") as f3:
    lines = f3.readlines()
    for l in lines:
        flag = False
        line = l[:-1].split('\t')
        tmp = line[0]
        for m in merge:
            if (m in tmp):
                tmp = m
                break
        if (not tmp in dict_gene):
            dict_gene[tmp] = []
        for i in line[1:]:
            dict_gene[tmp].append(eval(i))

with open("disease_num.txt","r") as f:
    lines = f.readlines()
    for l in lines:
        line = l[:-1].split('\t')
        tmp = line[0]
        for m in merge:
            if (m in tmp):
                tmp = m
                break
        if (tmp in dict):
            dict[tmp] = dict[tmp] + eval(line[1])
        else:
            dict[tmp] = eval(line[1]);

t = 0
k = 0
'''with open("disease_merge.txt", "w") as f2:
    for item in dict:
        if (dict[item] >= 10):
            t += 1
            k += dict[item]
            print(item)
            f2.write(item+'\t')
            for i in range(len(dict_gene[item])):
                if (i < len(dict_gene[item])-1):
                    f2.write(str(dict_gene[item][i])+'\t')
                else:
                    f2.write(str(dict_gene[item][i])+'\n')

f2.close() '''
for item in dict:
    if (dict[item] >= 50):
        t += 1
        k += dict[item]
        print(item)

#f2.close()

print(t)
print(k)






