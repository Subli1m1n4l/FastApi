from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

password = quote_plus('9PzOaDIqth5f')
database_url = f'postgresql://fl0user:{password}@ep-long-base-62807244.us-east-2.aws.neon.tech:5432/Detodo'


Pengine = create_engine(database_url)


PSession=sessionmaker(autocommit=False,autoflush=False,bind=Pengine)

PBase= declarative_base()