import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from sklearn.utils.validation import check_is_fitted

from chemotools.utils.check_inputs import check_input


class MinMaxScaler(OneToOneFeatureMixin, BaseEstimator, TransformerMixin):
    def __init__(self, norm: str = 'max'):
        self.norm = norm


    def fit(self, X: np.ndarray, y=None) -> "MinMaxScaler":
        # Check that X is a 2D array and has only finite values
        X = check_input(X)

        # Set the number of features
        self.n_features_in_ = X.shape[1]

        # Set the fitted attribute to True
        self._is_fitted = True

        return self

    def transform(self, X: np.ndarray, y=None) -> np.ndarray:
        # Check that the estimator is fitted
        check_is_fitted(self, "_is_fitted")

        # Check that X is a 2D array and has only finite values
        X = check_input(X)
        X_ = X.copy()

        # Check that the number of features is the same as the fitted data
        if X_.shape[1] != self.n_features_in_:
            raise ValueError(f"Expected {self.n_features_in_} features but got {X_.shape[1]}")

        # Normalize the data by the maximum value
        for i, x in enumerate(X_):
            if self.norm == 'max':
                X_[i] = x / np.max(x)
            
            if self.norm == 'min':
                X_[i] = x / np.min(x)

        return X_.reshape(-1, 1) if X_.ndim == 1 else X_