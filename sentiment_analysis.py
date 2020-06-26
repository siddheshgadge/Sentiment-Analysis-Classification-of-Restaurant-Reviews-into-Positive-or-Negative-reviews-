# -*- coding: utf-8 -*-
"""Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11dtvsOzjlIipeATYB7QF3VIgCwUX3IX6

#Sentiment Analysis (Natural Language Processing)

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('/content/Restaurant_Reviews.tsv',delimiter = '\t',quoting=3)

"""## Cleaning the texts"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(0,dataset.shape[0]):
  review = re.sub('[^^a-zA-Z]',' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  all_stopwords.remove('no')
  # all_stopwords.remove('only')
  # all_stopwords.remove('very')
  # all_stopwords.remove('few')
  # all_stopwords.remove('can')
  all_stopwords.remove('should')
  all_stopwords.remove('don')
  all_stopwords.remove('isn\'t')
  all_stopwords.remove('nor')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

"""## Creating the Bag of Words model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,-1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 13)

"""## Training the SVM model on the Training set"""

from sklearn.svm import SVC
clf = SVC(kernel='sigmoid')
clf.fit(x_train,y_train)

"""## Predicting the Test set results"""

y_pred = clf.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix,accuracy_score
print(confusion_matrix(y_test,y_pred))

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(clf,X=x_train,y=y_train,cv=10)
print(accuracies)

print("Accuracy:{:.2f}%".format(accuracies.mean()*100))
print("Standard Deviation:{:.2f}%".format(accuracies.std()*100))

np.set_printoptions(precision=2)
print(accuracy_score(y_test,y_pred)*100)

"""## Training the Logistic model on the Training set"""

from sklearn.linear_model import LogisticRegression
clf_reg = LogisticRegression()
clf_reg.fit(x_train,y_train)

pred_reg = clf_reg.predict(x_test)
print(np.concatenate((pred_reg.reshape(len(pred_reg),1),y_test.reshape(len(y_test),1)),1))

print(confusion_matrix(y_test,pred_reg))

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(clf_reg,X=x_train,y=y_train,cv=10)
print(accuracies)

print("Accuracy:{:.2f}%".format(accuracies.mean()*100))
print("Standard Deviation:{:.2f}%".format(accuracies.std()*100))

np.set_printoptions(precision=2)
print(accuracy_score(y_test,pred_reg)*100)

"""## Predicting if a single review is positive or negative"""

new_review = 'I love this restaurant so much'
new_review = re.sub('[^a-zA-Z]', ' ', new_review)
new_review = new_review.lower()
new_review = new_review.split()
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
new_review = ' '.join(new_review)
new_corpus = [new_review]
new_X_test = cv.transform(new_corpus).toarray()
new_y_pred = clf.predict(new_X_test)
print(new_y_pred)

new_review = 'I love this restaurant so much'
new_review = re.sub('[^a-zA-Z]', ' ', new_review)
new_review = new_review.lower()
new_review = new_review.split()
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
new_review = ' '.join(new_review)
new_corpus = [new_review]
new_X_test = cv.transform(new_corpus).toarray()
new_y_pred = clf_reg.predict(new_X_test)
print(new_y_pred)

new_review = 'I hate this restaurant so much'
new_review = re.sub('[^a-zA-Z]', ' ', new_review)
new_review = new_review.lower()
new_review = new_review.split()
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
new_review = ' '.join(new_review)
new_corpus = [new_review]
new_X_test = cv.transform(new_corpus).toarray()
new_y_pred = clf.predict(new_X_test)
print(new_y_pred)

new_review = 'I hate this restaurant so much'
new_review = re.sub('[^a-zA-Z]', ' ', new_review)
new_review = new_review.lower()
new_review = new_review.split()
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
new_review = ' '.join(new_review)
new_corpus = [new_review]
new_X_test = cv.transform(new_corpus).toarray()
new_y_pred = clf_reg.predict(new_X_test)
print(new_y_pred)