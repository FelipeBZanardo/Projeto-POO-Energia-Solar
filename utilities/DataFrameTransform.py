import pandas as pd

class DataFrameTransform:
    """Classe Responsável pela transformação dos dados presentes no DataFrame.\n
    Utiliza métodos estáticos para facilitar o uso como uma classe utilitária
    """
    
    @staticmethod
    def transform_column(data_frame: pd.DataFrame, old_column: str, new_column: str) -> pd.DataFrame:
        """Recebe um DataFrame (data_frame), o título da coluna a ser alterado (old_column) e o novo título (new_column).\n
        É feita a transformação para o novo valor.

        Args:
            data_frame (pd.DataFrame): DataFrame que deseja fazer a tranformação
            old_column (str): Título da coluna em string a ser alterado
            new_column (str): Novo título que estará presente no DataFrame

        Returns:
            pd.DataFrame: Rertona um novo DataFrame com o valor da coluna alterado
        """
        return data_frame.rename(columns={old_column: new_column})
    
    @staticmethod
    def verify_null():
        pass
    
    @staticmethod
    def merge_tables():
        pass
    


