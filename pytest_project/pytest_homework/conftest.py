import pytest
import pymssql

test_server = 'localhost:1433'
test_user = 'test_user'
password = 'HelloWorld22'
test_db = 'NEW_DB'


@pytest.fixture()
def connect_to_database():
    db_session = pymssql.connect(server=test_server, user=test_user, password=password, database=test_db)
    connection = db_session.cursor()
    return connection
