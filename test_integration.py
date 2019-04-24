import pytest
import json
import re
from app import app

app.config['TESTING'] = True
client = app.test_client()


def test_app_POST_todo_success():
    result = client.post('/todos', data=dict(
        title='testing'
    ))
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 201
    assert 'completed' in dict_
    assert dict_['completed'] is False
    assert 'created_date' in dict_
    assert re.search(r'\d{1,2}\/\d{1,2}\/\d{4}', dict_['created_date']) is not None
    assert 'completed_date' not in dict_ 
    assert dict_['title'] == 'testing'

def test_app_POST_todo_failure():
    result = client.post('/todos', data=dict(
        due_date='11/12/2019'
    ))
    data = result.data.decode()
    assert result.status_code == 404
    assert 'title is required' in data

def test_app_GET_todolist_success():
    result = client.get('/todos')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert '1' in dict_
    assert '2' not in dict_
    assert 'completed' in dict_['1']
    assert dict_['1']['completed'] is False
    assert 'created_date' in dict_['1']
    assert re.search(r'\d{1,2}\/\d{1,2}\/\d{4}', dict_['1']['created_date']) is not None
    assert 'completed_date' not in dict_['1']   
    assert dict_['1']['title'] == 'testing'

def test_app_GET_todo_success():
    result = client.get('/todos/1')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 200
    assert 'completed' in dict_
    assert dict_['completed'] is False
    assert 'created_date' in dict_
    assert re.search(r'\d{1,2}\/\d{1,2}\/\d{4}', dict_['created_date']) is not None
    assert 'completed_date' not in dict_   
    assert dict_['title'] == 'testing'

def test_app_PUT_todo_success():
    result = client.put('/todos/1', data=dict(
        completed=True
    ))
    data = result.data.decode()
    dict_ = json.loads(data)
    assert result.status_code == 201
    result = client.get('/todos')
    data = result.data.decode()
    dict_ = json.loads(data)
    assert 'title' in dict_['1']
    assert 'completed' in dict_['1']
    assert 'created_date' in dict_['1']
    assert dict_['1']['title'] == 'testing'
    assert dict_['1']['completed'] == True
    assert re.search(r'\d{1,2}\/\d{1,2}\/\d{4}', dict_['1']['last_updated_date'])
    assert re.search(r'\d{1,2}\/\d{1,2}\/\d{4}', dict_['1']['last_updated_date'])

def test_app_DELETE_todo_success():
    result = client.delete('/todos/1')
    assert result.status_code == 204
    result = client.get('/todos/1')
    assert result.status_code == 404
