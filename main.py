
from flask import Flask, request, jsonify
from entry import *


app = Flask(__name__)


@app.route('/get')
def get():
    name = request.args.get('name')
    result = get_entry(name)
    print(result)
    if result is not None and result['value'] is not None:
        return jsonify(result['value'])
    else:
        return jsonify('None')


@app.route('/set')
def set():
    name = request.args.get('name')
    value = request.args.get('value')
    try:
        set_entry(name, value)
    except:
        return jsonify('some error occurred')
    else:
        return jsonify({name: value})


@app.route('/unset')
def unset():
    name = request.args.get('name')
    try:
        unset_entry(name)
    except:
        return jsonify('some error occurred')
    else:
        return jsonify({name: None})


@app.route('/numequalto')
def numequalto():
    value = request.args.get('value')
    result = num_equal_to(value)
    return jsonify(result)
    # try:
    # except:
    #     return jsonify('some error occurred')
    # else:


@app.route('/end')
def end():
    clean()
    return jsonify('CLEANED')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
