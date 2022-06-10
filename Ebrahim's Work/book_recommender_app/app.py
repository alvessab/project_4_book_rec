from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
import logging
from modelHelper2 import ModelHelper


#init app and class
app = Flask(__name__)
modelHelper = ModelHelper()

app.logger.setLevel(logging.DEBUG)

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route('/knn_rec')
def knn():
    return render_template('knn_rec.html')

@app.route("/knn", methods=["POST"])
def knn_recommender():

    content = request.json["data"]
    print(f"CONTENT: {content}")

    # parse
    bookTitle = str(content["bookTitle"])

    recommendation = modelHelper.knn_recommender(bookTitle)
    print(f"Recommendation: {recommendation}")
    # return(jsonify({"ok": True, "recommendation":json.loads(recommendation.to_json(orient="records"))}))
    return jsonify(recommendation)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = '8000')