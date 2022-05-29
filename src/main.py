"""
@author: Anh-Tien Nguyen
@date  : 2022-05-24
"""

import utils
import configs
from mocker import Mocker
from classifier import Classifier
from dataset_handler import DatasetHandler

def train_model(dataset, target):
    classifier = Classifier(dataset, target)
    train_acc, val_acc = classifier.run()
    print(f"TRAIN ACC: {train_acc} - VAL ACC: {val_acc}")

if __name__ == '__main__':
    train_model(configs.PARKS, configs.PARKS_TARGET)
