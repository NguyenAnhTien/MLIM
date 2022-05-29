"""
@author: Anh-Tien Nguyen
@date  : 2022-05-26
@desc  :
    1) Convert Pandas Data Frame to the following vectors:
        1.1) feature vector
        1.2) label vector
"""
from sklearn.model_selection import train_test_split

import utils

class DatasetHandler(object):
    def __init__(self, dataset, target_column, id_column=None, imputer=None):
        """
        @args:
            df: Pandas Data Frame
        """
        self.df            = utils.read_csv(dataset)
        self.target_column = target_column
        self.id_column     = id_column
        self.imputer       = imputer

    def parse(self):
        df = self.df.copy()
        if self.id_column != None:
            df.drop(self.id_column, axis=1, inplace=True)
        labels = list(df[self.target_column])
        df.drop(self.target_column, axis=1, inplace=True)
        if self.imputer != None:
            imputer = Imputer()
            df = imputer.run(df)
        data = df.to_numpy()
        return data, labels

    def train_test_split(self, data, labels):
        X_train, X_test, y_train, y_test = train_test_split(data, labels,\
                                            test_size=0.33, random_state=2022)
        return X_train, X_test, y_train, y_test
