from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper1
from modelHelper2 import ModelHelper


#init app and class
app = Flask(__name__)
modelHelper1 = ModelHelper1()
modelHelper = ModelHelper()



# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/goodreads")
def goodreads():
    # Return template and data
    return render_template("Goodreads.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau2.html")

@app.route("/datatable")
def datatable():
    # Return template and data
    return render_template("Datatable.html")

@app.route("/workscited")
def workscited():
    # Return template and data
    return render_template("workscited.html")

@app.route("/aboutUS")
def aboutus():
    # Return template and data
    return render_template("about.html")

@app.route("/paper")
def paper():
    # Return template and data
    return render_template("paper.html")

@app.route("/nlp")
def nlp():
    # Return template and data
    return render_template("nlp.html")


@app.route("/nlpRecommendations", methods=["POST"])
def recommendation_df():

    content = request.json["data"]
    print(content)

    # parse
    bookTitle = str(content["bookTitle"])

    recommendation = modelHelper1.recommendation_df(bookTitle)
    print(recommendation)
    return(jsonify({"ok": True, "recommendation":json.loads(recommendation.to_json(orient="records"))})) 

@app.route(‘/knn_rec’)
def knn():
    return render_template(‘knn_rec.html’)

@app.route(“/knn”, methods=[“POST”])
def knn_recommender():
    content = request.json[“data”]
    print(f”CONTENT: {content}“)
    # parse
    bookTitle = str(content[“bookTitle”])
    recommendation = modelHelper.knn_recommender(bookTitle)
    print(f”Recommendation: {recommendation}“)
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
    app.run(debug=True)