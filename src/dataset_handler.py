"""
@author: Anh-Tien Nguyen
@date  : 2022-05-26
@desc  :
    1) Convert Pandas Data Frame to the following vectors:
        1.1) feature vector
        1.2) label vector
"""
class DatasetHandler(object):
    def __init__(self, df, target_column):
        """
        @args:
            df: Pandas Data Frame
        """
        self.df = df
        self.target_column = target_column

    def parse(self):
        df = self.df.copy()
        labels = list(df[self.target_column])
        df.drop(self.target_column, axis=1, inplace=True)
        data = df.to_numpy()
        return data, labels
