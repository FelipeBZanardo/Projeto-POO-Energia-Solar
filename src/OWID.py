from owid.catalog import charts 
from owid import catalog 
import pandas as pd

class OWID:

    def __init__(self, slug_value: str) -> None:
        self.slug_value = slug_value

    def slug_into_dataframe(self) -> pd.DataFrame:
        """
        Uma função para baixar dados presentes em gráficos (charts)
        """

        try:
            pdf_owid: pd.DataFrame = charts.get_data(self.slug_value)
        except catalog.ChartNotFoundError:
            print(f"Slug {self.slug_value} inexistente!")
        else:
          return pdf_owid   
               

