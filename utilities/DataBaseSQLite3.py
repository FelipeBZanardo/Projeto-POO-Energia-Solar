import sqlite3 
from sqlalchemy import create_engine
import os
import pandas as pd

class DataBaseSQLite3:
    """Classe Responsável pela manipulação do Banco de Dados SQLite3
    """
    def __init__(self, db_name):
       self.db_name = db_name

    def create_database(self):
        """Método para criar uma base de dados local em SQLite3
        """
        try: 
          conn = sqlite3.connect(self.db_name) 
          print(f"Database {self.db_name} formed.") 
          cursor = conn.cursor()
          print(dir(cursor))
        except sqlite3.Error as error: 
          print(f"Database {self.db_name} not formed.")
          print(f"Failed to connect with {self.db_name} database", error)
          
    def send_dataframe_to_database(self, dataframe: pd.DataFrame, table_name: str = ''):
        """
        Método responsável por enviar um DataFrame para o banco de dados.

        Args:
            dataframe (pd.DataFrame): DataFrame a ser enviado ao banco de dados
            table_name (str, optional): Nome da tabela a ser persistida. Defaults to ''.
        """
        db = self.db_name
        db_engine = create_engine(f'sqlite:///{db}')

        # Store DataFrame in SQLite        
        dataframe.to_sql(name = table_name, con = db_engine, if_exists = 'replace', index = False)
        connection = sqlite3.connect(self.db_name)        
        print(connection.total_changes)

    def check_tables_in_database(self):
        """Método responsável por verificar as tabelas presentes no banco de dados.
        """

        query = '''
        SELECT 
            name
        FROM 
            sqlite_schema
        WHERE 
            type ='table' AND 
            name NOT LIKE 'sqlite_%';
        '''

        connection = sqlite3.connect(self.db_name)
        print('connection.total_changes:', connection.total_changes)

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        #cursor.execute(query)
        tables = cursor.execute(query).fetchall()    
        #cursor.close()
        print(f'tables in database {self.db_name}:', tables)            

    def read_table_in_database(self, table_name:str = '', n_rows: int = 20):
        """Método responsável por ler uma tabela do banco de dados.

        Args:
            table_name (str, optional): Nome da Tabela a ser lida. Defaults to ''.
            n_rows (int, optional): Quantidade de linhas a ser lida. Defaults to 20.
        """

        query = f'''
        SELECT 
            * 
        FROM 
            {table_name}
        '''

        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        table = cursor.execute(query).fetchmany(n_rows)
        cursor.close()
        display(table)

    def delete_database(self):
        """Deleta o banco de dados se o mesmo existir
        """

        if os.path.exists(self.db_name):
            os.remove(self.db_name)
            print("Successfully! The File has been removed")
        else:
            print("Can not delete the file as it doesn't exists")