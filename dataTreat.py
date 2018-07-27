from dataMissing import dataMissing
from dataFeatSimp import dataFeatSimp
from dataFeatComb import dataFeatComb
from dataFeatPoly import dataFeatPoly
from dataCateg import dataCateg

import pandas as pd
import numpy as np
from scipy.stats import skew

def dataTreat(train, dataName, deleteSalePrice):
    train = dataMissing(train)
    train = dataCateg(train)
    train = dataFeatSimp(train)
    train = dataFeatComb(train)
    train = dataFeatPoly(train)

    # print('depois do tratamento')
    # print(train.shape)

    # Differentiate numerical features (minus the target) and categorical features
    categorical_features = train.select_dtypes(include = ["object"]).columns
    numerical_features = train.select_dtypes(exclude = ["object"]).columns


    # print(dataName + ' categorical_features' + str(categorical_features.shape))
    # print(dataName + ' numerical_features' + str(numerical_features.shape))


    if deleteSalePrice:
        numerical_features = numerical_features.drop("SalePrice")

    train_num = train[numerical_features]
    train_cat = train[categorical_features]


    # print(dataName + ' train_num' + str(train_num.shape))
    # print(dataName + ' train_cat' + str(train_cat.shape))
    
    train_num = train_num.fillna(train_num.median())
    
    skewness = train_num.apply(lambda x: skew(x))
    skewness = skewness[abs(skewness) > 0.5]
    # print(str(skewness.shape[0]) + " skewed numerical features to log transform")
    skewed_features = skewness.index
    train_num[skewed_features] = np.log1p(train_num[skewed_features])
    
    train_cat = pd.get_dummies(train_cat)


    # print(dataName + ' train_num' + str(train_num.shape))
    # print(dataName + ' train_cat' + str(train_cat.shape))
    
    train = pd.concat([train_num, train_cat], axis = 1)

    # print(train.columns)

    return train