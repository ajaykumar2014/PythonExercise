import pandas as pd
import requests
from sqlalchemy import create_engine


def readAllHipolabsUniversityByCountry() -> dict:
    API_URL = 'http://universities.hipolabs.com/search?name=middle'
    multiDict = {}
    """
    Fetch all country and remove duplicate 
    """
    for country in set([''.join(r['country']) for r in requests.get(API_URL).json()]) :
        dict = extractUniversityByUniversity(country)
        print(f'Read record by {country} and total records are : {len(dict)}')
        multiDict.update({country: dict})
    return multiDict


def extractUniversityByUniversity(country: str) -> dict:
    API_URL = f'http://universities.hipolabs.com/search?country={country}'
    return requests.get(API_URL).json()


def transform(data: list) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df['Domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['WebPages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df.reset_index(drop=True)
    return df[['name', 'country', 'Domains', 'WebPages']]


def createSqliteEngine():
    return create_engine('sqlite:///my_lite_store.db')


def db_persist(df: pd.DataFrame) -> None:
    engine = createSqliteEngine()
    df.to_sql('cal_uni_all', engine, if_exists='replace')
    # engine.connections.close_all()


def readFromDBToCSV():
    engine = createSqliteEngine()
    df = pd.read_sql('select * from cal_uni_all', con=engine)
    print(f'Total record is {len(df)}')
    df.to_csv('uni_all.csv',index=False)
    df.to_excel('uni_all.xlsx',sheet_name='All Hipolabs University ')

if __name__ == '__main__':


    """
    Persist the University record in DB through DataFrame
    """
    uni_dict = readAllHipolabsUniversityByCountry()
    resultant_dict = []
    for dictValue in uni_dict.values():
        [resultant_dict.append(ll) for ll in dictValue]

    df = transform(resultant_dict)
    db_persist(df)

    """
    Read record in DB and write into CSV And Excel
    """

    readFromDBToCSV()

# pd.merge_ordered(lambda l,r : pd.merge(l,r,left_index=True,right_index=True,on='country'),uni_dict.values())
# uni_dict = readAllHipolabsUniversityByCountry()
# data = extrac()
# print(f'Total number of records :{len(uni_dict[d])} of country:{d}')
# resultant_dict = [','.join(map(str,v)) for v in uni_dict.values()]
# resultant_dict = []
# for dictValue in uni_dict.values():
#     [resultant_dict.append(ll) for ll in dictValue]

# df = transform(resultant_dict)
# db_persist(df)

#readFromDBToCSV()
