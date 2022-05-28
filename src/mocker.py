"""
@author: Anh-Tien Nguyen
@date  : 2022-05-24
@desc  :
    1) It is designed to mock the missing data
    2) Randomly remove some features of data
    3) Only adjust 15% of number of rows
"""

import random

import utils

class Mocker(object):
    def __init__(self):
        pass

    def mock(self, df, target_column):
        """
        @desc:
            1) the data is stored in data frame and identify by row and column
            2) randomly generate a column and row to be removed
        """
        df_mock = df.copy()
        target_index = utils.convert_col_name_to_idx(df_mock, target_column)
        num_rows = utils.get_df_num_rows(df_mock)
        num_columns = utils.get_df_num_columns(df_mock)

        num_iters = int(num_rows * 0.15)

        for _ in range(num_iters):
            row_index = random.randint(0, num_rows - 1)
            column_index = random.randint(0, num_columns - 1)

            if column_index == target_index:
                column_index -= 1

            df_mock.iloc[row_index, column_index] = None

        return df_mock
