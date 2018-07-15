import time
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from pandas import DataFrame


def gridSearchAuto(estimators, parameters, names, x_train, y_train, x_test, y_test, x_submission, y_id):
    n_folds = 3
    for index in range(len(estimators)):
        x_train_copy = x_train
        y_train_copy = y_train
        x_test_copy = x_test
        y_test_copy = y_test
        print("------- starting to GridSearchCV " + names[index] + " -------")
        start_time = time.time()
        clf = GridSearchCV(estimators[index], parameters[index], cv=n_folds, refit=True)
        clf.fit(x_train_copy, y_train_copy)
        scores = clf.cv_results_['mean_test_score']
        print(scores)

        y_pred_train = clf.predict(x_test_copy)
        print(names[index] + " alpha: ")
        print(clf.best_params_)

        rmse = np.sqrt(mean_squared_error(y_test_copy, y_pred_train))
        print("Root Mean Squared Error: {}".format(rmse) + " " + names[index])
        print("grid " + names[index] + "--- %s seconds --------------" % (time.time() - start_time))

        # print(clf.get_params())


        y_pred_test=clf.predict(x_submission)

        # shape to export
        output=pd.concat([y_id, DataFrame(np.exp(y_pred_test)-1)], axis=1, ignore_index=True)
        output.columns=['Id', 'SalePrice']

        # export
        output.to_csv('./submission' + names[index] + '.csv', sep=',', index=False)