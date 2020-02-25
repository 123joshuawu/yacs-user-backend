from pytest_postgresql import factories
import pytest

from psycopg2.extensions import connection

from typing import Generic, TypeVar

from database import database as Database
from Model.Model import Model
from Model.Session import Session
from Model.User import User

from config import DB_HOST, DB_NAME

#Creates pytest fixture that injects connection to postgresql database
factories.postgresql_proc('test_postgresql', DB_NAME)

class TestDatabase(Database):
    def connect(self, postgresql: connection) -> None:
        self.conn = postgresql

T = TypeVar('T') 

def test_model_factory(model: T) -> T:
    class TestModel(model):
        def __init__(self, db: Database) -> T:
            self.pg = db
    return TestModel

def test_model_db_factory(model: T, postgresql: connection) -> T:
    test_db: Database = TestDatabase()
    test_db.connect(postgresql)
    test_db.conn.cursor().execute(open(f"tests/init_sql/{model.__name__.lower()}.sql", "r").read())

    return test_model_factory(model)(test_db)

#Creates pytest fixture for test session object and initializes session table
@pytest.fixture
def test_session_model(postgresql: connection) -> Session:
    return test_model_db_factory(Session, postgresql)

@pytest.fixture
def test_user_model(postgresql: connection) -> User:
    return test_model_db_factory(User, postgresql)


# db: Database = Database()
# db.connect()
# db.execute(open("init.sql", "r").read(), None, False)
# db.close()