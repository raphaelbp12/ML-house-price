# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.metrics import mean_squared_error, make_scorer
from scipy.stats import skew
#from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

from dataTreat import dataTreat

# Definitions
pd.set_option('display.float_format', lambda x: '%.3f' % x)
#%matplotlib inline
#njobs = 4

train = pd.read_csv("./input/train.csv")
test=pd.read_csv('./input/test.csv')

print(train.shape)
print(test.shape)

TestId=test['Id']
test.drop('Id', axis=1, inplace = True)

# Drop Id column
train.drop("Id", axis = 1, inplace = True)
train = train[train.GrLivArea < 4000]

# Log transform the target for official scoring
train.SalePrice = np.log1p(train.SalePrice)
y = train.SalePrice

print(set(train.columns)-set(test.columns))

train = julienTreat(train, 'train', True)
test = julienTreat(test, 'test', False)

X_train, X_test, y_train, y_test = train_test_split(train, y, test_size = 0.3, random_state = 0)
test_x, test_y = train_test_split(test, )
# print("X_train : " + str(X_train.shape))
# print("X_test : " + str(X_test.shape))
# print("y_train : " + str(y_train.shape))
# print("y_test : " + str(y_test.shape))

# Define error measure for official scoring : RMSE
scorer = make_scorer(mean_squared_error, greater_is_better = False)

def rmse_cv_train(model):
    rmse= np.sqrt(-cross_val_score(model, X_train, y_train, scoring = scorer, cv = 10))
    return(rmse)

def rmse_cv_test(model):
    rmse= np.sqrt(-cross_val_score(model, X_test, y_test, scoring = scorer, cv = 10))
    return(rmse)

# # Linear Regression
# lr = LinearRegression()
# lr.fit(X_train, y_train)

# # Look at predictions on training and validation set
# print("RMSE on Training set :", rmse_cv_train(lr).mean())
# print("RMSE on Test set :", rmse_cv_test(lr).mean())
# y_train_pred = lr.predict(X_train)
# y_test_pred = lr.predict(X_test)

# 2* Ridge
ridge = RidgeCV(alphas = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1, 3, 6, 7, 9, 10, 11, 11.1, 11.5, 12, 12.1, 12.5, 13, 13.1, 15, 30, 60])
ridge.fit(X_train, y_train)
alpha = ridge.alpha_
print("Best alpha :", alpha)

print("Try again for more precision with alphas centered around " + str(alpha))
ridge = RidgeCV(alphas = [alpha * .6, alpha * .65, alpha * .7, alpha * .75, alpha * .8, alpha * .85, 
                          alpha * .9, alpha * .95, alpha, alpha * 1.05, alpha * 1.1, alpha * 1.15,
                          alpha * 1.25, alpha * 1.3, alpha * 1.35, alpha * 1.4], 
                cv = 10)
ridge.fit(X_train, y_train)
alpha = ridge.alpha_
print("Best alpha :", alpha)

# print("Ridge RMSE on Training set :", rmse_cv_train(ridge).mean())
# print("Ridge RMSE on Test set :", rmse_cv_test(ridge).mean())
# y_train_rdg = ridge.predict(X_train)
# y_test_rdg = ridge.predict(X_test)

X_test=test.iloc[test.shape[0]:,]
predicted=ridge.predict(X_test)

submission=pd.DataFrame()
submission['Id']=TestId
submission['SalePrice']=predicted
submission.to_csv('submission.csv', index=False)


##################################################################################################################################################

# 3* Lasso
# lasso = LassoCV(alphas = [0.0001, 0.0003, 0.0006, 0.001, 0.003, 0.006, 0.01, 0.03, 0.06, 0.1, 
#                           0.3, 0.6, 1], 
#                 max_iter = 50000, cv = 10)
# lasso.fit(X_train, y_train)
# alpha = lasso.alpha_
# print("Best alpha :", alpha)

# print("Try again for more precision with alphas centered around " + str(alpha))
# lasso = LassoCV(alphas = [alpha * .6, alpha * .65, alpha * .7, alpha * .75, alpha * .8, 
#                           alpha * .85, alpha * .9, alpha * .95, alpha, alpha * 1.05, 
#                           alpha * 1.1, alpha * 1.15, alpha * 1.25, alpha * 1.3, alpha * 1.35, 
#                           alpha * 1.4], 
#                 max_iter = 50000, cv = 10)
# lasso.fit(X_train, y_train)
# alpha = lasso.alpha_
# print("Best alpha :", alpha)

# print("Lasso RMSE on Training set :", rmse_cv_train(lasso).mean())
# print("Lasso RMSE on Test set :", rmse_cv_test(lasso).mean())


##################################################################################################################################################

# 4* ElasticNet
# print("ElasticNet")

# elasticNet = ElasticNetCV(l1_ratio = [0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 1],
#                           alphas = [0.0001, 0.0003, 0.0006, 0.001, 0.003, 0.006, 
#                                     0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1, 3, 6], 
#                           max_iter = 50000, cv = 10)
# elasticNet.fit(X_train, y_train)
# alpha = elasticNet.alpha_
# ratio = elasticNet.l1_ratio_
# print("Best l1_ratio :", ratio)
# print("Best alpha :", alpha )

# print("Try again for more precision with l1_ratio centered around " + str(ratio))
# elasticNet = ElasticNetCV(l1_ratio = [ratio * .85, ratio * .9, ratio * .95, ratio, ratio * 1.05, ratio * 1.1, ratio * 1.15],
#                           alphas = [0.0001, 0.0003, 0.0006, 0.001, 0.003, 0.006, 0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1, 3, 6], 
#                           max_iter = 50000, cv = 10)
# elasticNet.fit(X_train, y_train)
# if (elasticNet.l1_ratio_ > 1):
#     elasticNet.l1_ratio_ = 1    
# alpha = elasticNet.alpha_
# ratio = elasticNet.l1_ratio_
# print("Best l1_ratio :", ratio)
# print("Best alpha :", alpha )

# print("Now try again for more precision on alpha, with l1_ratio fixed at " + str(ratio) + 
#       " and alpha centered around " + str(alpha))
# elasticNet = ElasticNetCV(l1_ratio = ratio,
#                           alphas = [alpha * .6, alpha * .65, alpha * .7, alpha * .75, alpha * .8, alpha * .85, alpha * .9, 
#                                     alpha * .95, alpha, alpha * 1.05, alpha * 1.1, alpha * 1.15, alpha * 1.25, alpha * 1.3, 
#                                     alpha * 1.35, alpha * 1.4], 
#                           max_iter = 50000, cv = 10)
# elasticNet.fit(X_train, y_train)
# if (elasticNet.l1_ratio_ > 1):
#     elasticNet.l1_ratio_ = 1    
# alpha = elasticNet.alpha_
# ratio = elasticNet.l1_ratio_
# print("Best l1_ratio :", ratio)
# print("Best alpha :", alpha )

# print("ElasticNet RMSE on Training set :", rmse_cv_train(elasticNet).mean())
# print("ElasticNet RMSE on Test set :", rmse_cv_test(elasticNet).mean())



##################################################################################################################################################









# plt.show()