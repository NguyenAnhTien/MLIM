"""
@author: Anh-Tien Nguyen
@date  : 2022-05-24
"""
import utils
import configs
from mocker import Mocker
from classifier import Classifier
from dataset_handler import DatasetHandler

def train_model(dataset, target, id_column=None):
    classifier = Classifier(dataset, target, id_column, imputer=True)
    train_acc, val_acc = classifier.run()
    print(f"TRAIN ACC: {train_acc} - VAL ACC: {val_acc}")

def mock_data(dataset, target_column, mock_file_name):
    mocker = Mocker()
    dataset = utils.read_csv(dataset)
    df_mock = mocker.mock(dataset, target_column)
    utils.dump_csv(df_mock, mock_file_name)

if __name__ == '__main__':
    utils.set_seed()
    # train_model(configs.MOCK_PARKS, configs.PARKS_TARGET, configs.PARKS_ID_COLUMN)
    ## mock_data(configs.PIDD, configs.PIDD_TARGET, configs.MOCK_PIDD)
    train_model(configs.PIDD, configs.PIDD_TARGET)
    train_model(configs.MOCK_PIDD, configs.PIDD_TARGET)
