# Deploy a Machine Learning model with Django

## About
This project applies a Machine Learning algorithm to the <a href="https://www.kaggle.com/elikplim/car-evaluation-data-set">Car Evaluation Dataset</a> from Kaggle. The model predicts the class of the vehicle, the output is one out of four categories: 'unacc', 'acc', 'vgood' and 'good'.

## Dataset
The Car Evaluation Database contains examples with the structural information removed, i.e., directly relates CAR to the six input attributes: buying, maint, doors, persons, lug_boot, safety.

Number of Instances: 1728 <br>
Number of Attributes: 6 <br>
Attribute Values:
* buying v-high, high, med, low
* maint v-high, high, med, low
* doors 2, 3, 4, 5-more
* persons 2, 4, more
* lug_boot small, med, big
* safety low, med, high

## Classifier
Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features. A tree can be seen as a piecewise constant approximation.
A <a href = "https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html">Decision Tree Classifier</a> from Scikit Learn has been applied to make the predictions giving an accuracy of 86%.

## Pickle
The <a href = "https://docs.python.org/3/library/pickle.html">pickle</a> module implements binary protocols for serializing and de-serializing a Python object structure. Pickle is used to save the trained model into .pkl format.

## Django
<a href = "https://www.djangoproject.com/">Django</a> is used as the backend framework for the webapp. Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. The model previously saved in .pkl format is loaded and called in the views.py file, and the predictions for the given user inputs are made.
