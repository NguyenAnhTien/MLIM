"""
@author : Anh-Tien Nguyen
@date   : 2022-05-29
@desc   :
    1)
"""
from sklearn.impute import SimpleImputer

class Imputer(object):
    def __init__(self):
        self.imputer = SimpleImputer( strategy='mean')

    def run(self, df):
        df = self.imputer.fit(df)
        return df
