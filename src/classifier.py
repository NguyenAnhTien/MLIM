"""
@author : Anh-Tien Nguyen
@date   : 2022-05-24
@desc   :
    -)
"""
import itertools

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

from dataset_handler import DatasetHandler

class Classifier(object):
    def __init__(self, dataset, target, imputer=None, id_column=None):
        self.scaler = self.define_scaler()
        self.dataset_handler = DatasetHandler(dataset, target, id_column, imputer)

    def run(self):
        lrs = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        gammas = [0.0001, 0.001, 0.01, 0.1, 0.09, 0.009, 0.0009, 0.08, 0.008, 0.0008, 0.06, 0.006, 0.0006]
        params = list(itertools.product(*[lrs, gammas]))

        X_train, X_val, y_train, y_val = self.setup()

        best_train_acc = 0
        best_val_acc = 0
        for param in list(params):
            C     = param[0]
            gamma = param[1]
            model = self.define_model(C, gamma)
            model.fit(X_train, y_train)
            train_acc = model.score(X_train, y_train)
            val_acc = model.score(X_val, y_val)
            if best_train_acc < train_acc and best_val_acc < val_acc:
                best_train_acc = train_acc
                best_val_acc = val_acc
        return best_train_acc, best_val_acc

    def setup(self):
        data, labels = self.dataset_handler.parse()
        X_train, X_test, y_train, y_test = \
                            self.dataset_handler.train_test_split(data, labels)
        self.scaler.fit(X_train)
        X_train = self.scaler.transform(X_train)
        X_test = self.scaler.transform(X_test)
        return X_train, X_test, y_train, y_test

    def define_scaler(self):
        scaler = StandardScaler()
        return scaler

    def define_model(self, C, gamma):
        model = SVC(C=C, gamma=gamma)
        return model
