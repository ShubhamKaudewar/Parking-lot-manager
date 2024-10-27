from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv
from os import environ

class DBEngine:
    def __init__(self):
        self.host_name = environ.get('hostIP')
        self.port = environ.get('port')
        self.username = environ.get('username')
        self.password = environ.get('password')
        self.database = environ.get("database")
        self.dialect = 'mssql+pyodbc'

    def start_engine(self):
        db_url = (f'{self.dialect}://{self.host_name}:{self.port}/'
                  f'{self.database}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes')
        from sqlalchemy import create_engine, inspect
        engine = create_engine(db_url)
        # insp = inspect(engine)
        # print("tables:", insp.get_table_names())
        return engine


Session = sessionmaker(DBEngine().start_engine())
