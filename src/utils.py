"""
@author: Anh-Tien Nguyen
@date  : 2022-05-24
"""
import random
import numpy

import pandas

def read_csv(file_name, drop_nan=False):
    df = pandas.read_csv(file_name, na_filter=drop_nan)
    if drop_nan:
        df.dropna(inplace=True)
    return df

def dump_csv(df, file_name):
    df.to_csv(file_name, index=False)

def get_shape(df):
    return df.shape

def get_df_num_rows(df):
    return df.shape[0]

def get_df_num_columns(df):
    return df.shape[1]

def convert_col_name_to_idx(df, column_name):
    return df.columns.get_loc(column_name)

def set_seed():
    random.seed(2022)
    numpy.random.seed(2022)
