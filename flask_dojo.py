from peewee import *

psql_db = PostgresqlDatabase('flask_dojo', user='sador')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db


class Counter(BaseModel):
    get_request = IntegerField()
    post_request = IntegerField()
