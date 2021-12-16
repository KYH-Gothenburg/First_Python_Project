import flask
import json


app = flask.Flask(__name__)


def read_data():
    with open('data.json', 'r') as json_file:
        return json.load(json_file)


def save_data(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


@app.get('/persons')
def index_get():
    json_persons = json.dumps(read_data())
    return flask.Response(json_persons, 200, content_type='application/json')


@app.post('/persons')
def index_post():
    data = flask.request.json
    valid_keys = ['first_name', 'last_name', 'age']
    for key in data:
        if key not in valid_keys:
            return flask.Response('{"status": "Error", "reason": "Json format error. Key ' + key + ' not allowed."}',
                                  400,
                                  content_type='application/json')
    persons = read_data()
    persons.append(data)
    save_data(persons)
    return flask.Response('{"status" : "Created"}', 201, content_type='application/json')


if __name__ == '__main__':
    app.run()
