from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from com.curd.model.University import University
from config import db
# engine = client = create_engine('sqlite:///university_lite_store.db',echo=True)
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()


class UniversityRepository:

    def __int__(self):
        pass

    def getAll(self) -> list:
        return db.session.query(University)

    def delete(self,index) -> None:
        instance = self.getById(index)
        db.session.delete(instance)

    def getById(self, index: int) -> University:
        return db.session.get(University, index)

    def save(self, record: University) -> None:
        db.session.add(record)
        db.session.commit()



if __name__ == '__main__':
    repo = UniversityRepository()
    # repo.getAll()
    # print(f'University :{repo.getById(1)}')
    record = University()
    record.__setattr__('name', 'Jamia University')
    record.__setattr__('country', 'India')
    record.__setattr__('Domains', 'jamiahamdard.edu')
    record.__setattr__('WebPages', 'http://jamiahamdard.edu/')
    repo.save(record)
    print(f'new record index is {record.index}')
