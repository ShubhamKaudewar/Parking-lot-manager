from sqlalchemy.orm import sessionmaker
from os import environ


class DBEngine:
    def __init__(self):
        self.host_name = environ['hostIP']
        self.port = environ['port']
        self.username = environ['username']
        self.password = environ['password']
        self.database = environ["database"]
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
