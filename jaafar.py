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


X_train_splited, X_test_splited, y_train_splited, y_test_splited = train_test_split(X_train, y_train, test_size = 0.3, random_state = 0)

# print(X_train.info)


# X_train.to_csv('./X_train.csv', sep=',', index=False)
# X_test.to_csv('./X_test.csv', sep=',', index=False)

# steps
steps = [('scaler', StandardScaler()),
         ('ridge', Ridge())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'ridge__alpha':np.logspace(-4, 0, 50)}

# Create the GridSearchCV object: cv
cv = GridSearchCV(pipeline, parameters, cv=3)

# Fit to the training set
cv.fit(X_train_splited, y_train_splited)

#predict on train set
y_pred_train=cv.predict(X_test_splited)

# Predict test set
# y_pred_test=cv.predict(X_test)

# rmse on train set
rmse = np.sqrt(mean_squared_error(y_test_splited, y_pred_train))
print("Root Mean Squared Error: {}".format(rmse))

# shape to export
# output=pd.concat([y_id, DataFrame(np.exp(y_pred_test)-1)], axis=1, ignore_index=True)
# output.columns=['Id', 'SalePrice']

# export
# output.to_csv('./submission.csv', sep=',', index=False)