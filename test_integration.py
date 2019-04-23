import pytest
import json
from app import app

app.config['TESTING'] = True

def test_app_todos_success():
    result = app.test_client().get('/todos')
    data = result.data.decode()
    assert result.status_code == 200

def test_app_todos_post_success():
    result = app.test_client().post('/todos')
    assert result.status_code == 201