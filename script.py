import numpy as np
import pandas as pd
import json
import csv
data_file = open("data_file.txt","a")#append mode

sentences=[]
with open('salida_tweets.txt') as file:
    for line in file:
        line=json.loads(line)
        if "delete" not in line.keys():
            sentences.append(line["text"])
word_data = pd.read_csv('Sentimientos.txt',sep="\t")
word_data=np.array(word_data)
sentence_rank=[]

for sen in sentences:
    rank=0
    for word in word_data:
        if word[0] in sen:
            rank = rank + int(word[1])
    data_file.write(sen+":"+str(rank)+"\n")
    sentence_rank.append([sen,rank])

for sen_rank in sentence_rank:
    print(sen_rank[0]+":"+str(sen_rank[1]))
data_file.close()