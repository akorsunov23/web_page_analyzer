from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

PATH = 'web_page/source_code/'


def test_create_source_code_success():
    """Тестирование успешного запроса на добавление исходного кода сайта."""
    url_parse = 'https://github.com/akorsunov23'
    response = client.post(PATH, params={'url': url_parse})
    assert response.status_code == 201
    assert response.json()['url'] == url_parse


def test_create_source_code_url_no_valid():
    """Тестирование запроса на добавление исходного кода сайта c не валидным url."""
    url_parse = 'httpssss://github.com/akorsunov23'
    response = client.post(PATH, params={'url': url_parse})
    assert response.status_code == 422


def test_create_source_code_url_redirect():
    """Тестирование запроса на добавление исходного кода сайта c url-перенаправлением."""
    url_parse = 'https://yandex.ru/search/?text=fastapi&lr=136914&clid=1955453&win=608'
    response = client.post(PATH, params={'url': url_parse})
    assert response.status_code == 400
