from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import environ
from dataclasses import dataclass

@dataclass
class DBEngine:
    load_dotenv(dotenv_path='.env')
    host_name: str = environ.get("hostIP")
    port: str = environ.get("port")
    username: str = environ.get("username")
    password: str = environ.get("password")
    database: str = environ.get("database")
    dialect: str = "mssql+pyodbc"

    def start_engine(self):
        db_url = (f'{self.dialect}://{self.host_name}:{self.port}/'
                  f'{self.database}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes')
        from sqlalchemy import create_engine, inspect
        engine = create_engine(db_url)
        # insp = inspect(engine)
        # print("tables:", insp.get_table_names())
        return engine


Session = sessionmaker(DBEngine().start_engine())
