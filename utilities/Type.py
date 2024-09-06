from enum import Enum

class Type(Enum):
    """Enum com os principais tipos de Dados do Python.\n
    Enum auxiliar usado na conversão de tipos de dados das colunas do DataFrame

    Args:
        Enum (_type_)
    """
    INT = 'int64'
    FLOAT = 'float64'
    STR = 'O'
    DATETIME = 'datetime64[ns]'