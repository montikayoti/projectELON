# projectELON (Extraction on keywords from Elon Musk's Tweets)

## Goal 
일론 머스크의 트위터 자료(Kaggle)를 나온 단어들의 빈도수를 측정하여 그가 가장 많이 언급한 내용들에 대한 대략적인 짐작을 해본다.

## 동작방식
동작방식은 굉장히 간단하다.

1) Kaggle로부터 https://www.kaggle.com/datasets/kulgen/elon-musks-tweets (Elon Musk's Tweets) 데이터셋을 불러와 필요한 데이터 정제를 진행한다. 
2) Data Preprocessing을 진행한다. 
  2-1) 텍스트를 소문자화한다.
  2-2) 이 프로젝트에서 다른 사람의 영향을 최소화하기 위해서, 일론 머스크가 누군가의 언급에 대한 답장으로써 작성한 트윗은 제외하고, 오로지 그가 자발적으로 올린 트윗만을 고려하고자 했다. 
  그러므로, 답장으로서의 트윗들은 제거한다.
  2-3) 토큰화 (Tokenization)
  2-4) 여러가지 케이스들의 불용어(STOPWORDS)들을 제거한다.
3) BOW(Bag-of-Words) 프로세스를 진행한다.

## Result
코드실행 후 아래와 같은 결과들이 출력되었다.

![result1](https://user-images.githubusercontent.com/89559437/170848608-6874f228-e2bb-47e1-bfd6-66cd7aa1a707.png)

![result2](https://user-images.githubusercontent.com/89559437/170848609-2037ef3f-7e97-4d4a-861e-f5438f8fee93.png)

![result3](https://user-images.githubusercontent.com/89559437/170848610-6ebe53c6-88d9-45f9-8695-3835b9dc8be6.png)
