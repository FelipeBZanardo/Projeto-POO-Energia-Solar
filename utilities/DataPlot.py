import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
class DataPlot:
    """Classe responsável por plotar gráficos através de um dataFrame
    """
    
    @staticmethod
    def plot_line(data_frame: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
        """Plota um gráfico de linha

        Args:
            data_frame (pd.DataFrame): Base de dados em formato de dataFrame
            x_col (str): Nome da Coluna do dataFrame que corresponderá ao eixo das abscissas
            y_col (str): Nome da Coluna do dataFrame que corresponderá ao eixo das ordenadas
            title (str): Título do gráfico
            xlabel (str): Descrição do eixo das abscissas
            ylabel (str): Descrição do eixo das ordenadas
        """
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=x_col, y=y_col, data=data_frame)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_area(data_frame: pd.DataFrame, x:str, title: str, xlabel: str, ylabel: str) -> None:
        """Plota um gráfico de área

        Args:
            data_frame (pd.DataFrame): Base de dados em formato de dataFrame
            x (str): Nome da Coluna do dataFrame que corresponderá ao eixo das abscissas
            title (str): Título do gráfico
            xlabel (str): Descrição do eixo das abscissas
            ylabel (str): Descrição do eixo das ordenadas
        """
        data_frame.plot(grid=True, kind='area',xlabel=xlabel, ylabel=ylabel, title=title, x=x)
       