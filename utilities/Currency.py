import requests
import json

class Currency:

    def __init__(self, value: float, type: str = 'USD') -> None:
        self.value = value
        self.type = type
    
    def converter(self, new_type: str = 'BRL') -> float:
        try: 
            url = 'https://economia.awesomeapi.com.br/json/last/'+ self.type +'-'+ new_type.upper()
            cotacao = requests.get(url).content
            dic = json.loads(cotacao)
            cotacao_atual = float(dic[self.type + new_type]["bid"])
            return round(cotacao_atual * self.value, 2)
        except KeyError:
            print("Tipo de moeda inválido")
    


