# import libraries
import pandas as pd
from pandas import DataFrame
import numpy as np

# import libraries
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

import time

start_time = time.time()


# read data
df_train=pd.read_csv('./input/train.csv')
df_test=pd.read_csv('./input/test.csv')

#store Ids of homes
df_train=df_train.drop('Id', axis=1)
y_id=df_test['Id'].copy()
df_test=df_test.drop('Id', axis=1)

#define y_train
y_train=df_train['SalePrice'].values.reshape(-1,1)
df_train=df_train.drop('SalePrice', axis=1)

#transform y_train to match the evaluation metric
y_train=np.log(y_train+1)

from julienTreat import julienTreat

df_train = julienTreat(df_train, 'train', False)
df_test = julienTreat(df_test, 'test', False)

#concate df_train and df_test
df=pd.concat([df_train, df_test], axis=0, ignore_index=True, sort=False)

#select columns with non null values
df=df.dropna(axis=1)

#transform categorical variables into dummy variables
df=pd.get_dummies(df, drop_first=True)

#create X_train and X_test
X_train=df.iloc[:df_train.shape[0],]
X_test=df.iloc[df_train.shape[0]:,]

from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
# import xgboost as xgb
# import lightgbm as lgb

X_train_splited, X_test_splited, y_train_splited, y_test_splited = train_test_split(X_train, y_train, test_size = 0.3, random_state = 0)

estimators = []
parameters = []
names = []

alphas = np.logspace(-4, -0.5, 30)

ridge = Ridge(random_state=0, max_iter=50000)
ridge_tuned_parameters = [{'alpha': [0.31622776601683794]}]
estimators.append(ridge)
parameters.append(ridge_tuned_parameters)
names.append('ridge')

lasso = Lasso(random_state=0, max_iter=50000)
lasso_tuned_parameters = [{'alpha': [0.0005298316906283707]}]
estimators.append(lasso)
parameters.append(lasso_tuned_parameters)
names.append('lasso')

elastic = ElasticNet(l1_ratio=.9, random_state=3, max_iter=50000)
elastic_tuned_parameters = [{'alpha': [0.0005298316906283707]}]
estimators.append(elastic)
parameters.append(elastic_tuned_parameters)
names.append('elastic')

KRR = KernelRidge(kernel='polynomial', degree=2, coef0=2.5)
KRR_tuned_parameters = [{'alpha': [0.6]}]
estimators.append(KRR)
parameters.append(KRR_tuned_parameters)
names.append('KRR')

from gridSearchAuto import gridSearchAuto

gridSearchAuto(estimators, parameters, names, X_train_splited, y_train_splited, X_test_splited, y_test_splited)

# print(clf.get_params())


# y_pred_test=clf.predict(X_test)

# shape to export
# output=pd.concat([y_id, DataFrame(np.exp(y_pred_test)-1)], axis=1, ignore_index=True)
# output.columns=['Id', 'SalePrice']

# export
# output.to_csv('./submission.csv', sep=',', index=False)