#!/usr/bin/env python 

import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

#Load train data 
train = pd.read_csv("train.csv")

#Selected features for train and test 
features = ["Pclass","Sex","Age","SibSp","Parch"]

#Load test features 
test = pd.read_csv("test.csv")

#Select features and parse the result to pandas dataframe
X_test = pd.DataFrame(test.loc[:,features].values)

#Load targets for test
submission = pd.read_csv("gender_submission.csv")

#Select the target column 
Y_test = submission.loc[:,"Survived"].values

#Slpit train data into features and targets for train
X_train = pd.DataFrame(train.loc[:,features].values)
Y_train = train.loc[:,"Survived"].values

#Data encoding : since machine learning work just with number we're going to parse strings to numeric values using Label Encoder
le = preprocessing.LabelEncoder()
X_train = X_train.apply(le.fit_transform)	
X_test = X_test.apply(le.fit_transform)	

#Create a K-Neighbors Classifier instance 
classifier = KNeighborsClassifier(8)

#Fit the classifier
classifier.fit(X_train,Y_train)

#Calculate the score (Accuracy)
score = classifier.score(X_test,Y_test)

#Printing the score
print(score)