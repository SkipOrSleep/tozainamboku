import os
import yaml
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

with open('../lib/data.yml', 'r') as datafile:
    data = yaml.safe_load(datafile)

@app.route('/cityname/<cityname>', methods=['GET'])
def getByCityname(cityname):
    for d in data:
        if d["name"] == cityname:
            return jsonify(d)

    return '', 404

@app.route('/citycode/<citycode>', methods=['GET'])
def getByCitycode(citycode):
    for d in data:
        if d["code"] == citycode:
            return jsonify(d)

    return '', 404


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, '.'), 'favicon.ico', )


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT')))
