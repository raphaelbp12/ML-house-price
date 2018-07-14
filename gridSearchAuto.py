import time
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np


def gridSearchAuto(estimators, parameters, names, x_train, y_train, x_test, y_test):
    n_folds = 3
    for index in range(len(estimators)):
        print("------- starting to GridSearchCV " + names[index] + " -------")
        start_time = time.time()
        clf = GridSearchCV(estimators[index], parameters[index], cv=n_folds, refit=True)
        clf.fit(x_train, y_train)
        scores = clf.cv_results_['mean_test_score']
        print(scores)

        y_pred_train = clf.predict(x_test)
        # print("*********************" * 3)
        # print(y_test_splited)
        # print("*********************" * 3)
        # print(y_pred_train)
        print(names[index] + " alpha: ")
        print(clf.best_params_)

        rmse = np.sqrt(mean_squared_error(y_test, y_pred_train))
        print("Root Mean Squared Error: {}".format(rmse) + " " + names[index])
        print("grid " + names[index] + "--- %s seconds -----------------------------" % (time.time() - start_time))