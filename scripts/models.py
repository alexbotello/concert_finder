from sqlalchemy import Column, BigInteger, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

def db_connect():
    """
    Establishes database connection
    Return engine instance
    """
    return create_engine('YOUR_DATABASE_URL', echo=False)


def create_concert_table(engine):
    """"""
    Base.metadata.create_all(engine)


class Concert(Base):
    """
    Table to store concert listings
    """

    __tablename__ = 'concerts'

    c_id = Column(BigInteger, primary_key=True)
    title = Column(String)
    datetime = Column(String)
