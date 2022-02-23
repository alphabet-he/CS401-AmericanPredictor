#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
from flask import Flask
from flask import request
from flask import jsonify


# In[ ]:


app = Flask(__name__)
app.model = pickle.load(open("model.pkl", "rb"))

@app.route("/api/american", methods=["POST"])
def predict_tweet():
    x = request.get_json(force=True)
    text = x["text"]
    predicted = app.model.predict([text])
    ans = int(predicted[0])
    return jsonify(
        is_american = ans,
        version = "1.0",
        model_date = "2022-02-19"
    )

