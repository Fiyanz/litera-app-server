from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/peminjaman_buku"
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/litera_app"


engine = create_engine(DATABASE_URL)
Sessionmaker = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = Sessionmaker()
    try:
        yield db
    finally:
        db.close()

def create_tabels():
    Base.metadata.create_all(bind=engine)