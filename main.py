
from flask import Flask, request, make_response
from entry import *


app = Flask(__name__)


def response(string):
    response = make_response(string, 200)
    response.mimetype = "text/plain"
    return response


@app.route('/get')
def get():
    name = request.args.get('name')
    if ' ' in name:
        return response('Inputs cannot contain spaces')
    result = get_entry(name)
    print(result)
    if result is not None and result['value'] is not None:
        return response(str(result['value']))
    else:
        return response('None')


@app.route('/set')
def set():
    name = request.args.get('name')
    value = request.args.get('value')
    if ' ' in name or ' ' in value:
        return response('Inputs cannot contain spaces')
    try:
        set_entry(name, value)
    except:
        return response('some error occurred')
    else:
        return response(str(name) + ' = ' + str(value))


@app.route('/unset')
def unset():
    name = request.args.get('name')
    if ' ' in name:
        return response('Inputs cannot contain spaces')
    try:
        succeeded = unset_entry(name)
        if succeeded is False:
            return response('Value does not exist')
    except:
        return response('some error occurred')
    else:
        return response(str(name) + ' = ' + str(None))


@app.route('/numequalto')
def numequalto():
    value = request.args.get('value')
    if ' ' in value:
        return response('Inputs cannot contain spaces')
    result = num_equal_to(value)
    return response(str(result))


@app.route('/end')
def end():
    clean()
    return response('CLEANED')

@app.route('/undo')
def on_undo():
    response_object  = undo()
    if response_object is False:
        return response('Nothing to undo')
    variable_name = response_object[0]
    new_value = response_object[1]
    return response(str(variable_name) + ' = ' + str(new_value))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
