from numpy import loadtxt
import random
import math
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import pandas as pd 
import re
from sklearn import (datasets, svm, metrics)
from sklearn.cluster import KMeans

nltk.download('punkt')
nltk.download('stopwords')

# 불용어를 생성한다.
stop_words = set(stopwords.words('english')) 
stop_words.update([',', '.','http', ':', ')', ';', '?', '!', '@', 'https', 'youtube.com', '%', '2018', '2019'])

# pandas를 통해 csv파일을 불러와서 저장한다.
elon = pd.read_csv('/datasets/elonmusk.csv')
elon.drop(["Tweet", "UserScreenName", "UserName", "Emojis", "Comments", "Likes", "Retweets", "Image link", "Tweet URL"], axis=1, inplace=True)

# 데이터프레임을 리스트 형식으로 변환한다
elon_list = elon.values.tolist()

# Patterns for RE
replying_pattern = 'replying'
tech_words = '\n[a-z]*'

# 트윗을 전처리하여 Bag-of-Words 카운트를 통해 빈도수를 수치화한다.
def BagOfWords(docs):
    doc_tokenized = []
    doc_words = []
    for tweet in docs :
        doc_tokenized = word_tokenize(tweet)
        for w in enumerate(doc_tokenized):
            if w not in stop_words:
                doc_words.append(w)
    

    # 단어 집합(Vocabulary)
    vocab = {}
    # BoW 벡터
    bow = []
    
    for word in doc_words:
        # 처음 나온 단어인 경우
        if word not in vocab.keys():
            # 단어가 등장한 순서를 정수 인덱스로 부여
            vocab[word] = len(vocab)
            # 처음 등장한 단어이므로 BoW에 1 부여
            bow.append(1)
            
        # 출현 이력이 있는 단어의 경우
        else:
            # 해당 단어의 인덱스 찾기
            word_index = vocab.get(word)
            # 등장 횟수 1 증가
            bow[word_index]+=1

    # print(vocab.items())
    return vocab, bow

def pre_process(tweet_list):
    processed_list = []
    for index, (timestamp, text) in enumerate(tweet_list):
         text = text.lower()
         if re.match(replying_pattern, text):
             continue
         else:
             processed_list.append(text)
    return processed_list

# 트윗의 전처리 과정을 수행한다. 
tweet_list_processed = pre_process(elon_list)

vocab, bow = BagOfWords(tweet_list_processed)
reverse_vocab= dict(map(reversed,vocab.items()))

# 가장 높은 BOW 값을 가지는 단어들을 저장한다.
top_index = []
top_words = []

for i in range(len(bow)):
    if bow[i] > 5:
        # print(bow[i])
        top_index.append(i)
    else:
        continue

# print(top_index)

for i in range(len(top_index)):
    a = reverse_vocab.get(top_index[i])
    top_words.append(a[1])

for i in range(len(top_words)):
    if top_words[i] not in stop_words:
        print("TOP WORDS: ")
        print(top_words[i])
        print("COUNTS : ")
        print(bow[top_index[i]])
        print("----------------------") 
        print("\n")






