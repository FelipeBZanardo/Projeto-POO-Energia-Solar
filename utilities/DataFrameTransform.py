import pandas as pd


class DataFrameTransform:
    
    @staticmethod
    def transform_column(data_frame: pd.DataFrame, old_column, new_column) -> pd.DataFrame:
        return data_frame.rename(columns={old_column: new_column})
    
    @staticmethod
    def verify_null():
        pass
    
    @staticmethod
    def merge_tables():
        pass
    


