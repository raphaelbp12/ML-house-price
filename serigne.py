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

#Validation function
# n_folds = 5

# def rmsle_cv(model):
#     kf = KFold(n_folds, shuffle=True, random_state=42).get_n_splits(X_train.values)
#     rmse= np.sqrt(-cross_val_score(model, X_train.values, y_train, scoring="neg_mean_squared_error", cv = kf))
#     return(rmse)

# lasso = make_pipeline(RobustScaler(), Lasso(alpha = 0.0005, random_state=1))

# score = rmsle_cv(lasso)
# print("\nLasso score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

X_train_splited, X_test_splited, y_train_splited, y_test_splited = train_test_split(X_train, y_train, test_size = 0.3, random_state = 0)

lasso = Lasso(random_state=0, max_iter=50000)
alphas = np.logspace(-4, -0.5, 30)

tuned_parameters = [{'alpha': [0.0005298316906283707]}]
n_folds = 3

clf = GridSearchCV(lasso, tuned_parameters, cv=n_folds, refit=True)
clf.fit(X_train_splited, y_train_splited)
scores = clf.cv_results_['mean_test_score']
print(scores)

y_pred_train = clf.predict(X_test_splited)
print("*********************" * 3)
# print(y_test_splited)
print("*********************" * 3)
# print(y_pred_train)

rmse = np.sqrt(mean_squared_error(y_test_splited, y_pred_train))
print("Root Mean Squared Error: {}".format(rmse))

print("--- %s seconds ---" % (time.time() - start_time))

print(clf.best_params_)
# print(clf.get_params())


y_pred_test=clf.predict(X_test)

# shape to export
output=pd.concat([y_id, DataFrame(np.exp(y_pred_test)-1)], axis=1, ignore_index=True)
output.columns=['Id', 'SalePrice']

# export
output.to_csv('./submission.csv', sep=',', index=False)