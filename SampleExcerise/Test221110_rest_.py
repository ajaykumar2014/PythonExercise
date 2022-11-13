import pandas as pd
import requests
from sqlalchemy import create_engine


def extrac() -> dict:
    API_URL = 'http://universities.hipolabs.com/search?country=turkey'
    return requests.get(API_URL).json()


def transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    print(f'Total Number of University in turkey {len(data)}')
    df['Domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['WebPages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df.reset_index(drop=True)
    return df[['name', 'country', 'Domains', 'WebPages']]


def createSqliteEngine():
    return create_engine('sqlite:///my_lite_store.db')


def db_persist(df: pd.DataFrame) -> None:
    engine = createSqliteEngine()
    df.to_sql('cal_uni', engine, if_exists='replace')


def readFromDB() -> pd.DataFrame:
    engine = createSqliteEngine()
    df = pd.read_sql('select * from cal_uni', con=engine)
    print(f'Total record is {len(df)}')
    return df


data = extrac()
df = transform(data)
db_persist(df)
print(readFromDB())
