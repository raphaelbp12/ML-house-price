import numpy as np

def dataFeatPoly(train):
    train["OverallQual-s2"] = train["OverallQual"] ** 2
    train["OverallQual-s3"] = train["OverallQual"] ** 3
    train["OverallQual-Sq"] = np.sqrt(train["OverallQual"])
    train["AllSF-2"] = train["AllSF"] ** 2
    train["AllSF-3"] = train["AllSF"] ** 3
    train["AllSF-Sq"] = np.sqrt(train["AllSF"])
    train["AllFlrsSF-2"] = train["AllFlrsSF"] ** 2
    train["AllFlrsSF-3"] = train["AllFlrsSF"] ** 3
    train["AllFlrsSF-Sq"] = np.sqrt(train["AllFlrsSF"])
    train["GrLivArea-2"] = train["GrLivArea"] ** 2
    train["GrLivArea-3"] = train["GrLivArea"] ** 3
    train["GrLivArea-Sq"] = np.sqrt(train["GrLivArea"])
    train["SimplOverallQual-s2"] = train["SimplOverallQual"] ** 2
    train["SimplOverallQual-s3"] = train["SimplOverallQual"] ** 3
    train["SimplOverallQual-Sq"] = np.sqrt(train["SimplOverallQual"])
    train["ExterQual-2"] = train["ExterQual"] ** 2
    train["ExterQual-3"] = train["ExterQual"] ** 3
    train["ExterQual-Sq"] = np.sqrt(train["ExterQual"])
    train["GarageCars-2"] = train["GarageCars"] ** 2
    train["GarageCars-3"] = train["GarageCars"] ** 3
    train["GarageCars-Sq"] = np.sqrt(train["GarageCars"])
    train["TotalBath-2"] = train["TotalBath"] ** 2
    train["TotalBath-3"] = train["TotalBath"] ** 3
    train["TotalBath-Sq"] = np.sqrt(train["TotalBath"])
    train["KitchenQual-2"] = train["KitchenQual"] ** 2
    train["KitchenQual-3"] = train["KitchenQual"] ** 3
    train["KitchenQual-Sq"] = np.sqrt(train["KitchenQual"])
    train["GarageScore-2"] = train["GarageScore"] ** 2
    train["GarageScore-3"] = train["GarageScore"] ** 3
    train["GarageScore-Sq"] = np.sqrt(train["GarageScore"])

    return train