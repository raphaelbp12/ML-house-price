import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings

warnings.filterwarnings('ignore')
#%matplotlib inline

train = pd.read_csv('./input/train.csv')
test = pd.read_csv('./input/test.csv')
a = train['SalePrice'].describe()
print(a)

# sns.boxplot(train.YearBuilt, train.SalePrice)

# sns.distplot(train['SalePrice']);

train.drop(train[(train["GrLivArea"]>4000)&(train["SalePrice"]<300000)].index,inplace=True)
train.drop(train[(train["TotalBsmtSF"]>3000)].index,inplace=True)

train.drop(['Id'],axis=1, inplace=True)
print(train.shape)

def plotGraph(varName):
    data = pd.concat([train['SalePrice'], train[varName]], axis=1)
    data.plot.scatter(x=varName, y='SalePrice', ylim=(0,800000));

plotGraph('GrLivArea')

sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(train[cols], size = 2.5)

plt.show()