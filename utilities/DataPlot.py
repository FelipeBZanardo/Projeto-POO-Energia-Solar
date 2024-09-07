import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
class DataPlot:
    
    @staticmethod
    def plot_line(data_frame: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str):
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=x_col, y=y_col, data=data_frame)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_area(data_frame: pd.DataFrame, x:str, title: str, xlabel: str, ylabel: str):
        data_frame.plot(grid=True, kind='area',xlabel=xlabel, ylabel=ylabel, title=title, x='Ano')
       