import numpy as np
import pandas as pd
import json
import csv
data_file = open("data_file.txt","a")#append 
new_word=open("new word.txt","a")

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
    sen_lst=sen.split()
    for word in word_data:
        if word[0] in sen_lst:
            sen_lst.remove(word[0])
            rank = rank + int(word[1])
    data_file.write(sen+":"+str(rank)+"\n")
    for wrd in sen_lst:
        np.append(word_data,[wrd,rank])
        new_word.write(wrd+"\t"+str(rank))
    sentence_rank.append([sen,rank])
for i in word_data:
    print(i)

# for sen_rank in sentence_rank:
#     print(sen_rank[0]+":"+str(sen_rank[1]))
# data_file.close()