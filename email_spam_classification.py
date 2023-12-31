# -*- coding: utf-8 -*-
"""Email_spam_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FH6_jpfFtnZGNpYMMwe8pWe1p8rjcBf4
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df=pd.read_csv("/content/drive/MyDrive/Dataset/email_spam.csv")

df.head()

df.shape

df.groupby('type').describe()

x=df['text']
y=df['label']

x_train,x_val,y_train,y_val=train_test_split(x,y,test_size=0.2,random_state=16,stratify=y)
x_val,x_test,y_val,y_test=train_test_split(x_val,y_val,test_size=0.2,random_state=16,stratify=y_val)

x_train.shape,y_train.shape,x_val.shape,y_val.shape,x_test.shape,y_test.shape

v=CountVectorizer()
x_train_count=v.fit_transform(x_train.values)
x_train_count.toarray()

model=MultinomialNB()
model.fit(x_train_count,y_train)

emails=['Upto 20% discont on parking, exclusive offer just for you. Dont miss this reward!']
emails_count=v.transform(emails)
model.predict(emails_count)

x_test_count=v.transform(x_test)
model_score=model.score(x_test_count,y_test)
print("Test Accuracy : ",model_score)

s=['Congratulations, you won']
s=v.transform(s)
model.predict(s)