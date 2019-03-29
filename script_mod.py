import numpy as np
import pandas as pd
import json
data_file = open("data_file.txt","a",encoding="utf-8")#append

sentences=[]
with open('salida_tweets.txt') as file:
    for line in file:
        line=json.loads(line)
        if "delete" not in line.keys():
            sentences.append(line["text"])
word_data = pd.read_csv('Sentimientos.txt',sep="\t",encoding="utf-8")

word_data=np.array(word_data)
sentence_rank=[]
new_word=[]
new_word_lst=[]

for sen in sentences:
    rank=0
    sen_lst=sen.split()
    for word in word_data:
        if word[0] in sen_lst:
            sen_lst.remove(word[0])
            rank = rank + int(word[1])

    for wrd in sen_lst:
        if wrd not in new_word:
            new_word.append(wrd)
            new_word_lst.append([wrd, rank])
    sentence_rank.append([sen,rank])
    data_file.write(sen + ":" + str(rank) + "\n")
for ranks in sentence_rank:
    print(ranks)

add_to_file=open('Sentimientos.txt','a',encoding="utf-8")
for i in new_word_lst:
    add_to_file.write(i[0]+" "+str(i[1])+"\n")
add_to_file.close()