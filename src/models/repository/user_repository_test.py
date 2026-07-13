import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from .user_repository import UsersRepository

@pytest.mark.skip(reason="insert in DB")
def test_users_repository():
    db_conn = DbConnectionHandler()
    users_repo = UsersRepository(db_conn)
    
    person_name="Bug"
    age=65
    height=7.34
    
    # user_repo.insert_user(person_name="Test", age=55, height=7.34) # Inserindo o usuário
    users = users_repo.select_user(person_name) # Buscando o usuário
    
    # Verificando se realmente inseriu o usuário e se a busca esta certa
    assert isinstance(users, list)
    assert len(users) == 1
    assert users[0].person_name == person_name
    assert users[0].age == age
    assert users[0].height == height