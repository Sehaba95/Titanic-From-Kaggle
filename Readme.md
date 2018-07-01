<h1>Titanic from Kaggle</h1>
In this project I've applied a different classifiers to Titanic dataset from Kaggle.

The dataset contain 891 samples for train the model, 418 samples for test and has 13 features (5 of them are selected for the classification).

The file "train.csv" contain data (Features and Targets) for train the model. The file "test.csv" contain features for the model test. The file "gender_submission.csv" contain targets for test the model.

<h2>Features selected are:</h2>

	Pclass : A proxy for socio-economic status (1st = Upper, 2nd = Middle, 3rd = Lower)
	Age : Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
	SibSp : The dataset defines family relations in this way: 
			Sibling = brother, sister, stepbrother, stepsister
			Spouse = husband, wife (mistresses and fiancés were ignored)
	Parch : The dataset defines family relations in this way...
			Parent = mother, father
			Child = daughter, son, stepdaughter, stepson
			Some children travelled only with a nanny, therefore parch=0 for them.
	Sex

<h2>Results</h2>
<table>
	<tr> <th>Algorithm</th> <th>Model Performance</th> </tr>
	<tr> <td>Support Vector Classifier</td> <td>1.0</td> </tr>
	<tr> <td>Decision Tree Classifier</td> <td>0.992822966507177</td> </tr>
	<tr> <td>Random Forest Classifier</td> <td>0.9808612440191388</td> </tr>
	<tr> <td>Linear Discriminant Analysis</td> <td>0.9617224880382775</td> </tr>
	<tr> <td>Logistic Regression</td> <td>0.9617224880382775</td> </tr>
	<tr> <td>Logistic Regression + lbfgs Solver</td> <td>0.937799043062201</td> </tr>
	<tr> <td>Discriminant Analysis</td> <td>0.9282296650717703</td> </tr>
	<tr> <td>Gaussian Naive Bayes</td> <td>0.9138755980861244</td> </tr>
	<tr> <td>Gaussian Process Classifier</td> <td>0.9090909090909091</td> </tr>
	<tr> <td>Ada Boost Classifier</td> <td>0.8708133971291866</td> </tr>
	<tr> <td>Multi Layer Perceptron Classifier</td> <td>0.7990430622009569</td> </tr>
	<tr> <td>K-Neighbors Classifier</td> <td>0.6507177033492823</td> </tr>
</table>

<h2>Requirements</h2>
Python 2.7 and up

<h2>Installation</h2>
The followoing are the prerequiste Python modules that needs to be installed to execute main.py:

	sudo pip install pandas 
	sudo pip install -U scikit-learn

<h2>Downloads</h2>
Clone the repository using the below mentioned command and execute the Python program.
	
	git clone https://github.com/Sehaba95/Titanic-From-Kaggle.git
	cd Titanic-From-Kaggle/Classifiers
	python SupportVectorClassifier.py

<h2>Authors</h2>

[Sehaba Amine](https://github.com/Sehaba95)