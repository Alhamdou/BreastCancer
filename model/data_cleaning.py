import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
# from data_injestion import DataInjestion


class DataCleaning:
    """
        this function is helping me in cleaning my data for better prediction and preprocssing of the model
        
    """
    def __init__(self, data) -> None:
        self.data = data
    
    
    def preprocessing_data(self)-> pd.DataFrame:
        
        """
           preprocssing of the data
            
        """
        pd.read_csv("./data/data.csv")
        
        
DataCleaning(data=pd.read_csv("../data.data.csv"))
        
        

