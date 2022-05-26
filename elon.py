from numpy import loadtxt
import random
import math
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import (datasets, svm, metrics)
from sklearn.cluster import KMeans


# pandas를 통해 csv파일을 불러와서 저장하는 부분.
elon = pd.read_csv('/Users/davidshinn/Desktop/ELON/projectELON/datasets/elonmusk.csv')
elon.drop(["Tweet", "UserScreenName", "UserName", "Emojis", "Comments", "Likes", "Retweets", "Image link", "Tweet URL"], axis=1, inplace=True)

# 데이터프레임을 리스트 형식으로 변환 
elon_list = elon.values.tolist()

# print(elon_list)

# 전체 트윗에서 절반을 복사해서 Training Dataset을 만든다.
elon_list_train = [random.choice(elon_list) for i in range(math.floor(len(elon_list)/10))]
print("---------------------this is the training data--------------------------")
# print(elon_list_train)




# data preprocessing part 1
year_2011 = []


# 1. split the tweets by each year
# 2. remove the tweet that's reply to others

def pre_process(text):
    text = text.lower()

    text = re.sub(r'[0-9]*', '', text)

    return text



for index, (timestamp, text) in enumerate(elon_list):
    # for year in ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    text = pre_process(text)
    if re.match(r"2011", timestamp):
        if re.match(r"Replying", text):
            continue
        else: 
            year_2011.append([timestamp, text])

# print(year_2011)

# Tf-Idf Vectorization
tfidf_vec = TfidfVectorizer(max_df = 0.8, stop_words='english')
tfidf = tfidf_vec.fit_transform(elon_list_train)
k_means = KMeans(n_clusters=2).fit(tfidf)

year_2011_text = []
for index, (timestamp, text) in enumerate(year_2011):
    year_2011_text.append(text)
    print(year_2011_text)


# k_means.predict(tfidf_vec.transform(year_2011_text))





    
