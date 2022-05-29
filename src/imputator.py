"""
@author : Anh-Tien Nguyen
@date   : 2022-05-29
@desc   :
    1)
"""
from sklearn.impute import SimpleImputer

class Imputer(object):
    def __init__(self):
        self.imputer = SimpleImputer(strategy='mean')

    def run(self, X_train, X_test):
        self.imputer.fit(X_train)
        X_train = self.imputer.transform(X_train)
        X_test = self.imputer.transform(X_test)
        return X_train, X_test
