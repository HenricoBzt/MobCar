from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL =  "mysql+pymysql://root:henricopereira12@localhost:3306/mobcar"

engine = create_engine(DATABASE_URL,echo=True)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
metadata.reflect(bind=engine)
Base = declarative_base()

print(engine)
session.commit()

