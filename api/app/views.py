from flask import request, jsonify, send_from_directory
import io
from app import app
from config import Configuration

import matplotlib.pyplot as plt


@app.route('/test/', methods=['GET'])
def test():
    return jsonify({'return': 'hello world'})


@app.route('/api/plot', methods=['POST'])
def plot():

    json_data = request.get_json()

    x = json_data['x']
    y = json_data['y']

    # Plot the data
    plt.plot(x, y)

    # Title of the graph
    if 'title' in json_data.keys():
        plt.title(json_data['title'])

    # X and Y labels
    if 'xLabel' in json_data.keys():
        plt.xlabel(json_data['xLabel'])
    if 'yLabel' in json_data.keys():
        plt.ylabel(json_data['yLabel'])

    plt.savefig("/app/outputs/plot.png")

    return send_from_directory('/app/outputs/',
                               'plot.png', as_attachment=True)
