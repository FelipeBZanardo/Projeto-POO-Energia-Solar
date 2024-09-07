import pandas as pd
from utilities import Type

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
    def verify_null(data_frame: pd.DataFrame) -> pd.Series:
        """Método que verifica se as colunas contém valores nulos no DataFrame.

        Args:
            data_frame (pd.DataFrame): DataFrame para verificação de nulos.

        Returns:
            pd.Series: Retorna as colunas que possuem valores nulos.
        """
        null_report: pd.Series = data_frame.isnull().sum()
        return null_report[null_report > 0]
    
    @staticmethod
    def transform_type_column(data_frame: pd.DataFrame, column:str, type_column: Type) -> pd.DataFrame:
        """Método responsável por mudar o tipo de dado da coluna.\n
        Informa ao usuário se o tipo de dado já é condizente o novo tipo passado no argumento (type_column).\n
        Trata exceção caso seja passado uma coluna inexistente no Dataframe ou Enum.Type que também não exista.

        Args:
            data_frame (pd.DataFrame): DataFrame para fazer a troca de tipo de dado
            column (str): Nome da coluna existente dentro do DataFrame
            type_column (Type): Tipo de dado a ser alterado conforme o Enum Type.

        Returns:
            pd.DataFrame: Retorna o DataFrame com as mudanças solicitadas.
        """
        try:
            if data_frame[column].dtype == type_column.value:
                print(f'Coluna {column} já se encontra com o tipo correto')
                return data_frame
            data_frame[column] = data_frame[column].astype(eval(type_column.name.lower()))
            print(f"Coluna {column} modificada para o tipo {type_column.name.lower()}")
            return data_frame
        except KeyError:
            print(f"A coluna '{column}' não existe no DataFrame {data_frame}")
        except (AttributeError, TypeError):
            print(f"Tipo de Dado no atributo 'type_column' inválido!")
    
    @staticmethod
    def merge_tables():
        pass
        # TODO
        # Parte do Álex
        # Não esquecer do Type hint e da docstring
        # apagar o 'pass' e todos esses comentários
    


