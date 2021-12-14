import flask
import json


app = flask.Flask(__name__)

persons = [
    {
        'first_name': 'Anna',
        'last_name': 'Andersson',
        'age': 34
    },
    {
        'first_name': 'Bo',
        'last_name': 'Bengtsson',
        'age': 56
    }
]


@app.get('/')
def index_get():
    json_persons = json.dumps(persons)

    return flask.Response(json_persons, 200, content_type='application/json')


@app.post('/')
def index_post():
    data = flask.request.json
    persons.append(data)
    return flask.Response('{"status" : "Created"}', 201, content_type='application/json')


if __name__ == '__main__':
    app.run()
