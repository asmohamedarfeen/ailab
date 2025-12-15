import numpy as np
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination


# Define the structure of the Bayesian Network
df=pd.read_csv('heart.csv')
model = DiscreteBayesianNetwork([('age','heartdisease'),('cp','heartdisease'),('exang','heartdisease'),('heartdisease','restecg'),('heartdisease','chol')])
model.fit(df,estimator=MaximumLikelihoodEstimator)
inference = VariableElimination(model)
q1=inference.query(variables=['heartdisease'],evidence={'restecg':1})
print(q1)
q1=inference.query(variables=['heartdisease'],evidence={'exang':1})
print(q1)

