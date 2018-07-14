# ML-house-price

This is a solution to a Kaggle Competition, called **House Price**.

## Source
This repository was based on many Kernels present on Kaggle.
#### Stacked Regressions : Top 4% on LeaderBoard - by Serigne
https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard
#### Simple Ridge Regression in Python - by Jaafar SAADANI
https://www.kaggle.com/jsaadani/simple-ridge-regression-in-python
#### A study on Regression applied to the Ames dataset - by juliencs
https://www.kaggle.com/juliencs/a-study-on-regression-applied-to-the-ames-dataset

## Running
You can run `python julien.py` for run my first try. Or you can run `python jaafar.py` for my second.

## Data Processing
All you need to do is run the function `julienTreat`.

### julienTreat arguments:
#### train - Type: Data Frame
This is the dataset to be processed
#### dataName - Type: String
This is string is used to show which dataset you are using on console
#### deleteSalePrice - Type: boolean
It determines if the column `SalePrice` will be deleted. This is because the test dataset hasn't this column.
