import requests
import json

class Currency:
    """Classe responsável por criar um valor monetário com um tipo de moeda existente.\n
    Para instanciar um objeto do tipo Currency é necessário passar como parâmetro um valor (value) e o tipo da moeda (type).\n
    Por padrão o tipo da moeda é 'USD' (Dólar americano).
    """

    def __init__(self, value: float, type: str = 'USD') -> None:
        self.value = value
        self.type = type
    
    def converter(self, new_type: str = 'BRL') -> float:
        """Converte um valor monetário com um determinado tipo de moeda para outro tipo de moeda passado como parâmetro (new_type).\n
        Por padrão o novo tipo de moeda é 'BRL' (Real brasileiro).\n
        Busca a cotação atual da moeda através da API <https://economia.awesomeapi.com.br/json/last/> e faz o câmbio de valores.

        Args:
            new_type (str, optional): Novo tipo de moeda no formato string. Defaults to 'BRL'.

        Returns:
            float: Retorna o valor convertido para a nova moeda
        """
        try: 
            url: str = 'https://economia.awesomeapi.com.br/json/last/'+ self.type +'-'+ new_type.upper()
            cotacao: bytes = requests.get(url).content
            dic: dict = json.loads(cotacao)
            cotacao_atual: float = float(dic[self.type + new_type]["bid"])
            return round(cotacao_atual * self.value, 2)
        except KeyError:
            print("Tipo de moeda inválido")
    


