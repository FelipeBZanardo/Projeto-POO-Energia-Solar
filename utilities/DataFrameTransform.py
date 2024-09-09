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
    def merge_tables(data_frame1: pd.DataFrame, data_frame2: pd.DataFrame, how: str, on: str) -> pd.DataFrame:
        """Recebe 2 DataFrames e realiza o merge com base em uma coluna comum.

        Args:
            data_frame1 (pd.DataFrame): O primeiro DataFrame.
            data_frame2 (pd.DataFrame): O segundo DataFrame.
            how (str): Tipo de merge ('inner', 'left', 'right', 'outer').
            on (str): Nome da coluna em comum para fazer o merge.

        Returns:
            pd.DataFrame: Retorna o DataFrame resultante do merge.
        """

        data_frame1 = data_frame1.reset_index() 
        data_frame2 = data_frame2.reset_index()

        # Certificando que a coluna 'on' tem o tipo desejado em ambos os DataFrames
        dtype = pd.concat([data_frame1[on], data_frame2[on]]).dtype
        data_frame1[on] = data_frame1[on].astype(dtype)
        data_frame2[on] = data_frame2[on].astype(dtype)

        df1_keys = data_frame1[on]
        df2_keys = data_frame2[on]

        if how == 'inner':
            merge_keys = df1_keys[df1_keys.isin(df2_keys)]
        elif how == 'left':
            merge_keys = df1_keys
        elif how == 'right':
            merge_keys = df2_keys
        elif how == 'outer':
            merge_keys = pd.concat([df1_keys, df2_keys]).drop_duplicates()
        else:
            raise ValueError(f"Tipo de merge '{how}' não suportado")

        # Realizando o merge com base nas keys obtidas
        result_data = []
        for key in merge_keys:
            row1 = data_frame1[data_frame1[on] == key].drop('index', axis=1, errors='ignore').iloc[0] if key in df1_keys.values else pd.Series(dtype='object')
            row2 = data_frame2[data_frame2[on] == key].drop('index', axis=1, errors='ignore').iloc[0] if key in df2_keys.values else pd.Series(dtype='object')

            merged_row = pd.concat([row1, row2.drop(on, errors='ignore')], axis=0)
            merged_row[on] = key
            result_data.append(merged_row)

        # Convertendo a lista de dados mesclados de volta em um DataFrame, garantindo que a key especificada em on esteja na primeira posição
        result_df = pd.DataFrame(result_data).reset_index(drop=True)
        cols = [on] + [col for col in result_df.columns if col != on]
        result_df = result_df[cols]

        # Forçando o tipo da coluna 'on' para o tipo original
        result_df[on] = result_df[on].astype(dtype)
        
        return result_df