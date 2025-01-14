import pytest
from flask import Flask
from flask_sock import Sock
from main import app, cclass

@pytest.fixture
def client():
    """Создаёт клиент тестового приложения Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Тестирует загрузку главной страницы."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Currency Observer Page' in response.data