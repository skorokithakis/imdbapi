from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref
import sqlalchemy
try:
    from database_settings import CONNECTION_STRING
except ImportError:
    CONNECTION_STRING = "sqlite:///imdbapi.db"

Base = declarative_base()

class Show(Base):
    __tablename__ = 'shows'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.Unicode(200), index=True)
    year = sqlalchemy.Column(sqlalchemy.Integer)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        return "<Show('%s','%s')>" % (self.name, self.year)

sqlalchemy.Index('idx_show_name_year', Show.name, Show.year)

class Episode(Base):
    __tablename__ = 'episodes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    show_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('shows.id'), index=True)
    name = sqlalchemy.Column(sqlalchemy.Unicode(200), index=True)
    season = sqlalchemy.Column(sqlalchemy.Integer)
    number = sqlalchemy.Column(sqlalchemy.Integer)

    show = relation(Show, backref='episodes', order_by=id)

    def __init__(self, show, name, season, number):
        self.show = show
        self.name = name
        self.season = season
        self.number = number

    def __repr__(self):
        return "<Episode('%s.%s','%s')>" % (self.season, self.number, self.name)

class Stats(Base):
    __tablename__ = 'stats'
    key = sqlalchemy.Column(sqlalchemy.Unicode(200), index=True, primary_key=True)
    value = sqlalchemy.Column(sqlalchemy.Integer)

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "<Stats('%s','%s')>" % (self.key, self.value)


def init_db(transactional=False):
    engine = sqlalchemy.create_engine(CONNECTION_STRING)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    init_db()
