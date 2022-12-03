import pandas as pd 
from pathlib import Path

class CSVDataHandler:

    def __init__(self):
        file_path = Path('output.csv')
        self.df = pd.read_csv(file_path, encoding='utf8')

    def add_https_to_string(self, data):
        if data[:5] != "https":
            data = "https:" + data
        return data
    
    def add_https_series(self, df):
        df['img'] = df.apply(lambda x: self.add_https_to_string(x['img']), axis=1)
        return df

    def get_preprocessed_data(self):
        self.df = self.add_https_series(self.df)
        self.df = self.df.sort_values("collection").reset_index(drop=True)
        return self.df
    


    