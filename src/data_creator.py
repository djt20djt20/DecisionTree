from sklearn.datasets import load_breast_cancer
import pandas as pd

class DataCreator:
    '''
    The purpose of this class is to get data for our decision tree to train and test on
    '''
    def __init__(self):
        self.data = None
        self.df = None

    def fetch_breast_cancer_data(self):
        self.data = load_breast_cancer()
        return self

    def return_data_frame(self):
        df = pd.DataFrame(self.data.data, columns=self.data.feature_names)
        df.loc[:,'Target'] = self.data.target
        self.df = df
        return self.df
