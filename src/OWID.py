from owid.catalog import charts 
from owid import catalog 
import pandas as pd

class OWID:
    """Classe Responsável pela extração de tabelas na API de dados da OWID (Our World In Data).\n
    Verifique a documentação da API em: <https://pypi.org/project/owid-catalog/>\n
    Para instânciar um objeto do tipo OWID é necessário passar um valor de slug (a parte do endereço que vem depois do domínio).
    """

    def __init__(self, slug_value: str) -> None:
        self.slug_value = slug_value

    def slug_into_dataframe(self) -> pd.DataFrame:
        """Uma função para baixar dados presentes em gráficos (charts) da API de dados da OWID.\n
        Caso o slug não exista, é mostrado uma mensagem de erro ao usuário.

        Returns:
            pd.DataFrame: Retorna um DataFrame com os dados extraídos da API.
        """
        try:
            pdf_owid: pd.DataFrame = charts.get_data(self.slug_value)
        except catalog.ChartNotFoundError:
            print(f"Slug {self.slug_value} inexistente!")
        else:
          return pdf_owid   
               

