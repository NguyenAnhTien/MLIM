"""
@author: Anh-Tien Nguyen
@date: 2022-05-24
"""

import utils
import configs
from mocker import Mocker
from dataset_handler import DatasetHandler

if __name__ == '__main__':
    # mocker = Mocker()
    # df = utils.read_csv(configs.PARKS)
    # mock_df = mocker.mock(df, target_column='status')
    # utils.dump_csv(mock_df, configs.MOCK_PARKS)
    dataset_handler = DatasetHandler(configs.PARKS, configs.PARKS_TARGET)
    data, labels = dataset_handler.parse()
