from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper

#init app and class
app = Flask(__name__)
modelHelper = ModelHelper()



# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")




@app.route("/nlp", methods=["POST"])
def recommendation_df():

    content = request.json["data"]

    print(content)
    # parse
    bookTitle = str(content["bookTitle"])
    rating_min = float(content["rating_min"])

    #dummy data
    #bookTitle = 'The Hunger Games'
    #rating_min = 1.0

    recommendation = modelHelper.recommendation_df(rating_min, bookTitle)
    print(recommendation)
    return(jsonify({"ok": True, "recommendation": (recommendation)}))






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
    app.run(debug=True)