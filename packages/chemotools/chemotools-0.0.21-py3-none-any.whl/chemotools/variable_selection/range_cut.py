import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from sklearn.utils.validation import check_is_fitted

from chemotools.utils.check_inputs import check_input


class RangeCut(OneToOneFeatureMixin, BaseEstimator, TransformerMixin):
    def __init__(
        self,
        wavenumbers: np.ndarray = None,
        start: int = 0,
        end: int = -1,
    ):
        self.wavenumbers = wavenumbers
        self.start = self._find_index(start)
        self.end = self._find_index(end)

    def fit(self, X: np.ndarray, y=None) -> "RangeCut":
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
            raise ValueError(
                f"Expected {self.n_features_in_} features but got {X_.shape[1]}"
            )

        # Range cut the spectra
        return X_[:, self.start : self.end]

    def _find_index(self, target: float) -> int:
        if self.wavenumbers is None:
            return target
        wavenumbers = np.array(self.wavenumbers)
        return np.argmin(np.abs(wavenumbers - target))
