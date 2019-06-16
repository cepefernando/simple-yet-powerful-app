from flask import Flask
import json
import pytest

total = 2 * 9
app = Flask(__name__)

#1 Do a simple math 
@app.route('/simplemath')
def calculation():
   return str(total)

#2 Display static text
@app.route('/statictext')
def static_text():
   return 'This is a simple text'

#3 Print given parameter
@app.route('/input/<name>')
def hello_name(name):
   return 'Hello %s!' % name

#4 Return JSON
@app.route('/json')
def retjson():
	return json.dumps({
        "name": "Foo Bar",
        "age": 78,
        "friends": ["Jane","John"],
        "balance": 345.80,
        "other_names":("Doe","Joe"),
        "active":True,
        "spouse":None
    }, sort_keys=True, indent=4)
	 

@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client

#UnitTesting for 1
def test_simple_math(client):
    response = client.get('/simplemath')
    assert str(total) == str(18) in response.data

#UnitTesting for 2
def test_static_text(client):
    response = client.get('/statictext')
    assert b'This is a simple text' in response.data

#UnitTesting for 3
def test_input_text(client):
	response = client.get('/input/test-input')  
	assert b'test-input' in response.data

#UnitTesting for 4
def test_json(client):
	response = client.get('/json')  
	assert response.status_code == 200

if __name__ == '__main__':
   app.run(debug = True)