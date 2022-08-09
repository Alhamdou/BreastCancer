
# Author: Alhamdou
# title: Breast Cancer Detection with Machine Learning


"""
    this project is purposely for the breast cancer detection with machine learning using python.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from data_cleaning import DataCleaning

class DataInjestion:
    """
        Data injestion class is about taken the data from the given source
    """
    def __init__(self) -> None:
        pass
    
    def read_data(self) -> pd.DataFrame:
        data = pd.read_csv("../data/data.csv")
        
        
    def get_data(self) -> pd.DataFrame:
        """
            this function is taking the data from the given source
        """
        df = pd.read_csv("../data/data.csv")
        return df
    
    def get_data_for_test():
        """
            this function is taking the data from the given source and will be split for testing purposely
        """
        df = pd.read_csv("./data/data.csv")
        df = df.sample(n=100)
        data_clean = DataCleaning.preprocessing_data()
        df.drop(["Diagnosis"], axis=1, inplace=True)
        results = df.to_json(orient="split")
        return results