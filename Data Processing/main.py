import os

dict_num = {}
dict_gene = {}

num = 0

with open("Gene_Chip_Data/E-TABM-185.sdrf.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    tags = lines[0][:-1].split('\t')
    for i in range(len(tags)):
        if (tags[i] == "Characteristics [Sex]"):
            index = i
            print(index)
            break
    t = 0
    total = 0
    for l in lines[1:]:
        line = l[:-1].split('\t')
        if (line[index] != '  '):
            total += 1
            tmp = line[index]
            if (line[index] in dict_num):
                dict_num[tmp] = dict_num[tmp] + 1
                dict_gene[tmp].append(t)
            else:
                dict_num[tmp] = 1
                dict_gene[tmp] = [t]
                num += 1
        t += 1

print("num:", num)
print("t:", t)
print("total",total)

with open("sex_num.txt", "w") as f2:
    for item in dict_num:
        f2.write(item+'\t'+str(dict_num[item])+'\n')
    f2.close()

with open("sex_gene.txt", "w") as f3:
    for item in dict_gene:
        f3.write(item+'\t')
        for i in range(len(dict_gene[item])):
            if (i < len(dict_gene[item]) - 1):
                f3.write(str(dict_gene[item][i])+'\t')
            else:
                f3.write(str(dict_gene[item][i])+'\n')

    f3.close()









