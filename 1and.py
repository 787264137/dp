# -*- coding:utf-8 -*-
import os

all1_name = []
all1_features = []
alter_name = []
alter_features = []

with open("data_7.24//1_and_all.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        name, features = line.split("|")
        all1_name.append(name)
        all1_features.append(features)
with open("data_7.24//1_and_wrong.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        name, features = line.split("\t")[0], "".join(line.split('\t')[1:])
        alter_name.append(name)
        alter_features.append(features)

and1_not_wrong_name = []
and1_not_wrong_features = []
for i in range(len(all1_name)):
    if all1_name[i] not in alter_name:
        and1_not_wrong_name.append(all1_name[i])
        and1_not_wrong_features.append(all1_features[i])

for i in range(len(and1_not_wrong_name)):
    words_lst = and1_not_wrong_features[i].split(" ")
    for i in range(len(words_lst)):
        if words_lst[i] == "and":
            words_lst[i] = '\t'
    last_feature = ' '.join(words_lst)
    print and1_not_wrong_name[i] + '\t' + last_feature.strip()