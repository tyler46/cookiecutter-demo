{%- if cookiecutter.use_db == "y" -%}
import settings
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Entity({id}, {name})>'.format(id=self.id, name=self.name)


engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    convert_unicode=True)

Base.metadata.create_all(engine)
{%- endif -%}
