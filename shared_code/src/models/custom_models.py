import numpy as np

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.multiclass import unique_labels
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class ANDModel(BaseEstimator, ClassifierMixin):
    def __init__(self, flg_do_ohe: bool = False):
        self.flg_do_ohe = flg_do_ohe

    def fit(self,  X, y):
        X, y = check_X_y(X, y)
        self.classes_ = unique_labels(y)
        return self

    def predict(self, X):
        X = check_array(X)
        check_is_fitted(self)

        if self.flg_do_ohe:
            X = (X > 0).astype(int)

        ps = np.multiply.reduce(X, axis=1)
        return ps


